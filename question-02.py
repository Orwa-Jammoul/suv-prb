import sys


# program functions

# Function to display the question
def sayHello():
  print("\n\n\n")
  print('Question 2:\n'+
      '==================================================================\n')

# Function to exit the program
def exitProgram():
  print("\n=================================================================="+
      "\nGood bye.\n")
  sys.exit()

# Function to get a number from the user
def getNumber():
  while True:
    try:
      numInput=input("Please enter a Number to check if it is Symmetrical or not: ")
      numInput= int(numInput)
      if(numInput>0):
        return numInput
    except:
      print("------ ❌ '" + numInput + "' is an invalid value! ------\n")
      command=input("type 0 to exit, or any to reEnter: ")
      if command=="0":
        exitProgram()
      print("--------------- reEnter ----------------\n")

# Function to check if a number is symmetrical or not
def checkSymmetry(stringNum):
  temp=''
  count=len(stringNum)-1
  while count>=0:
    temp=temp + stringNum[count]
    count-=1
  isSymmetry=(int(stringNum)-int(temp))==0
  if (isSymmetry):
    print("Yes, the number '"+ stringNum +"' is Symmetry. ✅")
  else:
    print("No, the number '"+ stringNum +"' is NOT Symmetry.❌")

# Function to ask the user if they want to run the program again
def again():
  print("-------------------------------\n")
  print("1.   try again.")
  print("any. exit.")
  command = input("please enter your choice: ")
  return command=="1"

# program commands
runAgain= True
while(runAgain):
  sayHello()  # Display the question
  Number= getNumber()  # Get a number from the user
  checkSymmetry(str(Number))  # Check if the number is symmetrical or not
  runAgain = again()  # Ask the user if they want to run the program again
exitProgram()  # Exit the program