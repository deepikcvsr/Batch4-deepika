#DAY-2
    
#------>Swapping of Varriables
a=7
b=5

temp=a #temp=7
a=b #a=5
b=temp #b=7

print(a,b)

#example-2
a=a+b #a=12
b=a-b #b=12-7=5
a=a-b  #a=12-5=7

#print(a,b)


#example-3
a,b=b,a#only in python
#print(a,b)


a=a*b #a=35
b=a/b#b=35/7=5.0
a=a/b#a=35/5=7.0
print (int(a),int(b))


a=7
b=8
print(id(a))
print(id(b))


import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))





#To check if the string is keyword or not
print(keyword.iskeyword("sid"))#False



#!----->literals
#literal is the constant value assigned to a variable
#A variable is constant to be constant it is defines
#in caps

#a=89#a is a variable
#A=78 #A is constant


#hash()---->it creates a hash value for constant datatypes and provides
#error for non constant datatype
n1=89+7j
print(hash(n1))
f1=(7,8,9)
print(hash(f1)) #error ---->list is non constant or mutable datatypes



#a=9;
#b=9;
#b=90;
#print(id(a))
#print(id(b))


#?erators are symbols which is used to perform various operations
#between 2 or more operands

#arithmatic
#assessment
#logical
#relational or comparsion
#bitwise
#identity
#mebership

# todo------->arithematic<------>+,-,*/,%,//,**
#eg:1
#a=8
#b=6
#c=9
#print(a+b+c)



#input ()----->used to get the runtime input
#eval()---->used to get the runtime values of all datatype
#n1=eval(input("enter the value:"))
#print(type(n1))


#a=4
#b=2
#print(a/b)#is used to get the quotient value
#print(a%b)#is used to get the remainder value



#!//-->floor division
#a=765433
#b=19
#print(a//b)#->the output will be in integer &the output
#will be based on floor value

#!**-->used for power of a number
#print(2**4)#-->16


#!Assignment -->=,-=,/+,//=,**=,?&=,|=

a=8
a+=2
#print(a)
a=30
a=-5
#print(a)
  
#comparision-->==,>,<,!=,<=,>=
a=8
b=7
#print(a>b)
a=9
b=5
#print(a==b)
  


#!Bitwise operator -->&,|,<<,>>
a=7
b=4
#print(a|b)

#AND

#A B A&B                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
#0 0 0
#0 1 0
#1 0 0
#1 1 1



#~---->
a = 9876
#print(~a)


#a=9
#128 64 32 16 8 4 2 1
#0 0 0 0 1 0 0 1#----> 9

#1 1 1 1 0 1 1  0--> -10

#0 0 0 0 1 0 1 0 ---> 10

#1 1 1 1 0 1 -> 1s compliment of 10
           #1 ->2s compliment 



#logical operators
#and ,or ,not
a=6
#print(a>3 and a<10)
#print(a>7 and a<30)
#print(not(a>8 and a<10))


#Identity operator
#is,is not
#print(a is b)
#print(a==b)


#a=[1,2,3]
#b=[1,2,3]
#print(a is b)
#print(a==b)

#a=[1 ,2 ,3]
#b=[1 ,2 ,3]



#!Membership operator
#in,not in
#l1=[7,8,9,0,6,5]
#num=55
#print(num in l1)
#print (num not in l1)

#num =678
#print(8 in  num) #error


#Conditional Statement
#if,elif,else

#EX:1
#a=6
#if a:
#print("hello")


#EX:2
#a=6
#if a>3:
#   print("hey")_
#  else:
#     print("no")

#EX:3
#if7>8:
#   print("hello")_
#  else:
#     print("no")


#EX:4
#a=0
#a=None
#a=False
#a=""
#if a:
#print("yes")
#else:
#print("no")


#EX:5
#a number is even or odd
num=int(input("enterr a number:"))
if("num%2)==0
printf(num,"is even")
   
   else:
       print(num,"is odd")


#EX:6

#sum:2
#name=int(input("enter a number:"))
#age=int(input("enter a age:"))
#nationality=input("enter the nation:")

if age>18 and nationality=="Indian"
print("elgible for vote")
else:
    print("not elgible")





























 

