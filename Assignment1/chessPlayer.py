import random


#White: Offset=10
#Black: Offset=20

#Piece: Value
#Pawn:   +0
#Knight: +1
#Bishop: +2
#Rook:   +3
#Queen:  +4
#King:   +5

class queue:
   def __init__(self):
      self.store = []
      self.length = 0
           
   def push(self, value):
      self.store = self.store + [value]
      self.length = self.length + 1
     
   def pop(self):
      if self.length == 0:
         return False
      rval = self.store[0]
      del (self.store[0])
      self.length = self.length - 1
      return rval


class evalTree:
   def __init__(self,x):
      self.store = [x,[]]

   def AddSuccessor(self,x):
      self.store[1] = self.store[1] + [x]
      return True
   
   def Helper(self, indentlevel):
      print (self.store[0])
      for i in range (len(self.store[1])):
         temp = self.store[1][i]
        #tab character
         for j in range (0, indentlevel):
            print ("\t",)
         temp.Helper(indentlevel+1)
      return 0
         
   def Print_DepthFirst(self):
      self.Helper(1)
      return 0

   def Get_LevelOrder (self):
      Q1 = queue()
      Q1.push(self)
      popList = []
      Failure = 0
      while (Failure != 1):
        try:
          popped = Q1.pop()
          popList = popList + [popped.store[0]]
        except:
          Failure = 1
          break
        if (popped.store[1] != None):
          #push in the children lists
          for i in range (len(popped.store[1])):
            Q1.push(popped.store[1][i])
      return popList

   def LevelHelper(self, Q1):
      #check for children 
      if (self.store[1] != None):
         self.LevelPusher(Q1)
         for i in range (len(self.store[1])):
            temp2 = self.store[1][i]
            print ("   Finding children of:", temp2.store[0],"")
            temp2.LevelHelper(Q1)
   
   def LevelPusher(self, Q1):
      for i in range (len(self.store[1])):
          Q1.push(self.store[1][i].store[0])
          print ("Pushing: ",self.store[1][i].store[0],"")
 

def getPiece(name):
   if name=="pawn":
      return 0
   elif name=="knight":
      return 1
   elif name=="bishop":
      return 2
   elif name=="rook":
      return 3
   elif name=="queen":
      return 4
   elif name=="king":
      return 5
   else:
      return -1

