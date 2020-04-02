# QUIZGEN

this is a hacky set of python scripts to automatically create BlackBoard
questions

quizgen.py is the bit that does the "hard" work, containing functions for
creating fill-in-the-blank and multiple choice questions

welsh.py has examples of simple question creation

For the fill-in-the-blank (FIB) questions you set up a question template
containing the word PARAMETER, and then create instances of the question with
different parameters and answers. Example:

Template:

    quiz.fib_setup("What's the Welsh word for PARAMETER?")

Instances:

    quiz.fib_instance(Cheese,Caws)
    quiz.fib_instance(Carrot,Moron)


caesar.py is an example of a program which creates some fill-in-the-blank
questions involving Caesar ciphers of different shifts

For the multiple choice (MC) questions you set up a question template
containing the word PARAMETER, and then create instances of the question with
different parameters and a list of answers. In your list, the first answer has
to be the right one; the quizgen program will shuffle the answers after adding
the correct/incorrect markers required by BlackBoard. Example:

Template:

    quiz.mc_setup("What's the Welsh word for PARAMETER?")

Instances:

    quiz.mc_instance("Cheese",["Caws","Moron","Tatws"])
    quiz.mc_instance("Carrot",["Moron","Caws","Tatws"])


pwentropycalc.py is another example of a program which creates some multiple
choice questions based upon the calculation of entropy for passwords 
