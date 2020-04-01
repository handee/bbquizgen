import sys
import random 

class quizgen:

    def __init__(self, output_filename):
        self.ofn = output_filename
        self.current_question= "" 
        self.of=open(self.ofn,"w+")
   
    def __del__(self):
        self.of.close()

 
    ###  Fill in blank FIB questions

        # note: short answer questions in BB are not automatically 
        # marked so you need to use FIB questions to get string comparison.
        # so you to set up a question like:

        # "What is the Welsh word for Cheese?" with the answer Caws.
        # the question setup would be 
        
        # fib_setup("What is the Welsh word for PARAMETER?")

        # and the instance function would be called as 
       
        # fib_instance("Cheese","Caws") 
      
        # thus the question doesn't really have a blank to fill in at all. 

    ###  fib_setup creates the question and the output file
    ###  fib_instance appends an instance of a question to the output file

    def fib_setup(self, question):
        # fill in blank question 
        # each question has a parameter represented by the word "PARAMETER"
        # 
        # the blank is as far as i can tell at this stage presentational 
        # and you can represent that how you like. If question doesn't have the
        # word PARAMETER in it, the parameter passed by question 
        # just gets appended at the end.
        # curly braces have meaning from here on in so if they
        # exist in the question we throw an error
        if ( '{' in question ) or ('}' in question ):
        # there are curly braces there already which will mess stuff up
            print("There are curly braces already, whoops\n")
            sys.exit("alreadybracketswhoops")
        if ('PARAMETER' in question ) :
            question=question.replace('PARAMETER','{}')
        else :
            question.append('{}')
        self.current_question=question


    def fib_instance(self, parameter, answer):
        # parameter is the string which gets embedded in the question
        # answer is the response the student has to type in. 
        qstring=self.current_question.format(parameter)
        ostring="FIB\t"+qstring+"\t"+answer+'\n';
        self.of.write(ostring)



    def mc_setup(self, question):
        # multiple choice question 
        # each question has a parameter represented by the word "PARAMETER"
        # 
        if ( '{' in question ) or ('}' in question ):
        # there are curly braces there already which will bollox stuff up
            print("There are curly braces already, whoops\n")
            sys.exit("alreadybracketswhoops")
        if ('PARAMETER' in question ) :
            question=question.replace('PARAMETER','{}')
        else :
            question.append('{}')
        self.current_question=question


    def mc_instance(self, parameter, answers):
        # parameter is the string which gets embedded in the question

        # for this type of question (multiple choice) pass in an array of 
        # answers with the first (0th) item being the right answer and the
        # rest all being wrong

        # this will format the answers for BB then shuffle the answers for you 

        qstring=self.current_question.format(parameter)
        ostring="MC\t"+qstring+"\t"
        # answer array needs "correct" and "incorrect" adding:
        newanswers=[] 
        newanswers.append(answers[0]+'\t'+"correct")
        for i in range(1,len(answers)):
             newanswers.append(answers[i]+'\t'+"incorrect")
 
 
        random.shuffle(newanswers)  
    
        for newanswer in newanswers:
            ostring+=newanswer+'\t'
        ostring+="\n"
        self.of.write(ostring)


