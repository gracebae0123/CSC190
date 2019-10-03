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
   if n>= 0 and n<=16:
      return True
   return False

  
def GetPlayerPositions(board,player):
   rlist = []
   for pos in range(len(board)):
      if (isWhite(board[pos]) == isWhite(player)) and board[pos] != 0:
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
   #idx 0 = upright idx 1 = downright idx 2 = upleft idx 3 = downleft
   ul=ll=ur=lr = pos
   for i in range(0,nr,1):
      ur += 7
      if not IsOnBoard(ur):
         break
      #   if board[ur] == 0 and (isWhite(piece) != isWhite(board[ur])):
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
   #0 = left 1 = right 2 = down 3 = up
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


##def GetQueenMoves(pos):
##   return GetRookMoves(pos) + GetBishopMoves(pos)

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
   
#def GetPawnMoves (pos):
#   tst = []
#   accum = []
#   if ((pos >= 48) and (pos <= 55)) or ((pos >= 8) and (pos <= 15)):
#      if IsOnBoard(pos+16):
#         accum +=[pos+16]
#   if IsOnBoard(pos+8):
#      accum += [pos+8]  
#   tst = [pos+7, pos+9, pos-7, pos-9]
#   for val in tst:
#      if IsOnBoard(val):
#         accum+=[val]
#   return accum
   
 
def GetPieceLegalMoves(board,position):
   #return a list of all legal positions that the piece in the given position can take
   tst = []
   rlist = []
   piece = board[position]
   #check who it is 
   if isWhite(piece) == True:
      player = 10 #white
   else:
      player = 20 #black 
   print("DEBUGGING: COLOUR OF PLAYER = " + str(player)) 
   #pawn
   if piece - player == 0:
      if piece == 10:
         mult = 1
      else:
         mult = -1 

      if IsOnBoard(position+(mult*8)):
         rlist += [position+(mult*8)]
      if (isWhite(position+(mult*9)) != isWhite(piece)) and (board[position+(mult*9)] != 0):
         rlist +=[position+(mult*9)]
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
#      tst = GetBishopMoves(position)
#      rlist=[]
##      print(tst[0])
#      for val in tst[0]:
#         if len(tst[0]) == 0:
#            break
##         print("value of pos is.." + str(val))
#         if (board[val] == 0 or isWhite(piece) != isWhite(board[val])):
#            rlist+=[val]
#         else:
#            break
##      print(rlist)
##      print(tst[1])
#      for val in tst[1]:
#         if len(tst[1]) == 0:
#            break
#         if (board[val] == 0 or isWhite(piece) != isWhite(board[val])):
#            rlist+=[val]
#         else:
#            break
##      print(rlist)
##      print(tst[2])
#      for val in tst[2]:
#         if len(tst[2]) == 0:
#            break
#         if (board[val] == 0 or isWhite(piece) != isWhite(board[val])):
#            rlist+=[val]
#         else:
#            break
##      print(rlist)
##      print(tst[3])
#      for val in tst[3]:
#         if len(tst[3]) == 0:
#            break
#         if (board[val] == 0 or isWhite(piece) != isWhite(board[val])):
#            rlist+=[val]
#         else:
#            break
##      print(rlist)
      return rlist
            
#rook
   elif piece - player == 3:
      return GetRookMoves(board,position,piece)
#      nl = position %8
#      nr = 7-nl
#      nd = position/8
#      nu = 7-(position/8)
#      accum = []
#    #0 = left 1 = right 2 = down 3 = up         
#      left=right=up=down=position                      
#                                                   
#      for i in range(0,nl,1):                     
#         left -= 1                                
#         if IsOnBoard(left):                      
#           if (board[left] == 0 or isWhite(piece) != isWhite(board[left])):
#            accum += [left]                    
#           else:
#              break
#                                                   
#      for i in range(0,nr,1):                     
#         right += 1                               
#         if IsOnBoard(right):                     
#           if (board[right] == 0 or isWhite(piece) != isWhite(board[right])):
#            accum += [right]                   
#           else:
#              break
#                                                   
#      for i in range(0,nd,1):                     
#         down -= 8                                
#         if IsOnBoard(down):                      
#           if (board[down] == 0 or isWhite(piece) != isWhite(board[down])):
#            accum += [down]                   
#           else:
#              break
#                                                   
#      for i in range(0,nu,1):                     
#         up += 8                                  
#         if IsOnBoard(up):                        
#           if (board[up] == 0 or isWhite(piece) != isWhite(board[up])):
#            accum += [up]                   
#           else:
#              break
#      return accum
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
   play = GetPlayerPositions(board,player)
   for pos in play:
      LM = GetPieceLegalMoves(board, pos)
      if position in LM:
         return True
   return False 

def desire(board, temp, player,pval):
   rlist = GetPlayerPositions(board,player)
   for pos in rlist:
      blah = GetPieceLegalMoves(board,pos)
      for a in blah:
         if a ==temp:
            if (board[temp] == 20 or board[temp] == 10):
               pval.append(1)
            if (board[temp] >10 and board[temp] <20):
               pval.append(board[temp]%10)
            if (board[temp] >20):
               pval.append(board[temp]%10)
            return [temp,pos]
   return False 

def isKing(board):
   alpha = False
   beta = False
   for i in board:
      if i == 15:
         alpha = True
      if i == 25:
         beta = True
   return (alpha and beta)

#######################################################################
#print printBoard(range(0,64,1))
#board=genBoard()
#print "\nwhich will look like the following:"
#print printBoard(board)

#print ""
#print " Note 1: lower right hand square is WHITE"
#print " Note 2: two upper rows are for BLACK PIECES"
#print " Note 3: two lower rows are for WHITE PIECES"
#
#print "White occupies:"
#print GetPlayerPositions(board,10)
#print "Black occupies:"
#print GetPlayerPositions(board,20) 
