import sys
# program functions

# Function to display a welcome message
def sayHello():
  print("\n\n\n")
  print('Welcome to the customer service of "XCar Company for car rental"\n'+
      '==================================================================\n')

# Function to exit the program
def exitProgram():
  print("\n=================================================================="+
      "\nThank you for using our services, good bye.\n")
  sys.exit()

# Function to get the car rental duration from the user
def getDuration():
  while True:
    try:
      durationInput=input("Please enter the car rental period in days: ")
      durationInput= int(durationInput)
      if(durationInput>0):
        return durationInput
    except:
      print("------ ❌ '" + durationInput + "' is an invalid value! ------\n")
      command=input("type 0 to exit, or any to reEnter: ")
      if command=="0":
        exitProgram()
      print("--------------- reEnter ----------------\n")

# Function to calculate and print the total cost based on the rental duration
def printCost(days):
  months= days//30
  rest=days%30
  costPerDay=1000
  costPerMonth = [0, 30000, 25000, 20000]
  index = -1
  if(months>=3):
    index=3
  else:
    index = months
  totalCost= costPerMonth[index] * months + costPerDay * rest
  print("Total Cost: " + str(totalCost))

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
  sayHello()  # Display the welcome message
  duration= getDuration()  # Get the rental duration from the user
  printCost(duration)  # Calculate and print the total cost based on the rental duration
  runAgain = again()  # Ask the user if they want to run the program again
exitProgram()  # Exit the program