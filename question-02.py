import sys

# program functions
def sayWelcome():
  print("\n\n\n")
  print('Question 2:\n'+
      '==================================================================\n')

def exitProgram():
  print("\n=================================================================="+
      "\nGood bye.\n")
  sys.exit()


def getNumber():
  while True:
    try:
      numInput=input("Please enter a Number to check if it is Symmetrical or not: ")
      numInput= int(numInput)
      if(numInput>0):
        return numInput
      
    except:
      print("------ ❌ '" + numInput + "' is invalid value! ------\n")
      command=input("type 0 to exit, or any to reEnter: ")
      if command=="0":
        exitProgram()
      print("--------------- reEnter ----------------\n")

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
    print("No, the number '"+ stringNum +"' is NOT Symmetry.❎")


def again():
  print("-------------------------------\n")
  print("1.   try again.")
  print("any. exit.")
  command = input("please enter your choice: ")
  return command=="1"


# program commands

runAgain= True
while(runAgain):
  sayWelcome()
  Number= getNumber()
  checkSymmetry(str(Number))
  runAgain = again()

exitProgram()

