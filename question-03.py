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
# for question 1

def getVaildSSN2Registration(data):
  while True:
    print("Please write the new employee's info:\n")
    ssNum = getNumber("  Social Security Number (SSN): ")
    if ssNum in data:
      print("  ❌ '" + ssNum + "' is already exist! \n")
      print("---------------------------")
      print("1.   Rewrite another 'Social Security Number'.")
      print("2.   Back to Home Page.")
      print("any. Exit.")
      print("---------------------------")
      command=input("Please type your choice number: ")
      if(command=="1"):
        continue
      elif(command=="2"):
        return -1
      else:
        exitProgram()
    else:
      return ssNum

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

def getNewEmployeeFromUser(data):
  print("==================================================================\n")
  print("* Register a new employee")
  ssNum = getVaildSSN2Registration(data)
  if (ssNum ==-1):
    return 
  
  name = input("  Full Name:      ")
  email = input("  Email:          ")
  mobile = input("  Mobile Number:  ")

  # info={"Name":name,"Email":email,"mobile":mobile}
  # data[str(ssNum)] = info
  data[str(ssNum)] = Employee(ssNum, name, email, mobile)

def getNewSaleFromUser(data):
  print("==================================================================\n")
  print("* Register a sale ")

  selectedEmployee = selectEmployeeFromUser(data)
  if (selectedEmployee is None):
    return 

  while True:
    productName = input("Please write the 'Product Name': ")
    quantity = getNumber("Please write the 'Quantity': ")
    unitPrice = getNumber("Please write the 'Unit Price': ")
    sale=Sale(productName, quantity, unitPrice)
    selectedEmployee.addSale(sale)
    print("---------------------------")
    command = input("1. add one more sale,  any. enough : ")
    if(command!='1'):
      print(selectedEmployee.toString())
      break

#------------------------------------------
# for question 2

def printEmployeesTotalSales(data):
  count=0
  info="\nEmployees total sales\n"
  info+= cellW("num",5) +" | " + cellW("Employee",20)+ " | " + cellW("Total Sales Price",20)+ "\n"
  info+="--------------------------------------------------------\n"
  for key in data:
    employee=data[key]
    count+=1
    info+= cellW(str(count),5) +" | " + cellW(employee.name,20)+ " | " + cellW(str(employee.totalSalesPrice),15)+ "\n"

  print(info)

#------------------------------------------
# for question 3

def maxTotalSales(emplist):
  max=0
  count=0
  i=-1
  for emp in emplist:
    if(max<=emp.totalSalesPrice):
      max=emp.totalSalesPrice
      i=count
    count+=1

  return emplist[i]

def sortEmployeeByTotalSales(data):
  sortedList=[]
  employeelist=[]
  for key in data:
    employee=data[key]
    employeelist.append(employee)

  for x in range(len(employeelist)):
    top=maxTotalSales(employeelist)
    sortedList.append(top)
    employeelist.remove(top)
  
  return sortedList

def printTop3EmployeesBestSaler(data):
  best3=sortEmployeeByTotalSales(data)[0:3]
  count=0
  info="\nTop 3 Employees Best Saler.\n"
  info+= cellW("num",5) +" | " + cellW("Employee",20)+ " | " + cellW("Total Sales Price",20)+ "\n"
  info+="--------------------------------------------------------\n"
  for employee in best3:
    count+=1
    info+= cellW(str(count),5) +" | " + cellW(employee.name,20)+ " | " + cellW(str(employee.totalSalesPrice),20)+ "\n"

  print(info)

#------------------------------------------
# for question 4

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
  info+= cellW("num",5) +" | " + cellW("SSN",6)+" | " + cellW("Name",20)+" | " + cellW("Email",20)+" | " + cellW("Mobile",13)+ " | " + cellW("Salary",20)+ "\n"
  info+="------------------------------------------------------------------------------------------\n"
  for employee in sortedList:
    count+=1
    info+= cellW(str(count),5) +" | " + cellW(str(employee.ssn),6)+" | " + cellW(employee.name,20)+" | " + cellW(employee.email,20)+" | " + cellW(employee.mobile,13)+ " | " + cellW(str(employee.salary),20)+ "\n"

  print(info)

#------------------------------------------
# for question 5
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



  #       if(max <= sale.quantity):
  #         max = sale.quantity
  #         bestSellingProduct=sale.productName
  # print("sd")

#==========================================
# program commands

def mainMenu(data):
  print("-------------------------------------")
  print("------------- Home Page -------------")
  print("-------------------------------------")
  print("1.   Register a new employee.")
  print("2.   Register a sale.")
  print("3.   Print employees total sales.")
  print("4.   print Top 3 Employees Best Sales.")
  print("5.   print Employees Sorted By Salary.")
  print("6.   print Best-Selling Product.")
  print("any. Exit.")
  print("---------------------------")
  command=input("Please type your choice number: ")
  if(command=="1"):
    getNewEmployeeFromUser(data)
  elif(command=="2"):
    getNewSaleFromUser(data)
  elif(command=="3"):
    printEmployeesTotalSales(data)
  elif(command=="4"):
    printTop3EmployeesBestSaler(data)
  elif(command=="5"):
    printEmployeesSortedBySalary(data)
  elif(command=="6"):
    printBestSellingProduct(data)
  else:
    # for key in data:
    #   print(data[key].toString())
    exitProgram()

def testData():
  e1=Employee(1001,"employee1", "employee1@abc.com","099991")
  e2=Employee(1002,"employee2", "employee2@abc.com","099992")
  e3=Employee(1003,"employee3", "employee3@abc.com","099993")
  e4=Employee(1004,"employee4", "employee4@abc.com","099994")
  s1=Sale("aaa",4,400000)
  s2=Sale("bbb",3,900000)
  s3=Sale("ccc",6,600000)
  s4=Sale("ttt",4,100000)
  s5=Sale("eee",3,200000)
  s6=Sale("bbb",4,800000)
  e1.addSale(s1)
  e2.addSale(s2)
  e3.addSale(s3)
  e4.addSale(s4)
  e1.addSale(s5)
  e2.addSale(s6)
  e3.addSale(s4)

  return  {
            str(e1.ssn):e1,
            str(e2.ssn):e2,
            str(e3.ssn):e3,
            str(e4.ssn):e4,
          }

dataSet=testData()
# dataSet={}  # empty data

while(True):
  sayHello()
  mainMenu(dataSet)
