import mysql.connector
import datetime
mydb = mysql.connector.connect(user='root', password='12345',
host='localhost',database='air')
mycursor=mydb.cursor()

def registercust():
 L=[]
name=input("enter name:")
L.append(name)
addr=input("enter address:")
L.append(addr)
jr_date=input("enter date of journey:")
L.append(jr_date)
source=input("enter source:")
L.append(source)
destination=input("enter destination:")
L.append(destination)
cust=(L)
sql="insert into pdata(custname,addr,jrdate,source,destination)values(%s,%s,%s,%s,%s)"
mycursor.execute(sql,cust)
mydb.commit()
print(“insertion completed”)
runAgn=input("\ndo you want to insert more details? y/n")
    while runAgn.lower()=='y':
        registercust()
    
def classtypeview():
print("Do you want to see class type available : Enter 1 for yes :")
ch=int(input("enter your choice:"))
if ch==1:
sql="select * from classtype"
mycursor.execute(sql)
rows=mycursor.fetchall()
for x in rows:
print(x)
def ticketprice():
print ("We have the following rooms for you:-")
print ("1.  type First class---->rs 6000 PN\-")
print ("2.  type Business class---->rs 4000 PN\-")
print ("3.  type Economy class---->rs 2000 PN\-")
        x=int(input("Enter Your Choice Please->"))
        n=int(input("No of passenger:"))
if(x==1):
print ("you have opted First class")
            s=6000*n
elif (x==2):
print ("you have opted Business class")
            s=4000*n
elif (x==3):
print ("you have opted Economy class")
           s=2000*n
else:
print ("please choose a class type")
print ("your room rent is =",s,"\n")
def menuview():
print("Do yoy want to see menu available : Enter 1 for yes :")
ch=int(input("enter your choice:"))
if ch==1:
sql="select * from food"
mycursor.execute(sql)
rows=mycursor.fetchall()
for x in rows:
print(x)

def orderitem():
global s
print("Do you want to see menu available : Enter 1 for yes :")
ch=int(input("enter your choice:"))
if ch==1:
sql="select * from food"
mycursor.execute(sql)
rows=mycursor.fetchall()
for x in rows:
print(x)

print("do you want to purchase from above list:enter your choice:")
d=int(input("enter your choice:"))
if(d==1):
print("you have ordered tea")
          a=int(input("enter quantity"))
          s=10*a
print("your amount for tea is :",s,"\n")
elif (d==2):
        print("you have ordered coffee")
        a=int(input("enter quantity"))
        s=10*a
print("your amount for coffee is :",s,"\n")
elif(d==3):
print("you have ordered colddrink")
       	 a=int(input("enter quantity"))
s=20*a
print("your amount for colddrink is :",s,"\n")
elif(d==4):
print("you have ordered samosa")
          a=int(input("enter quantity"))
 s=10*a
print("your amount for samosa is :",s,"\n")
elif(d==5):
print("you have ordered sandwich")
          a=int(input("enter quantity"))
          s=50*a
print("your amount fopr sandwich is :",s,"\n")
elif(d==6):
print("you have ordered dhokla")
  	 a=int(input("enter quantity"))
  	 s=30*a
print("your amount for dhokla is :",s,"\n")
elif(d==7):
print("you have ordered kachori")
  	 a=int(input("enter quantity"))
   	s=10*a
print("your amount for kachori is :",s,"\n")
elif(d==8):
print("you have ordered milk")
 a=int(input("enter quantity"))
  	 s=20*a
print("your amount for kachori is :",s,"\n")
elif(d==9):
print("you have ordered noodles")
          a=int(input("enter quantity"))
          s=50*a
print("your amount for noodles is :",s,"\n")
elif(d==10):
print("you have ordered pasta")
          a=int(input("enter quantity"))
          s=50*a
print("your amount for pasta is :",s,"\n")
else:
Print("please enter your choice from the menu")
def lugagebill():
global z
print("Do yoy want to see rate for lugage  : Enter 1 for yes :")
ch=int(input("enter your choice:"))
if ch==1:
sql="select * from lugage"
mycursor.execute(sql)
rows=mycursor.fetchall()
for x in rows:
print(x)
    y=int(input("Enter Your weight of extra lugage->"))
    z=y*1000
    print("your laundarybill:",z,"\n")
    return z
def lb():
print(z)
def res():
print(s)
def ticketamount():
    a=input("enter customer name:")
print("customer name :",a,"\n")
print("lugage bill:")
print(lb)
print("food bill:")
print(“total amount”)

def Menuset():
print(“AIR TICKET RESERVATION”)
print("enter 1: To enter customer data")
print("enter 2 : To view class")
print("enter 3 : for  ticketamount")
print("enter 4 : for viewing food menu")
print("enter 5 : for food bill")
print("enter 6 :for lugage bill")
print("enter 7 : for complete amount")
print("enter 8 : for exit")
userinput=int(input("enter your choice"))
if(userinput==1):
registercust()
elif(userinput==2):
classtypeview()
elif(userinput==3):
ticketprice()
elif(userinput==4):
menuview()
elif(userinput==5):
orderitem()
elif(userinput==6):
lugagebill()
elif(userinput==7):
ticketamount()
elif(userinput==8):
quit()
else:
print("enter correct choice")
Menuset()
