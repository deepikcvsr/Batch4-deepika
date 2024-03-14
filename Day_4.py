                        ###DAY -3###
#----->WHILE LOOP
#------>break using while loop


#eg:1
#iterate from 20 to 30 and break the loop in 27
'''
i = 20
while i<31:
    if i==27:
        break
    print(i)
    i+=1
'''
'''
#eg:2
i = 27
while i<31:
    if  i==27:
        print(i)
        break
    i+=1
'''
'''
#------>continue
i = 20
while i<31:
    i=i+1
    if i ==27:
        continue
    print(i)
'''
'''
#while to iterate from 12 to 22
#find the sum of all nummbers

i =12
sum=0
while i<23:
    sum=sum+1
    i=i+1
    print(sum)
'''
'''
#Eg:2
#Find the average of value from 20 to 25
    
i=20
sum=0
count=0
while i<=25 :
    sum=sum+i
    count=+i
    i+=1
print(sum/count)
'''
'''
#------->nested for loop
#EG:1
for row in range(1,3+1):
     for col in range(1,4+1):
         print(row,col)
'''

'''
for row in range(5):
    for col in range(5):
        print("*",end="" )
    print()

'''
'''
sum = 0
for row in range(5):
 for col in range(5):
    sum =sum+1
    print(sum , end=" ")
    print()

'''

'''
#! to print stars in right angled tringle


for row in range (0,6):
    for col in range (0,6):
        print("*",end=" ")
    print()                                                                                                                            
'''
'''
for row in range(6,0,-1):
    for col in range(0,row):
         print("*", end=" ")
    print()
'''
'''
for row in range(5):
    for col in range(5):
        if col == 0 or col == 5-1 or row == 0 or row == 5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
'''

for row in range(0, 5):
    for col in range(0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
             print("*", end=" ")
        else:
             print(" ",end=" ")
    print()     
'''
'''
for row in range (0,5):
     for col in range(0,6):
         if ((row==0 and col==1) or (row==2 and (col==2 and col==4) or (row==2 and (col>1 and col<=5)))):
             print("*", end=" ")
         else:
             print(" ",end=" ")
     print()        
'''
'''
# ------->List<-----
 Data Types:(1)Primary (2) Collection
#Primary
   *number
   *string
   *boolen
   *none
   
#Collection
   *List
   *set
   *tuple
   *Dictionary

   
----->(1)LIST:The collection of elements are surronded by[] brackets are considered as list
EG: l1=[4,5,"hello".7+ij]

----->CHARACTERISCTICS OF LIST

(1)It consist of []
(2)It is mutable (elements in the list are changable)
(3)Every  element inside list is indexed
(4)It can hold duplicate values
(5)The elements inside list will be ordered format
(6)Its heterogenous



#Acess the elements in list
lst1 =[1,4,1,7,89.7,7.5,"p","i"]
print(l1)


#----->Indexing
In the collection datatypes like list,tuple,string,the elemnents with pre defined unique value called index value


we have 2 types of indexing
#Positive indexing --->starts with 0 from LHS
#Negative indexing ---->starts with -1 from RHS

#----->Positive Indexing
print(lst1[0])


#---->Negative Indexing
lst1=[1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-1])
'''
'''
#------>Slicing
lst1=[1,4,1,7,89.7,7.5,"p","i"]
print(lst1[6:8])
print(lst1[:5])
print(lst1[0:7:2])


lst1=[1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-7:-1:2])
'''

#To insert OR  add element inside list
#append()
l1 =[9,8,0,6]
l1.append("DEEPIKA")
print(l1)






















