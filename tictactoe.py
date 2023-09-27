import random
# my board
acceptable_numbers=[1,2,3,4,5,6,7,8,9]
board=[[1,2,3],[4,5,6],[7,8,9]]
# my rews and columns
rows=3
columns=3
counter=0
print('\nHey there, welcome to my your Awesome tictactoe game.\n')
way=input("Who do you want to play with, the computer or a friend\t:").upper()
for i in range(rows):
    print('\n+------------+')
    print('| ', end='')
    for j in range(columns):
        print(f' * |', end='')
print('\n+------------+')

# The mistake i made in my main.py was that i made my complete board a string instead of a function
def completeboard():
    for i in range(rows):
        print('\n+------------+')
        print('| ',end='')
        for j in range(columns):
            print(f' {board[i][j]} |' ,end='')
    print('\n+------------+')

def replace(num,letter):
#     i am going to subtract 1 from num because you know how list index works
    acceptable_numbers.remove(num)
    num-=1
    if num==0:
        board[0][0]=letter
    elif num==1:
        board[0][1]=letter
    elif num==2:
        board[0][2]=letter
    elif num==3:
        board[1][0]=letter
    elif num==4:
        board[1][1]=letter
    elif num==5:
        board[1][2]=letter
    elif num==6:
        board[2][0]=letter
    elif num==7:
        board[2][1]=letter
    elif num==8:
        board[2][2]=letter



def checker():
#     for the rows
    if(board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X' ):
        print('Hurray frist palyer wins  win🥳, second player, you lose😕')
        return True
    elif(board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X' ):
        print('Hurray frist palyer wins  win🥳, second player, you lose😕')
        return True
    elif(board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X' ):
        print('Hurray frist palyer wins  win🥳, second player, you lose😕')
        return True
    elif(board[0][0]=='O' and board[0][1]=='O' and board[0][2]=='O' ):
        print('Hurray player 2 you win🥳,Plapyer1 You lose😕')
        return True
    elif(board[1][0]=='O' and board[1][1]=='O' and board[1][2]=='O' ):
        print('Hurray player 2 you win🥳,Plapyer1 You lose😕')
        return True
    elif(board[2][0]=='O' and board[2][1]=='O' and board[2][2]=='O' ):
        print('Hurray player 2 you win🥳,Plapyer1 You lose😕')
        return True
#     for the columns
    if(board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X' ):
        print('Hurray frist palyer wins  win🥳, second player, you lose😕')
        return True
    elif(board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X' ):
        print('Hurray frist palyer wins  win🥳, second player, you lose😕')
        return True
    elif(board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X' ):
        print('Hurray frist palyer wins  win🥳, second player, you lose😕')
        return True
    elif(board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O' ):
        print('Hurray player 2 you win🥳,Plapyer1 You lose😕')
        return True
    elif(board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O' ):
        print('Hurray player 2 you win🥳,Plapyer1 You lose😕')
        return True
    elif(board[0][2]=='O' and board[1][2]=='O' and board[2][2]=='O' ):
        print('Hurray player 2 you win🥳,Plapyer1 You lose😕')
        return True
#     for the crossroads
    if(board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X' ):
        print('Hurray frist palyer wins  win🥳, second player, you lose😕')
        return True
    elif(board[2][0]=='O' and board[1][1]=='O' and board[0][2]=='O' ):
        print('Hurray player 2 you win🥳,Plapyer1 You lose😕')
        return True



if way=='FRIEND':
    while counter<9:

        if counter % 2 == 0:
            counter += 1
            player1=int(input('Type in the number you want to replace :'))
            if (player1 in acceptable_numbers):
                replace(player1,'X')
                completeboard()
            else:
                print('You entered a number that has been entered before.START AGAIN')
                break
        else:
            counter += 1
            player2=int(input('Type in the number you want to replace :'))
            if player2 in acceptable_numbers:
                replace(player2,'O')
                completeboard()
        if checker():
            break
else:
    print('The computer is player2\n')
    while counter < 9:
        if counter % 2 == 0:
            counter += 1
            player1 = int(input('Type in the number you want to replace :'))
            if (player1 in acceptable_numbers):
                replace(player1, 'X')
                completeboard()
            else:
                print('You entered a number that has been entered before.START AGAIN')
                break
        else:
            counter += 1
            comp_input = random.choice(acceptable_numbers)
            replace(comp_input, 'O')
            completeboard()
        if checker():
            break

# i didn't have to make a 2d list.I should have worked with my 1 d list and made winnin combinations