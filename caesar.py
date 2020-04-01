import quizgen  
import random
import os


# this file contains some plaintext phrases one per line
f=open("data/plaintext_phrases.txt","r")

# this is where our output questions will go
q=quizgen.quizgen('bbquestions/output_caesardecode.txt')

q.fib_setup("\"PARAMETER\" is encoded with a Caesar cipher. What letter shift was used (answer should be a number between 1 and 25)?")

ctr=0

# for each line in the plaintext file
for p in f :
    # first make it uppercase
    p=p.rstrip().upper()
    
    # then calculate a Caesar encoded version with each shift from 1 to 25 
    for i in range(1 , 25): 
        translated=''
        for symbol in p:
            if symbol.isalpha():
                n=ord(symbol)
                n+=i
                if n>ord('Z'):
                    n-=26
                if n<ord('A'):
                    n+=26
                translated+=chr(n)
            else:
                translated+=symbol
        
        # the answer is i , but it could also be 26-i
        # that is it could be 3 or 23 (that is, let's give the students
        # marks whichever way they count in the alphabet)

        # to allow multiple answers, just separate them with a tab
        ans=str(i)+'\t'+str(26-i)
        q.fib_instance(translated,ans)
