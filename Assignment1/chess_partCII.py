from chess import *
from random import randint

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
whitept=[]
white = 0
blackpt = []
black = 0
cnt = 0
rat = 20

for p in range(0,rat):
   while True:
      invalid = True 
      count = 0
      print ("\n")
      print (printBoard(board))
      while invalid:
         accum=[]
         L = GetPlayerPositions(board,10)
         for moves in L:
            blah = GetPieceLegalMoves(board,moves)
            print("legal moves:" , blah)
            for i in blah:
               if not(IsPositionUnderThreat(board,i,10)):
                  accum+=[i]
            randnum = randint(0,len(accum))
            temp = accum[randnum]
            desire(board,temp,10,whitept)
            print(whitept)
            print("-------------white move---------",count)
            printBoard(board)
         accum = []
         L = GetPlayerPositions(board,20)
         for moves in L:
            blah = GetPieceLegalMoves(board,moves)
            print("legal moves:",blah)
            for i in blah:
               if not(IsPositionUnderThreat(board,i,20)):
                  accum+=[i]
         if not accum:
            break
         randnum = randint(0,len(accum))
         temp = accum[randum]
         desire(board,temp,20,blackpt)
         print (blackpt)
         print("----------------black move---------",count)
         printBoard(board)
         if not isKing(board):
            print("-------------Final move---------",count)
            printBoard(board)
            print("White had: ",sum(whitept),"points")
            print("Black had: ",sum(blackpt),"points")
            break
         if sum(whitept) > sum(blackpt):
            white+=1
         if sum(whitept) < sum(blackpt):
            black+=1
   
print("white is: ",white,"black is: ",black,"out of: ",rat) 
      


   
          

      
