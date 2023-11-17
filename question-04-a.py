#==========================================
# import libs
import sys

#==========================================
# Classes
class Employee:
  ssn=0
  name=''
  email=''
  mobile=''
  sales=[]

  totalSalesPrice=0
  salary=700000


  def __init__(self, ssn, name, email, mobile):
    self.ssn = ssn
    self.name= name
    self.email= email
    self.mobile= mobile
    self.sales=[]

  def addSale(self, sale):
    self.sales.append(sale)
    self.calcTotalSalesPrice()
    self.calcSalary()

  def calcTotalSalesPrice(self):
    tempPrice=0
    for sale in self.sales:
      tempPrice += sale.price
    self.totalSalesPrice = tempPrice

  def calcSalary(self):
    self.salary= 700000 + 0.09 * self.totalSalesPrice

  def toString(self):
    info= "SSN:       " +str(self.ssn)     +"\n"
    info+="Full Name: " +self.name    +"\n"
    info+="Email:     " +self.email   +"\n"
    info+="mobile:    " +self.mobile  +"\n\n"

    if(len(self.sales)==0):
      info+=" no sales yet ..\n"
      return info
    info+="Sales Table\n"
    info+= cellW("num",5) +" | " + cellW("Sale ID",10)+ " | " + cellW("Product Name",25)+ " | " +cellW("Quantity",10)+ " | " + cellW("Unit Price",10)+ " | " + cellW("Price",10)+ "\n"
    info+="-----------------------------------------------------------------------------------\n"

    count=0
    for sale in self.sales:
      count+=1
      info+= cellW(str(count),5)+ " | "+  sale.toTableRow() + "\n"
    info+="-----------------------------------------------------------------------------------\n"
    info+= cellW("Sum",5) +" | " + cellW("",10)+ " | " + cellW("",25)+ " | " +cellW("",10)+ " | " + cellW("",10)+ " | " + cellW(str(self.totalSalesPrice),10)+ "\n"

    return info

class Sale:
  count=0
  saleID=0
  productName=''
  quantity=0
  unitPrice=0
  price=0
  def __init__(self, productName, quantity, unitPrice):
    Sale.count += 1
    self.saleID= Sale.count
    self.productName= productName
    self.quantity= quantity
    self.unitPrice= unitPrice
    self.price= self.quantity * self.unitPrice


  def toString(self):
    return "Sale ID: "+ str(self.saleID) +"\nProduct Name: "+ self.productName +"\nQuantity: "+ str(self.quantity) +"\nUnit Price: "+ str(self.unitPrice)
  
  def toTableRow(self):
    return cellW(str(self.saleID),10) +" | "+ cellW(self.productName,25) +" | "+ cellW(str(self.quantity),10) +" | "+ cellW(str(self.unitPrice),10)+ " | "+ cellW(str(self.quantity*self.unitPrice),10)

#==========================================
# basic functions

def sayHello():
  print('\nWelcome to Company X')
  print('==================================================================')

def exitProgram():
  print("\n=================================================================="+
      "\nGood bye.\n")
  sys.exit()

def cellW(s, l):
  return (s+(l-len(s))*" ")

def getNumber(lable):
  while True:
    try:
      numInput=input(lable)
      numInput= int(numInput)
      if(numInput>0):
        return numInput
    except:
      print("  ❌ '" + numInput + "' is invalid value! \n")
      command=input("type 0 to exit, or any to reEnter: ")
      if command=="0":
        exitProgram()
      print("--------------- reEnter ----------------\n")

#==========================================
# program functions
#------------------------------------------
# for question 1-a

def selectEmployeeFromUser(data): 
  while True:
    ssNum = input("  Please write the employee's 'Social Security Number': ")
    if ssNum not in data:
      print("  ❌ No employee has this SSN: '" + ssNum + "' ! \n")
      print("---------------------------")
      print("1.   Rewrite 'Social Security Number'.")
      print("2.   Back to Home Page.")
      print("any. Exit.")
      print("---------------------------")
      command=input("Please type your choice number: ")
      if(command=="1"):
        continue
      elif(command=="2"):
        return None
      else:
        exitProgram()
    else:
      return data[str(ssNum)]
      # return ssNum

def employeeSalary(data):
  employee= selectEmployeeFromUser(data)
  if(employee!=None):
    print("\nEmployee Salary of '"+ employee.name +"' : "+ str(employee.salary))


#------------------------------------------
# for question 1-b

def maxSalary(emplist):
  max=0
  count=0
  i=-1
  for emp in emplist:
    if(max<=emp.salary):
      max=emp.salary
      i=count
    count+=1

  return emplist[i]

def sortEmployeeBySalary(data):
  sortedList=[]
  employeelist=[]
  for key in data:
    employee=data[key]
    employeelist.append(employee)

  for x in range(len(employeelist)):
    top=maxSalary(employeelist)
    sortedList.append(top)
    employeelist.remove(top)
  
  return sortedList

