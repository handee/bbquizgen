import math
import quizgen  
import random

# a data file with a bunch of passwords in it, one per line, 
# and an integer indicating the size of the character set the
# password has been drawn from 
f=open("data/pwsorted_char.txt","r")

# output file
q=quizgen.quizgen('entropy.txt')

#setup mcq
q.mc_setup("What is the entropy of the password \"PARAMETER\" ?")

for p in f :
    # grab a line at a time, split into pw and character set R
    p,R=p.rstrip().split(",")
    L=len(p)
    R=int(R)
    # calculate entropy based upon length and character set
    result = round(math.log(math.pow(R,L),2),2)
    answers=[]
    answers.append(str(result))
    # make up some random wrong answers
    answers.append(str(round(50*random.random()+30,2)))
    answers.append(str(round(50*random.random()+30,2)))
    q.mc_instance(p,answers)


