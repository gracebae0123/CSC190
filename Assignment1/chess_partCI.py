from chess import *

def generateBoardMove (board,init,final):
   newBoard = []
   for idx in range (0,64,1):
      newBoard += [board[idx]]
   newBoard[final] = board[init]
   newBoard[init] = 0
   return newBoard

board = genBoard()
rlist = []
invalid = True 
count = 0

while True:
   invalid = True 
   count = 0
   print ("\n")
   print (printBoard(board))
   while invalid:
      current = input("White moves from?")
      final = input("To?")
      if not isWhite(board[int(current)]):
         print ("CHOSE WRONG SIDE")
      else:
         rlist = GetPieceLegalMoves(board,int(current)) 
         print(rlist)
         if len(rlist) == 0:
            print ("EMPTY LIST RETURNED\n")
         else:
            for i in rlist:
               if int(final) != i:
                  count +=1
               elif int(final) == i:
                  board = generateBoardMove(board,int(current),int(final))
                  print (printBoard(board))
                  invalid = False 
                  break 
            if count == len(rlist):
               print ("INVALID")
            

   print ("\n")
   invalid = True
   count = 0
   while invalid:
      current = input("Black moves from?")
      final = input("To?")
      if isWhite(board[int(current)]):
         print("CHOSE WRONG SIDE")
      else:
         rlist = GetPieceLegalMoves(board,int(current))
         print(rlist)
         if len(rlist) == 0:
             print ("EMPTY LIST RETURNED\n")
         else:
            for i in rlist:
               if int(final) != i:
                  count +=1
               elif int(final) == i:
                  board = generateBoardMove(board,int(current),int(final))
                  print (printBoard(board))
                  invalid = False 
                  break 
            if count == len(rlist):
               print ("INVALID")
       