def genBoard():
   r=[0]*64
   White=10
   Black=20
   for i in [ White, Black ]:
      if i==White:
         factor=+1
         shift=0
      else:
         factor=-1
         shift=63
      r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
      r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
      r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
      if i==White:
         r[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*3] = i+getPiece("king")
      else:
         r[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
         r[shift+factor*4] = i+getPiece("king")
      for j in range(0,8):
         r[shift+factor*(j+8)] = i+getPiece("pawn")
   return r

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   return accum

def isWhite(n):
   if n>=10 and n<20:
      return 10
   elif n>=20 and n<30:
      return 20
   else:
      return 0

  
def GetPlayerPositions(board,player):
   rlist = []
   for pos in range(len(board)):
      if (isWhite(board[pos]) == isWhite(player)):
         rlist= rlist+[pos]
   return rlist 

def IsOnBoard(pos):
   if (pos >= 0) and (pos <= 63):
      return True
   return False

def GetBishopMoves(board,pos,piece):
#   print("BISHOP")
   nr = pos % 8
   nl = 7 - nr
   accum=[]
   ul=ll=ur=lr = pos
   for i in range(0,nr,1):
      ur += 7
      if not IsOnBoard(ur):
         break
      if board[ur] == 0:
         accum+=[ur]
      elif isWhite(piece) != isWhite(board[lr]):
         accum+=[ur]
         break
      else:
         break
#   print("UPRIGHT")
#   print(accum)

   for i in range(0,nr,1):
      lr -= 9
      if not IsOnBoard(lr):
         break
      #   if board[lr] == 0 and (isWhite(piece) != isWhite(board[lr])):
      if board[lr] == 0:
         accum+=[lr]
      elif isWhite(piece) != isWhite(board[lr]):
         accum+=[lr]
         break
      else:
         break
#   print("DOWNRIGHT")
#   print(accum)

   for i in range(0,nl,1):
      ul += 9
      if not IsOnBoard(ul):
         break #   if board[ul] == 0 and (isWhite(piece) != isWhite(board[ul])):
      if board[ul] == 0:
         accum+=[ul]
      elif isWhite(piece) != isWhite(board[ul]):
         accum+=[ul]
         break
      else:
         break
#   print("UPLEFT")
#   print(accum)

   for i in range(0,nl,1):
      ll -= 7
      if not IsOnBoard(ll):
         break
      #   if board[ll] == 0 and (isWhite(piece) != isWhite(board[ll])):
      if board[ll] == 0:
         accum+=[ll]
      elif isWhite(piece) != isWhite(board[ll]):
         accum+=[ll]
         break
      else:
         break
   return accum

def GetRookMoves(board,pos,piece):
#   print("ROOK")
   nl = pos % 8
   nr = 7 - nl 
   nd = pos / 8
   nu = 7 - (pos / 8)
   accum=[]
   left=right=up=down=pos
   for i in range(0,int(nl),1):                     
      left -= 1                                
      if not IsOnBoard(left):                      
         break
      if board[left] == 0:
         accum +=[left]
      elif isWhite(piece) != isWhite(board[left]):
         accum+=[left]
         break
      else:
         break
#   print("LEFT")
#   print(accum)
                                                
   for i in range(0,int(nr),1):                     
      right += 1                               
      if not IsOnBoard(right):                     
         break
      if board[right] == 0:
         accum+=[right]
      elif isWhite(piece) != isWhite(board[right]):
         accum+=[right]
      else:
         break
#   print("RIGHT")
#   print(accum)
                                                
   for i in range(0,int(nd),1):                     
      down -= 8                                
      if not IsOnBoard(down):                     
         break
      if board[down] == 0:
         accum+=[down]
      elif isWhite(piece) != isWhite(board[down]):
         accum+=[down]
      else:
         break
#   print("DOWN")
#   print(accum)
                                               
   for i in range(0,int(nu),1):                     
      up += 8                                  
      if not IsOnBoard(up):                     
         break
      if board[up] == 0:
         accum+=[up]
      elif isWhite(piece) != isWhite(board[up]):
         accum+=[up]
      else:
         break
#   print("UP")
#   print(accum)
   return accum


def KnightHelper(a,b):
   if abs(a/8 - b/8) >2 or abs(a%8 - b%8)>2:
      return False
   return True

def GetKingMoves(pos):
   accum = []
   tst=[]
   left = pos+1
   right = pos-1
   up = pos+8
   down = pos-8
   ul = up+1
   ur = up-1
   dl = down+1
   dr = down-1
   tst = [left,right,up,down,ul,ur,dl,dr]
   for val in tst:
      if IsOnBoard(val) and KnightHelper(pos,val):
         accum+=[val]
   return accum


def GetKnightMoves(pos):
   accum = []
   tst = []
   ull = pos+10
   ulu = pos+17
   urr = pos+6
   uru = pos+15
   dll = pos-6
   dld = pos-15
   drr = pos-10
   drd = pos-17

   tst = [ull,ulu,urr,uru,dll,dld,drr,drd]
   for val in tst:
      if IsOnBoard(val) and KnightHelper(pos,val):
         accum+=[val]
   return accum
   
 
 
def GetPieceLegalMoves(board,position):
   #return a list of all legal positions that the piece in the given position can take
   tst = []
   rlist = []
   piece = board[position]
   player = isWhite(piece)
   #pawn
   if piece - player == 0:
      if piece == 10:
         mult = 1
      else:
         mult = -1 

      if IsOnBoard(position+(mult*8)):
         rlist += [position+(mult*8)]
      if IsOnBoard(position+(mult*9)):
         if (isWhite(position+(mult*9)) != isWhite(piece)) and (board[position+(mult*9)] != 0):
            rlist +=[position+(mult*9)]
      if IsOnBoard(position+(mult*7)):
         if (isWhite(position+(mult*7)) != isWhite(piece)) and (board[position+(mult*7)] != 0):
            rlist +=[position+(mult*7)]
      return rlist

#knight
   elif piece - player == 1:
      tst=GetKnightMoves(position)
      for pos in tst:
         if (board[pos] == 0 or isWhite(piece) != isWhite(board[pos])):
            rlist +=[pos]
      return rlist

#bishop
   elif piece - player == 2:
      return GetBishopMoves(board,position,piece)
      return rlist
            
#rook
   elif piece - player == 3:
      return GetRookMoves(board,position,piece)
#queen 
   elif piece - player == 4:
      a1 = GetRookMoves(board,position,piece) 
#      print(a1)
      a2 = GetBishopMoves(board,position,piece)
#      print(a2)
      accum = a1+a2
      rlist = []
      for i in range(len(accum)):
         if accum[i] not in rlist:
            rlist+=[accum[i]] 
      
      return rlist
      

#king
   elif piece - player == 5:
      tst =  GetKingMoves(position)
      for pos in tst:
         if (board[pos] == 0 or isWhite(piece) != isWhite(board[pos])):
            rlist +=[pos]
      return rlist

def IsPositionUnderThreat(board,position,player):
  if board[position] == 0:
    #print ("Empty position")
    return False
  else:
    if (player == 10):
      enemyPositions = GetPlayerPositions(board,20)
    elif (player == 20):
      enemyPositions = GetPlayerPositions(board,10)
    else:
      return False
  
      
    for i in range (0,len(enemyPositions)):
      enemyMoves = GetPieceLegalMoves(board, enemyPositions[i])

      for j in range (0, len(enemyMoves)):
        if (enemyMoves[j] == position):
    
          return True
    
    return False 


#relative piece strengths
#pawn = +- 10
#knight = +-30
#bishop = +-30
#rook = +-50
#queen = +-90
#king = +- 900

def boardScore(board):
   score = 0
   whitepawn = [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
                5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
                1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
                0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
                0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0, 
                0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5, 
                0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5, 
                0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
   
   blackpawn = list(reversed(whitepawn))
   knight = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0, 
             -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0, 
             -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0, 
             -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
             -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0, 
             -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0, 
             -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0, 
             -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
   
   whitebishop =  [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0, 
                   -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0, 
                   -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0, 
                   -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0, 
                   -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0, 
                   -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0, 
                   -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0, 
                   -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
   
   blackbishop = list(reversed(whitebishop))
   
   whiterook = [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  
                 0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
                -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, 
                -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, 
                -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, 
                -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5, 
                -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,  
                 0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
   
   blackrook = list(reversed(whiterook))
   
   queen = [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0, 
             -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0, 
             -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0, 
             -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5, 
              0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5, 
             -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0, 
             -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0, 
             -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
   
   whiteking = [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, 
                 -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                 -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, 
                 -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, 
                 -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0, 
                 -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
                  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
                  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
   
   blackking = list(reversed(whiteking))
  
   for i in range(0,64):
      if (board[i] == 10):
         score = score + 10 + whitepawn[63-i]
      elif (board[i] == 20):
         score = score - 10 - blackpawn[63-i]
      elif (board[i] == 11):
         score = score + 30 + knight[63-i]
      elif (board[i] == 21):
         score = score - 30 - knight[63-i]
      elif (board[i] == 12):
         score = score + 30 + whitebishop[63-i]
      elif (board[i] == 22):
         score = score - 30 - blackbishop[63-i]
      elif (board[i] == 13):
         score = score + 50 + whiterook[63-i]
      elif (board[i] == 23):
         score = score - 50 - blackrook[63-i]
      elif (board[i] == 14):
         score = score + 90 + queen[63-i]
      elif (board[i] == 24):
         score = score - 90 - queen[63-i]
      elif (board[i] == 15):
         score = score + 900 + whiteking[63-i]
      elif (board[i] == 25):
         score = score - 900 - blackking[63-i]
   return score 


def generateBoardMove (board,initialposition,finalposition):
   newBoard = []
   for i in range (0,64):
      newBoard = newBoard + [board[i]]
   newBoard[finalposition] = board[initialposition]
   newBoard[initialposition] = 0
   return newBoard 

def minimax(moves, depth, minimum, maximum, maximizingPlayer): 
   leaf = 0
   try: 
      temp = moves.store[1][0]
   except:
      leaf = 1
 
   if depth == 0 or leaf == 1:
      return boardScore(moves.store[0][3])
     
   if maximizingPlayer == True:
      v = minimum
      for i in range (0,len(moves.store[1])): 
         vnew = minimax(moves.store[1][i],depth-1,v,maximum,False)
         if vnew > v:
            v = vnew
         if v > maximum:
            return maximum
      return v
     
   elif maximizingPlayer == False:
     v = maximum
     for i in range (0,len(moves.store[1])):
        vnew = minimax(moves.store[1][i],depth-1,minimum,v,True)
        if vnew < v:
           v = vnew
        if v < minimum:
           return minimum
     return v
   
def treeGenerator (depth,board,player,moves):
   if depth == 0:
      return moves
   positions = GetPlayerPositions(board,player)
   if isWhite(player):
      enemy = 20
   else:
      enemy = 10
   
   kingpositioninitial = -1
   for i in range (0,64):
      if board[i] == player+5:
         kingpositioninitial = i
        
   if kingpositioninitial == -1:
      status = False 
      print ("King is dead; Player",player,"lost.")
      return moves
   
   #record possible moves for current player 
   moves1 = []
   pieces1 = []
   for i in range (len(positions)):
      moves1 = moves1 + [GetPieceLegalMoves(board,positions[i])]
      pieces1 = pieces1 + [positions[i]]
   
   moves1final = []
   pieces1final = []
   for i in range (0,len(pieces1)):
      for j in range (0,len(moves1[i])):
         newBoard = generateBoardMove(board,pieces1[i],moves1[i][j])
         kingposition = -1
         for x in range (0,64):
            if newBoard[x] == player+5:
               kingposition = x
            
         if kingposition != -1:
            if IsPositionUnderThreat(newBoard,kingposition,player) == True:
               #print 'The king position at threat is',kingposition
               pass
            else:
               moves1final = moves1final + [moves1[i][j]]
               pieces1final = pieces1final + [pieces1[i]]
   
   
   boards1 = []
   for i in range (0,len(pieces1final)):
      newBoard = generateBoardMove(board,pieces1final[i],moves1final[i])
      score = boardScore(newBoard)
      #print (score)
      boards1 = boards1 + [[pieces1final[i],moves1final[i],score,newBoard]]
   
   #add to the tree
   for i in range(0,len(boards1)):
      addedTree = evalTree(boards1[i])
      addedTree = treeGenerator(depth-1,boards1[i][3],enemy,addedTree)
      moves.AddSuccessor(addedTree)
   return moves



def chessPlayer(board,player):
   status = False 
   if isWhite(player): 
     enemy = 20
   else:
     enemy = 10
   
   #make sure kings are still alive, otherwise no valid moves 
   kingpositioninitial = -1
   enemyking = -1
   for i in range (0,64):
     if board[i] == player+5:
        kingposinit = i
     if board[i] == enemy+5:
        enemyking = i
       
   if kingposinit == -1:
     status = False 
     print ("King is dead; Player",player,"lost.")
     return [status,[],[],[]]
     
   elif enemyking == -1:
     status = False
     print ("King is dead; Player",enemy,"lost.")
     return [status,[],[],[]]
     
   else:
     moves = evalTree(board)
     moves = treeGenerator(3,board,player,moves)
     output = moves.Get_LevelOrder()
    
     if player == 10:
        maximizingPlayer = True
     elif player == 20:
        maximizingPlayer = False
     
     level1minimax = []
     for i in range (0,len(moves.store[1])):
        level1minimax = level1minimax + [minimax(moves.store[1][i],3,-9999,9999,maximizingPlayer)]
       
     #print (level1minimax)
     
     if maximizingPlayer == True:
       # print ("Max:",max(level1minimax))
        index = level1minimax.index(max(level1minimax))
     else:
       # print ("Min:",min(level1minimax))
        index = level1minimax.index(min(level1minimax))
     
     
     move = [output[index+1][0],output[index+1][1]]
     #print (move)
     candidateMoves = []
     for i in range (1,len(level1minimax)+1):
        newMove = [output[i][0],output[i][1]]
        moveScore = float(output[i][2])
        candidateMoves = candidateMoves + [[newMove,moveScore]]
     evalTree1 = output
     status = True
     finalOutput = [status,move,candidateMoves,evalTree1]
     return finalOutput
     
     
  


def main():
   board=genBoard()
   newBoard = board
   print (printBoard(newBoard),'\n')
   invalid = True
   while invalid:
      try:
         output = chessPlayer(newBoard,10)
         newBoard = generateBoardMove(newBoard,output[1][0],output[1][1])
         print (printBoard(newBoard),'\n')
         positions = GetPlayerPositions(board,20)
         #record possible moves for current player 
         moves1 = []
         pieces1 = []
         for i in range (len(positions)):
            moves1 = moves1 + [GetPieceLegalMoves(newBoard,positions[i])]
            pieces1 = pieces1 + [positions[i]]
           # print("=======All possible moves =======")
           # print(moves1)
           # print(pieces1)
         #fix the moves and pieces lists to only have valid moves and pieces(king threat check)
         moves1final = []
         pieces1final = []
         for i in range (0,len(pieces1)):
            for j in range (0,len(moves1[i])):
               testBoard = generateBoardMove(newBoard,pieces1[i],moves1[i][j])
               kingposition = -1
               for x in range (0,64):
                  if testBoard[x] == 25:
                     kingposition = x
               if kingposition != -1:
                  if IsPositionUnderThreat(testBoard,kingposition,20) == True:
                     pass
                  elif IsPositionUnderThreat(testBoard,moves1[i][j],20) == True:
                     pass
                  else:
                     moves1final = moves1final + [moves1[i][j]]
                     pieces1final = pieces1final + [pieces1[i]]
         #print ("MOVES FINAL",moves1final)
         #print ("PIECES FINAL",pieces1final)
         
         randomindex = random.randint(0,len(moves1final)-1)
         newBoard = generateBoardMove(newBoard,pieces1final[randomindex],moves1final[randomindex])
        
         print("==========New Move ============") 
         print ([pieces1final[randomindex],moves1final[randomindex]])
         print (printBoard(newBoard),'\n')
      except:
         invalid = False
         print ('Game over.')
main()
