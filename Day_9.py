###Day-9###

'''
#Write a code to print the 8th fibonaci number
#0,1,1,2,3,5,8

num = 5
n1 =0
n2 =1
for val in range(5):
     ans =n1+n2
     print(ans)
     n1 = n2
     n2 =ans
print(ans)


#Find thr uncommon words from strings
s1 ="Hello how are you"
s2 = "Hello how is"

s1=s1.split(" ")
s2=s2.split(" ")
for i in s1:
     if i  not in s2:
         print(i)
for i in s2:
     if i not in s1:
         print(i)


#Constructors:
#EG :2

#unparametarised constructor:
class profile:
    def __init__ (self):
        print("hello world")
obj =profile()
obj.__init__()

#EG:3
#Parameterised Constructor:
class profile:
    def __init__(self,id,name,age):
        print(id,name,age)
        
obj = profile(1,"deepu",21)

#EG:4
class c1:
    email = "deepikadeepu@gmail.com"
    def m1(self):
       name ="deepika"
       place = "kadapa"
       print(name,place)
       print(self.email)
    
object = c1()
object.m1()

#EG:5
class c1:
    def m1(self):
        name ="deepu"
        age =21
    def display(self):
   print(name,age)
   print(self.name,self.age)
   print(self.m1())
object =c1()
object.display()

#EG :6
#To use the variable inside the constructor in another methods
class class1:
    #email ="deepika@gmail.com" #static variable
    def __init__(self):   
        self.name = "deepu" #instance variable
        self.email = "deepu@gmail.com"
        return name,email#error--> cannot use return with construction
    def display(self):
        print(self.name, self.email)


c1=class1()
c1.display()

#------->Inheritance
#The process of utilizing the methods and attribbutes of parent class
#throught the object of child class it is called as inheritance
*Single Inheritance
*Multilevel Inheritance
*Multiple Inheritance
*Hybrid Inheritance
*Heirarichal Inheritance

#* Single Inheritance
It has only one parent class and only one child class

#EG:1#
class parent:
    def m1(self):
        print("I am parent class")

class child:
    def m2(self):
        print("I am child class")

obj = child()
obj.m1()

#EG:2#
class c1:
    def __init__(self):
        print("I am constructor from parent class")
        
class child1(c1):
    pass

obj = child1()

#EG:3#
class parent:
    name = "deepu"


class child(parent):
    name = "name1"
    def display(self):
     print(self.name)

d = child()
d.display()


#Multilevel inheritance
#EG:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("Meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

#EG:2
class honda_city:
    def engine_specs(selff,cc,hp,torque,fuel_type,num_of_piston):
        print(cc,hp,torque,fuel_type,num_of_piston)

    def body_specs(self,color,weight,height,length,vehicle_type):
            print(color,weight,height,length,vehicle_type)
class Honda(civic):
    pass

honda =Honda()
honda.honda_city_engine_specs(1500,230,2979,"petrol",4)
honda.civic_body_specs("white",2000,5.5,8,"Hatchback")

#Multiple Inheritance
#It hass multiple parrent and 1 child

class while_petrol:
    def function(self):
        print("used to Airplans")

class Organic_petrol:
    def function(self):
        print("used for Bike,cars")

class premium_petrol:
    def function_p(self):
        print("sport cars,bikes")

class petrol(while_petrol,Organic_petrol,premium_petrol):
    def defination(self):
        print("petrols types")

p = petrol()
p.defination()
p.function()

#Hybrid inheritance

#The one parent class will act as parent for all the child classes
#The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("class1")
class c2(c1):
    def m2 (self):
        print("class2")
class c3(c2):
    def m3(self):
        print("class 3")
class c4(c3):
    def m4(self):
        print("class 4")
    def m3(self):
        print("i am m3 from c4")
              
class c5(c4):
    def m5(self):
        print("class 4")
class c6(c5,c4,c2,c1):
    def m6(self):
        print("class 4")
obj= c6()
obj.m3()

#!------->polymorphism
#poly -many,morph--->form
#A function which has the ability to perffor more than 1 functionality
#then it is considered to be as polymorphism


#polymorphism in builtin functions
#len()--->which is used to find the  length of list,tuple,dict etc...
#index()
#max()
#min()
#count()
#pop()
#and more....


#polymorphism in operators
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])


#print(6*7)
l1 = [1,2,3,4]
print(type(*l1))
def f1(*args)
l1 =[1,2,3,4]
print(l1*10)

polymorohism in classes
we canacheive polymorphism in 2 ways
1)method overloading-->it is not possible in python
2)method overridings


























