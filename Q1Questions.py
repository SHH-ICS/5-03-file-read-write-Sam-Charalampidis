# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
question = input("Input question: ")
a = input("Input answer a: ")
b = input("Input answer b: ")
c = input("Input answer c: ")
d = input("Input answer d: ")
e = input("Input correct answers letter: ")
filehandle = open("questions.txt","w")
filehandle.write(question+"\n"+a+"\n"+b+"\n"+c+"\n"+d+"\n"+e)
filehandle.close()