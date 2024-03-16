### DAY-6###

#Python code to capitalize the first and last character of
#of each
'''
s1=input("enter a string:")
fst = s1[0].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)
'''
'''
n = 128
temp = n
f1 =0
str1 = ""
while n!=0:
    rem =n%10
    check = temp % rem
    if check!=0:
        f1 = 1
    n= n//10
if f1 ==0:
    print("yes")
else:
    print("no")



l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

print(l1[0]+l2[1]+l1[1]+l2[1])
l3 =[] 
for val in range(len(l1)):
   ans = l1[val]+l2[val]
   l3.append(ans)
print(l3)   



#-------->Sets

#Characteristics of set:

1.) Set can be created using{}
2.) The element inside set are not indexed
3.) Does not allow duplicate values
4.) it unordered
5.) heterogenous
6.) mutable or changable
'''
'''
#EG :1
s1 ={9,89,9,7.76,8+7j,(8,7,5), "truck" ,'e'}
print(s1)


#EG :2
s2 = {5,8,98,[9,0]}
print(s2)--->error


#EG :3
min(),max(),len()

'''
'''
#EG :4
#To add element inside set

s1 = {8,78,67,'u'}
s1.add(43)
print(s1)

#update()
s1.update([9,0])
print(s1)

#To delete element inside set
s1 = {8,78,7,'u'}
print(s1)

#remove()
s1= {1,2,3,4}
s1.remove(3)
print(s1)


#discard()
s1.discard(67)
print(s1)


#clear()
l1 ={}
print(type(l1))--->datatype is dict

s1 = set() # to crete empty set
print(type(s1))

s1={8,9,0}
s1.clear()
print(s1)

del s1
print(s1)


# join the sets
s1 = {9,0,8}
s2 = {9.90 ,"card",'t',56}
#union()--->to combine 2 sets
s3=s1.union(s2)
print(s3)


intersection() ---> to get common elements inside list 
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.intersection(s2))

'''
'''
#difference()
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.differencce(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

#isdisjoint(),issubset(),issuperset()

#----->PROBLEM:1
s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

for val in s1:
    if val in s2:
        str1 = "Its joint set"
print(str1)
'''
'''
#! ------>Dictionary
#Characteristics of dictionary

1.) Have to be surrounded by{}
2.) It have to be in the form of key,value pair
3.) It is mutable
4.) Duplicate keys are not allowed,
5.) Duplicate values are allowed
6.) It is unidexed
7.) It is ordered
8.) Key does nat allow mutable datatypes
9.) Values allow mutable datatypes


d1 ={1:100,2:200 ,3:300 ,4:400}
# to access elements in dictionary

#print(d1)
or
To access the values ,have to use key
print(d1[1]) #o/p---->100


#Some common functions
#len(),min(),max()
print(min(d1))
print(max(d1))

#To find min ,max based on values
print(min(d1.values()))
print(max(d1.values()))


#dictionary based funnctions
#to add element(key and value pair) in dict
d1 = {1:100,2:200,3:300,4:400}
d1[5] = 500
print(d1)


#To replace a value in dictionary
d1 ={1:100,2:200,3:300,4:400}
d1[2]="mango"
print(d1)
'''
'''
#delete the element from dictionary
d1 = {1:100,2:200,3:300,4:400}
popitem() #--->to delete last key pair in dict
d1.popitem()
print(d1)
#pop()
d1.pop(2) #2 is the key in dictionary
print(d1)

'''
'''
#clear(),del


#join 2 dictionary
update()
d1={1:100,2:200,3:300,4:400}
d2 = {"a":"apple","b":"boy","g":"girl"}
d1.update(d2)
print(d1)

#get()
d1 = {1:100,2:200,3:300,4:400}

#to print the all the keys()
#print(d1.keys())
#print(type(d1.keys()))

# to print all the values
print(d1.values)

#Iterating dictionary: # to iterate values alone
#for val in d1:
      print(val)

#for val in d1.values(): to iterate values along
      print(val)

#to get both key and values
for key ,val in d1.items():
      print(key,val)


'''
'''
#PROBLEM:1
n = int(input("Enter a number:"))
integer =[]
float_value=[]
string=[]

for val in range(n):
    value = eval(input("Enter the values:"))
    if type(value)== int:
        integer.append(value)
    elif type(value) == float:
        float_value.append(value)
    elif type(value) == str:
        string.append(value)
    else:
         print("pls provide data in int,float,string")
print(integer)
print(float_value)
print(string)

'''
'''
#Problem:2
# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 =set()

for val in set1:
    if val not in set2:
       set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3) 
'''


l1= [1,2,3,4]
l2 =["a","b","c","d"]
for val in range(len(l1)):
    d1[l1[val]] = l2[val]
print(d1)    






'''
d1 ={}
d1[l1[0]] =l2[0]
print(d1)
d1 ={}
d1[l1[1]] = l2[1]
d1[l2[2]] = l2[2]
print(d1)
'''










      
      



























 

                                                                





















