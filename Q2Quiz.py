# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
filehandle = open("questions.txt","r")
question = filehandle.readline()
a = filehandle.readline()
b = filehandle.readline()
c = filehandle.readline()
d = filehandle.readline()
e = filehandle.readline()
filehandle.close
print(question)
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)
guess = input("Which letter? ")
if guess != str(e):
    print("ur loss sucka")
elif guess == str(e):
    print("u win sucka")