# Tic TAC TOE

grid=[[0,1,2],[3,4,5],[6,7,8]]
def screen_show():
    print("              ","Select the number 0-8  which is showing on the screen")
    print("Player1 Symbol 'P1' ")
    print("Player2 Symbol 'P2' ")
screen_show()    
# Grid print 
def grid_draw():
  length=len(grid)
  n=0
  i=0
  while(n!=length):
 
     print(grid[n][i],"|",grid[n][i+1],"|",grid[n][i+2])
     print("---------")
     n=n+1

grid_draw()
#User input 
#check game
def check_game():
     n=0
     lenght = len(grid)
     #column wise check
     while(n!=lenght):
        
        if(grid[n][0] == 'P1' and grid[n][1]=='P1' and grid[n][2]=='P1'):
         print("Player 1 is winner :)")
         print("Game Over :(")
         quit(1)
        if(grid[n][0] == 'P2' and grid[n][1]=='P2' and grid[n][2]=='P2'):
         print("Player 2 is winner :)")
         print("Game Over :(")
         quit(1)
        else:
         n=n+1
    #row wise check  
     i=0
     while(i!=lenght):
        
        if(grid[0][i] == 'P1' and grid[1][i]=='P1' and grid[2][i]=='P1'):
         print("Player 1 is winner :)")
         print("Game Over :(")
         quit()
        if(grid[0][i] == 'P2' and grid[1][i]=='P2' and grid[2][i]=='P2'):
         print("Player 2 is winner :)")
         print("Game Over :(")
         quit()
        else:
         i=i+1
    # cross over check
     if(grid[0][0] =='P1'and grid[1][1]=='P1' and grid[2][2]=='P1'):
        print("Player 1 is winner :)")
        print("Game Over :(")
        quit()
     if(grid[0][0] =='P2'and grid[1][1]=='P2' and grid[2][2]=='P2'):
        print("Player 2 is winner :)")
        print("Game Over :(")
        quit()
     if(grid[0][2] =='P1'and grid[1][1]=='P1' and grid[2][0]=='P1'):
        print("Player 1 is winner :)")
        print("Game Over :(")
        quit()
     if(grid[0][2] =='P2'and grid[1][1]=='P2' and grid[2][0]=='P2'):
        print("Player 2 is winner :)")
        print("Game Over :(")
        quit()
     
# change grid number
def change(number,turn):
    
    length=len(grid)
    n=0
    prt=0
    
    while(n!=length):
        i=0
        while(i!=length):
         if(number==grid[n][i]) and turn=='P1' :
             grid[n][i]='P1'
             grid_draw()
             check_game()
             prt=1
             break
         elif(number==grid[n][i]) and turn=='P2' :
             grid[n][i]='P2'
             grid_draw()
             check_game()
             prt=1
             break
         else:
             i=i+1
            
        n=n+1 
    if(prt==0):
        print("Select from remaining numbers")
        user_input(turn)
        
    
        
    
def user_input(turn):
    
      num=int(input("Enter :"))
      while(num < 0 or num > 8):
        print("Choice from given numbers")
        num=int(input("Enter :"))
        
      change(num,turn)
   
 

# player turn
def player_turn():
     i=1
     while(i!=10) :
        if(i % 2 == 0):
         print('       Player 2 turn')    
         turn='P2'
         i=i+1
         
        else:
          print('     Player 1 turn')
          turn='P1'
          i=i+1
        user_input(turn)   
        
     if(i==10):
        print("No one win :(") 
        print('Game Over :(')  
        quit()
player_turn() 