def printEmployeesSortedBySalary(data):
  sortedList=sortEmployeeBySalary(data)
  count=0
  info="\nEmployees Sorted By Salary.\n"
  info+= cellW("num",3) +" | " + cellW("SSN",6)+" | " + cellW("Name",17)+" | " + cellW("Email",25)+" | " + cellW("Mobile",13)+ " | " + cellW("Salary",20)+ "\n"
  info+="------------------------------------------------------------------------------------------\n"
  for employee in sortedList:
    count+=1
    info+= cellW(str(count),3) +" | " + cellW(str(employee.ssn),6)+" | " + cellW(employee.name,17)+" | " + cellW(employee.email,25)+" | " + cellW(employee.mobile,13)+ " | " + cellW(str(employee.salary),20)+ "\n"

  print(info)

#------------------------------------------
# for question 1-c

def bestSellerEmployee(data):
  max=0
  bestSellerEmp=None

  for key in data:
    employee=data[key]
    if(max<= employee.totalSalesPrice):
      max= employee.totalSalesPrice
      bestSellerEmp=employee
  
  print("\nBest Seller Employee: \n"+ bestSellerEmp.toString())

#------------------------------------------
# for question 1-d
def printBestSellingProduct(data):
  products={}
  maxQuantity=0
  bestSellingProduct=''


  for key in data:
    employee=data[key]
    if(len(employee.sales)!=0):
      for sale in employee.sales:
        if sale.productName in products:
          products[sale.productName]+=sale.quantity
        else:
          products[sale.productName]=sale.quantity
  
  # print(products)
  for key in products:
    if(maxQuantity<=products[key]):
      maxQuantity= products[key]
      bestSellingProduct=key

  print("\nBest-Selling Product: "+bestSellingProduct)
  print("Quantity: "+ str(maxQuantity))

#------------------------------------------
# for question 1-e

def writeEmployeeToFile(data,filePath):
  employeeFile=''

  try:
    employeeFile=open(filePath,"w")
  except:
    print(" ❌ '" + filePath + "' is not exist! \n")
    exitProgram()

  info="socialSecurityNumber,Name,Email,mobile\n"
  for key in data:
    employee=data[key] 
    info+=str(employee.ssn)+","+employee.name+","+ employee.email+ ","+employee.mobile+"\n"

  employeeFile.write(info)
  employeeFile.close()

def writeSalesToFile(data,filePath):
  salesFile=''
  
  try:
    salesFile=open(filePath,"w")
  except:
    print(" ❌ '" + filePath + "' is not exist!\n")
    exitProgram()

  count=0
  info="saleID,socialSecurityNumber,productName,quantity,unitPrice\n"
  for key in data:
    employee=data[key] 
    if(len(employee.sales)==0):
      continue

    for sale in employee.sales:
      count+=1
      info+=str(count)+","+str(employee.ssn)+","+ sale.productName+ ","+str(sale.quantity)+","+str(sale.unitPrice)+"\n"

  salesFile.write(info)
  salesFile.close()

def saveData(data):
  writeEmployeeToFile(data,"data/Employees.txt")
  writeSalesToFile(data,"data/Sales.txt")
  print("\nThe data has been saved successfully.")
#------------------------------------------
# for question 1-f

def getEmployeeFromFile(data,filePath):
  employeeFile=''

  try:
    employeeFile=open(filePath)
  except:
    print(" ❌ '" + filePath + "' is not exist! \n")
    exitProgram()

  for line in employeeFile:
    if not line.startswith("social"):
      info=line.replace("\n","")
      info=info.split(",")
      ssNum=info.pop(0)
      data[str(ssNum)] = Employee(ssNum, info[0], info[1], info[2])

def getSalesFromFile(data,filePath):
  salesFile=''
  
  try:
    salesFile=open(filePath)
  except:
    print(" ❌ '" + filePath + "' is not exist!\n")
    exitProgram()

  for line in salesFile:
    if not line.startswith("saleID"):
      info=line.replace("\n","")
      info=info.split(",")
      ssNum=info[1]
      sale=Sale(str(info[2]), int(info[3]), int(info[4]))
      data[str(ssNum)].addSale(sale)

#==========================================
# program commands

def mainMenu(data):
  print("-------------------------------------")
  print("------------- Home Page -------------")
  print("-------------------------------------")
  print("1.   Employee salary.")
  print("2.   print Employees Sorted By Salary.")
  print("3.   Best Seller Employee.")
  print("4.   Best Selling Product.")
  print("5.   Save and Exit.")
  print("any. Exit.")
  print("---------------------------")
  command=input("Please type your choice number: ")
  if(command=="1"):
    employeeSalary(data)

  elif(command=="2"):
    printEmployeesSortedBySalary(data)

  elif(command=="3"):
    bestSellerEmployee(data)

  elif(command=="4"):
    printBestSellingProduct(data)

  elif(command=="5"):
    saveData(data)
    exitProgram()

  else:
    exitProgram()

# dataSet=testData()
dataSet={}  # empty data
getEmployeeFromFile(dataSet,"data/Employees.txt")
getSalesFromFile(dataSet,"data/Sales.txt")

while(True):
  sayHello()
  mainMenu(dataSet)