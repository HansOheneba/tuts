def greet(fName, lName):
    return "Hello, " + fName + " " + lName + "!"

inputFName = input("Enter your first name: ")
inputLName = input("Enter your last name: ")
message = greet(inputFName, inputLName)
print(message)

file = open("output.txt", "w")
file.write(message)