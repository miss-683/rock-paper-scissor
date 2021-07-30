print('hello')
print('whats your name?')
username = input()
print('lets play paper scissor rock'+ ' ' + username)
print('any time wanted to end the game just type finish!')

print('go on... guss what:')

import random


while True :
    items = ['paper', 'scissor', 'rock']
    PC = random.choice(items)
    human_index = input()
    print(PC)

    
    if PC == 'paper' and human_index == 'scissor':
        print('* i will win this time')
    elif PC == 'paper' and human_index == 'rock':
        print('*pc wins')
    elif PC == 'rock' and human_index == 'scissor':
        print('*pc wins')
    elif PC == 'rock' and human_index == 'paper':
        print('*i will win this time')
    elif PC == 'scissor' and human_index == 'paper':
        print('*pc wins')
    elif PC == 'scissor' and human_index == 'rock':
        print('*i will win this time')
    elif PC == human_index:
        print('ops...lets try again')
    elif human_index == 'finish':
        break 
    elif human_index != 'paper'or 'scissor' or 'rock' or 'finish':
        print('what the hell r u talking about?? play rihgt!')


print('goodbye'+ ' ' + username)
        