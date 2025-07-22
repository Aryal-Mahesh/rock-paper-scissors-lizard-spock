"""
Scissors cut Paper.
Paper covers Rock.
Rock crushes Lizard.
Lizard poisons Spock.
Spock smashes Scissors.
Scissors beat Lizard.
Lizard eats Paper.
Paper disproves Spock.
Spock vaporizes Rock.
Rock breaks Scissors.
"""
"""
================================
Rock Paper Scissors Lizard Spock
================================

1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
Pick a number: 3

You chose: ✌️
CPU chose: ✌️
It's a tie!
"""

print('=============================================')
print ("AS THE LEGEND SAID, THE NAME OF THE GAME IS:\n   'Rock-Paper-Scissors-Lizard-Spock'")
print('=============================================')
print('         1 is ROCK ✊ \n'  '         2 is PAPER ✋\n'  '         3 is SCISSORS ✌️ \n'  '         4 is LIZARD 🦎\n'  '         5 is SPOCK 🖖' )
print('=============================================')
print ("           RULES ALERT!")
print('=============================================')
print('        Scissors cut Paper.')
print('        Paper covers Rock.')
print('        Rock crushes Lizard.')
print('        Lizard poisons Spock.')
print('        Spock smashes Scissors.')
print('        Scissors beat Lizard.')
print('        Lizard eats Paper.')
print('        Paper disproves Spock.')
print('        Spock vaporizes Rock.')
print('        Rock breaks Scissors.')
print('=============================================')
import random 
game = ['Rock ✊', 'Paper ✋ ', 'Scissor ✌️']
game.append('Lizard 🦎')
game.append('Spock 🖖')
print("Here we go, Let me remind you again!")
print('=============================================')
#print(len(game))
for i in range(len(game)):
  print(f"{i+1}. {game[i]}")
print('=============================================')
your_choice = int(input("Choose a number from 1 to 5:"))
print('=============================================')

player = game[your_choice-1]
AI = random.choice(game)

print(f"You chose:",player)
print(f"AI choses:",AI)

player_move = player.split()[0]
ai_move = AI.split()[0]
print('=====kukukaka======kukukaka=======kukukaka===')
if player_move == ai_move:
  print("It is a tie.")
elif player_move == 'Rock' and ai_move in ['Scissors', 'Lizard']:
  print(f"Rock crushes/breaks {ai_move}. You win!")
elif player_move == 'Paper' and ai_move in ['Rock', 'Spock']:
  print(f"Paper beats {ai_move}. You win!")
elif player_move =='Scissors' and ai_move in ['Paper', 'Lizard']:
  print(f"Scissors cut {ai_move}. You win!")
else:
  print(f"{ai_move} beats {player_move}. You Lose!")
print('=============================================')
