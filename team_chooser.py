from random import choice
User_input=input('Enter your members here to form teams. Please be sure to leave some space between the names:')
players=list(User_input.split())
print(players)
TeamA=[]
TeamB=[]

while len(players)>0:
    playerA=choice(players)
    print('Chosen player for TeamA:',playerA)
    TeamA.append(playerA)
    print('TeamA:',TeamA)
    players.remove(playerA)
    print('Players left:', players)
    if len(players)==0:
        break


    playerB=choice(players)
    print('Chosen player for TeamB:', playerB)
    TeamB.append(playerB)
    print('TeamB:',TeamB)
    players.remove(playerB)
    print('Players left:', players)


print('Final list for TeamA:', TeamA)
print('Final list for TeamB:', TeamB)
