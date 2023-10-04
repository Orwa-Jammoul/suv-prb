import sys

# program functions
def sayHello():
  print("\n\n\n")
  print('Question 2:\n'+
      '==================================================================\n')

def exitProgram():
  print("\n=================================================================="+
      "\nGood bye.\n")
  sys.exit()

def getEmployeeFromFile(data):
  employeeFile=''

  try:
    filePath="data/question-03-Employees.txt"
    employeeFile=open(filePath)
  except:
    print("------ ❌ '" + filePath + "' is not exist! ------\n")
    exitProgram()

  for line in employeeFile:
    if not line.startswith("social"):
      info=line.split(",")
      ssNum=info.pop(0)
      info={"Name":info[0],"Email":info[1],"mobile":info[2]}
      data[str(ssNum)]={"info":info,}

def getSalesFromFile(data):
  salesFile=''
  
  try:
    filePath="data/question-03-Sales.txt"
    salesFile=open(filePath)
  except:
    print("------ ❌ '" + filePath + "' is not exist! ------\n")
    exitProgram()

  for line in salesFile:
    if not line.startswith("saleID"):
      sale=line.split(",")
      ssNum=sale.pop(1)
      sale={"saleID":sale[0],"productName":sale[1],"quantity":sale[2],"unitPrice":sale[3]}
      if "sales" in data[str(ssNum)]:
        data[str(ssNum)]["sales"].append(sale)
      else:
        data[str(ssNum)]["sales"]=[]
        data[str(ssNum)]["sales"].append(sale)

def getDataFromFiles(data):
  getEmployeeFromFile(data)
  getSalesFromFile(data)

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

def again():
  print("-------------------------------\n")
  print("1.   try again.")
  print("any. exit.")
  command = input("please enter your choice: ")
  return command=="1"


# program commands
runAgain= True
while(runAgain):
  sayHello()
  dataSet={}
  getDataFromFiles(dataSet)
  print(dataSet)
    
  
  # Number= getNumber()
  # checkSymmetry(str(Number))

  runAgain=False
  # runAgain = again()



exitProgram()


# {
#   "10001":{
#             "info":{name,email,mobile},
#             "sales":[{saleID,productName,quantity,unitPrice},],
#           }
# }