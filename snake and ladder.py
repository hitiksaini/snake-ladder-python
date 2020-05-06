#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PIL import Image
import random
end=100

def show_board():
    img=Image.open("snake_ladder.png")
    img.show()
#note: I've not set the numbers as on a real ladder game so please check what numbers represnts ladder and customise this funct   
def check_ladder(points):ion.
    if(points==5):
        print('ladder')
        return 23
    elif(points==7):
        print("ladder")
        return 98
    else:
        return(points)
#note: I've not set the numbers as on a real snake game so please check what numbers represnts snake and customise this funct   
def check_snake(points):
    if(points==45):
        print("snake")
        return 22
    elif(points==99):
        print("snake")
        return 5
    else:
        return points
    
def reached_end(points):
    if(points==end):
        return True
    else:
        return False
    
def play():
    p1_name = input('Player1, Enter name: ')
    p2_name = input('Player2, Enter name: ')
    
    #initial point of players
    pp1=0 
    pp2=0
    
    turn=0 
    while(1):
        if(turn%2==0):     #this is a condition for player 1 turn 
            print(p1_name, " it's your turn.")
            choice=input("Press 1 to continue, 0 to Exit.")
            if(choice==0):
                print(p1_name , " scored ", pp1 , " points.")
                print(p2_name , " scored ", pp2 , " points.")
                print("Thanks for playing.")
                break
            dice=random.randint(1,6)
            print("Dice showed- ",dice)
            #points for player 1
            pp1=pp1+dice
            #to check whether playyer 1 encounters the snake or a ladder 
            pp1=check_ladder(pp1)    
            pp1=check_snake(pp1)
            #not to exceed the end score 100
            if(pp1>end):
                pp1=end
            print(p1_name, " your score ", pp1)
            
            if(reached_end(pp1)):
                print(p1_name, " won ")
                break
        else:
            print(p2_name, " it's your turn.")
            choice=input("Press 1 to continue, 0 to Exit.")
            if(choice==0):
                print(p1_name , " scored ", pp1 , " points.")
                print(p2_name , " scored ", pp2 , " points.")
                print("Thanks for playing.")
                break
            dice=random.randint(1,6)
            print("Dice showed- ",dice)
            #points for player 2
            pp2=pp2+dice
            #to check whether playyer 1 encounters the snake or a ladder 
            pp2=check_ladder(pp2)    
            pp2=check_snake(pp2)
            #not to exceed the end score 100
            if(pp2>end):
                pp2=end
            print(p2_name, " your score ", pp2)
            
            if(reached_end(pp2)):
                print(p2_name, " won ")
                break
        turn=turn+1
        
show_board()
play()


# In[ ]:




