import quizgen  

# output file
q=quizgen.quizgen('welshfib.txt')

#setup fib 
q.fib_setup("What is the welsh word for \"PARAMETER\" ?")


q.fib_instance("Cheese","Caws")
q.fib_instance("Carrot","Moron")


# output file
q2=quizgen.quizgen('welshmcq.txt')

#setup mcq
q2.mc_setup("What is the welsh word for \"PARAMETER\" ?")


q2.mc_instance("Cheese",["Caws","Moron","Tatws"])
q2.mc_instance("Carrot",["Moron","Caws","Tatws"])



