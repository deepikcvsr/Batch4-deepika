###DAY-8###


'''
#EG:1
n=int(input("enter the number"))
d=dict()
for x in range(1,n+1):
    d[x] =x*x
print(d)


#EG:2
s1 = "Hello how are you"
s2 = "hello how is"
def uncombined words(s1,s2)
    s1=s1.split()
    s2=s2.split()
    x=[]
    for i in s1:
        if i not in s2:
            x.append(i)
    for i in s2:
         if i not in s1:
             x.append(i)


#EG:3
def profile(name,age,place):
    txt ="My name is{}.I am{} years old{}.I am from{}."
    print(txt.format(name,age,place))
    profile("deepika",21,"kdp")
             

#EG:4
#Functions with return statement

#! return
1.) A variable declared inside the function can be accessed outside the functions
#using return
2.)return does not print anything
3.)We cannot write any code below return statement


def f1():
    z=8
f1()
print(z)#error --> used outside the function

#EG:5
def f1(a,b):
    c = a*b
    return c
##print(f1(6,8))
obj = f1(6,8)
obj1 = f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

#Problem:1
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "Palindrome")
    else:
        print("not palindrome")
a = int(input("Enter a value:"))
palindrome(a)

##Based on the declaration of parameter and args
#functions are ddivided into 6 categories

#positional
#keyword args
#default args
#variable length args
#keyword variable length args

#*Positional args
#The position of paramater have to be same as position as arguments
#!EG:1

def profile(name,phone,mark):
    txt ="My name is {}.My phone number is{}.I got{] marks."
    print(txt.format(name,phone,mark))

profile(987877676,"deepu",98)#unexcepted output

#*Keyword args
#!EG:1
#To overcome the disadvantage of position args,we use keyword args
#It is the process of initializing the paramter with the args while calling the function
def profile(name,phone,mark):
    txt = "My name is {].My phone number is{}.I got{] marks."
    print(txt.format(name,phone,marks)
          
profile(name="deepu",mark=98,phone=12334567890

#Exception of keyword args function
def profile(name,phone,mark):
     txt = "My name is {].My phone number is{}.I got{] marks."
     print(txt.format(name,phone,mark))

#profile(name="sid",1234455667,mark=98) #error--->poositional args follow keyword arg
#profile(123567890,name="deepu",mark=98)# error--->name has multiple values
profile("deepu",mark=98,phone=123456789)

#!EG:1
#*Default args
The method of assigning the argument  to the parameter while declaring the
#function
def profile (name,phone,place="Kadapa"):
    txt = "My name is{].My phone number is{}.I am from{}."
    print(txt.format(name,phone,place))

profile("deepu",1223434545,"Guntur")



#!EG:2
def profile(name,phone,place="Kadapa"):
    if place ==  "kadapa" or place =="kadapa" or place =="Kadapa":
       txt = "My name is{}.My phone number is{}.I am from{}."
       print(txt.format(name,phone,place))
    else:
       print("you are not elgible to signup")
profile("sid",8990938890)



#!Exception
def profile(name,place="KADAPA",phone): #error--->coz default args should not follow
#positional
if place == "kadapa" or place =="kadapa" or place=="kadapa":
    txt = "my name is{}.my phone number is{}.I am from{}."


'''
'''
#!variable length params
#EG:1
#To pass more than 1 arg to a parameter means we use variable length argumendef profile(*name):
#To convert normal parameter to variable length param,add* to their prefix of parameter

name = "deepika","name2","name3"
def profile(*name):
    for val in name:
         print("my name is",val)
profile("deepika",'name2','name3')


#!EG:2
def profile(*name,age):
    for val in name:
        print("my name is",val,"may age is",age)
profile("sid",'name2','name3',28)#error --->age has no args


def profile(age,*name):
    for val in name:
        print("My name is",val,"may age is", age)
profile(28,"deepika",'name2','name3')


#*Keyword variable length args
#kwargs--->which is used to provide the args in the form of key value pair
#!EG:1
def price(price_list):
    print(price_list)

price(shirt=1000,iphone=80000)


d1 ={"a":100,"b":200,"c":300}
d1=dict(a=100, b=200, c=300)
print(d1)



n=int(input("enter the number:"))
d1=dict()
for  val in range(1,n+1):
    d1[val] =val**2
print(d1)


def dict1(n):
    d1=dict()
    for  val in range(1,n+1):
         d1[val] =val**2
    print(d1)
dict1(6)


#----->object oriented programming
#The paradigms of objects oriented programming are


#class
#objects
#inheritance
#polymorphism
#abstraction
#encapsulation



#class is a blue print of an object
l1 =[1,2,3,4,5,6]

#! EG:1
class c1:
    name = "Deepika"
    print(name1)

#EG :2
class person:
    name ="deepika"

c = person() #c as object
#The process of creation of an object is called as instantiation
print(c.name)

#? EG:3
#creation of method
#When the function is created with a class is called as method

class person:
    def display(person):#It is a method
        print("Hello Welcome to classes")
p = person()
p.display()


#?EG:4
#!Method with parameter
class person:
    def display(person,name,age):
        print(name,age)
p = person()
p.display("deepika",20)

#?EG:5
class person1:
    fname = "deepika" #attribute or static variable
    lname ="M"
    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(Self.fname+" " +self.lname)
p = person1()
p.first_name()
p.full_name()
'''

#EG:6
#Constructors--->_int_()
#This is a special mthod which has the ability to execute itself without
#calling it manullay through tht process of instantiation

class profile:
    def d1(self):#constructor method
        print("hey")
p = profile() #execution of constructor throught this process












    
    
    









    
