import random

name = input('What is your name : ')

print('You have only 12 turns to guess right word :) ')
print('Good Luck ! :))',name)

# words = ['rainbow', 'computer', 'science', 'programming',  
#          'python', 'mathematics', 'player', 'condition',  
#          'reverse', 'water', 'board', 'geeks']

words =  list(open('Words.txt').read().split())

word = random.choice(words)
word1 = word
len1 = len(word)
position = []
guess = ''
while len1>0 :
    len1 = len1-1
    guess += '_ '

turns = 12

while turns > 0 :
    failed = 0
    print(guess)
    guess_temp = input('Guess Your character : ')
    if guess_temp in word:
        if guess_temp not in guess:
            
            for i in range(0,len(word)) :
                if word[i] == guess_temp:
                    position.append(i)
            
            temp = list(guess)
            for pose in position:
                if pose == 0:
                    temp[pose] = guess_temp
                else:
                    temp[pose*2] = guess_temp
            guess = ''.join(temp)
            guess_word = guess
            guess_word = guess_word.replace(' ','')
            if guess_word == word1 :
                print('')
                print('Congratularion !!! You did it :)))')
                print('')
                break
            position = []
        
        else:
            print(guess_temp,'Word has already occur')

    if guess_temp not in word:
        turns -= 1
        print('Wrong')

        print('You have ',+turns,' more guess')

        if turns==0:
            print('You Loose')
            print('The Word is',word)
            break