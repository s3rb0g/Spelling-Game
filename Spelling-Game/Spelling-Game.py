import random
Sample = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
word = ''
correct = 11
wrong = 0

print('HELLO, WELCOME TO THE WOLRD SPELLING GAME.')
print('\nSPELL AS MUCH NUMBER AS YOU CAN TO GET MARK')
print('\n--------------------------------------------\n')

for x in range(11):
    ranNum = Sample.pop(random.randrange(len(Sample)))
    life = 3
    if ranNum == '0':
        word = "zero"
    elif ranNum == '1':
        word = "one"
    elif ranNum == '2':
        word = "two"
    elif ranNum == '3':
        word = "three"
    elif ranNum == '4':
        word = "four"
    elif ranNum == '5':
        word = "five"
    elif ranNum == '6':
        word = "six"
    elif ranNum == '7':
        word = "seven"
    elif ranNum == '8':
        word = "eight"
    elif ranNum == '9':
        word = "nine"
    elif ranNum == '10':
        word = "ten"
    
    while True:
        ans = str(input("Spell " + ranNum + ": "))
        
        if str.lower(ans) == word:
            break
        else:
            life -= 1
            print("Incorrect spelling. ", life ," trials left\n")
            if life == 0:
                print("Sorry! Number of trials Exceeded")
                correct -= 1
                wrong += 1
                break
            else:
                continue
    
print("------------------")  
print("END OF GAME")
print("\nCORRECT SPELLING SCORE: ", correct)
print("\nWRONG SPELLING SCORE: ", wrong)
