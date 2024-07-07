#libraries
import random
import array

#variables

#the words are in Portuguese!
word = ['dicionário', 'intrínseco', 'prescindir', 'presunçoso', 'diligência', 'corroborar', 'intempérie',
            'perspicaz', 'recíproco', 'concessão', 'impressão', 'escrúpulo', 'inerente', 'respeito', 'peculiar',
            'denegrir', 'sagaz', 'âmago', 'negro', 'termo', 'êxito', 'mexer', 'nobre', 'senso', 'afeto', 'algoz',
            'imprescindível', 'condescendente', 'idiossincrasia', 'característica', 'concupiscência', 'extraordinário']

word_cho = random.choice(word) #vector word random words
vector_letter = [] #letter
vector_cho = [] #guessing
vector_att = [] #attempted lyrics
attempts = 6 #how many attempts
let_att = 1 #how many were tried

##discovering how many letters there are, recording in the vectors
count = 0
for x in word_cho:
    count += 1
    vector_letter.insert(count, x)
    vector_cho.insert(count, ' _ ')

#starting game
letters = str
while vector_letter != vector_cho:
    #if you make a mistake 6 times
    if attempts == 0:
        print("Unfortunately you lost!! the word was:", word_cho)
        break
       
    print("You got ", attempts, " tries\n")
    #printing the letters already tried
    for x in vector_att:
        print(x, end="")
    print("\n")
       
    #printing the guessed letters
    for x in vector_cho:
        print(x, end="")
    #trying to guess
    letters = str(input("\n\nEnter a letter or word: \n"))
    print("\n")
   
    #if you get it right typing the words
    if letters == word_cho:
        #skipping several lines
        for x in range(10):
            print("\n")
        print("Congratulations!! you won")
        break
   
    has_lyric = 0
    countara = 0
    #if you have the lyrics
    for x in vector_letter:
        if letters == x:
            vector_cho.pop(countara)
            vector_cho.insert(countara, letters)
            has_lyric = 1
        countara += 1
        
    #adding typed letter in vector
    vector_att.insert(let_att, letters)
    let_att += 1
   
    #if you don't have the lyrics
    if has_lyric == 0:
        attempts -= 1
     
           
    #skipping several lines
    for x in range(10):
        print("\n")
       
#if you get the words right 
else:
    #skipping several lines
    for x in range(10):
        print("\n")
    print("The word was", word_cho)
    print("Congratulations!! you won")
