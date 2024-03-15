###DAY -5###

'''


#------>Common functions for list

l1 = [6, 7, 8, 9, 0]
print(len(11))
print(max(l1))


l1=[6 ,8,9,"p" , "u"]
print(max(l1)) #---->error coz its a combination of list and string
print(min(l1)) #----->error coz its a combination of int and sring


l1 = [6,7,8,9,8.89,-5,0.78]
print(min(l1) #-5

#Index() ---> to get index value of specific element
print(l1.index(9))
      

l1 = [6,7,8,9,8.89,-5,0.78]
coun() -->how many num of times an element is repeated
print(l1.count(6))

#!some functions which is specifically used for list

to add elements inside list
insert (index_value,element)--->to add element at specific index position
l1 =[6,6,6,7,8,9,8.89,-5,0.78]
pop()---->last element will be deleted
print(l1)


pop(index_value)---> used to delete elements at specific index
l1.pop(4) #4 is index value
print(l1)


#remove(element) ----> used to delete element directly
l1.remove(8.89)
print(l1)


#clear() ---> to complete delete all elements in list
l1.clear()
print(l1)

del --> to delete the list
del l1# or del(l1)
print(l1)
'''
'''
#--->join 2 lists

l1 =[9,0,8]
l2 =["p" ,"o" ,"t" ,34]
print(l1+l2)


#----->extend() to combine 2 lists
l1.extend (l2)
print(l1)

#copy()
l1 = [6,7,8,8,3]
l2 = l1.copy()
print(l2)
print(l1)


print(id(l1))
print(id(l2))


#difference btw shallow copy and deep copy
#shallow copy
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)
      
        
#Deep copy  --->used to copy the list with nested list    
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
print(l1[-1][1])

l2 = copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)


#Sort--->arrange elements in ascending order
l1 = [9,7,45,0,-6 ,5, 12]
l1.sort() #arrange in ascending order
print(l1)


l1.sort(reverse =True)to sort in descending order
print(l1)


l1 =['z','i','o','p' ,9]
l1.sort()
print(l1) #---->error


#list Constructor
list() --> to convert other collecction data type to list
l3 =((8,9,0))
print((list(13))

l4 =(8,9)
print(list(l4))
      
#Nested list
l1 = [8,9,[0,8,7],["p","o",'y'], [8,'t']]
print(l1[-2][1])
print(l1[1:4])
print(l1[1:-1])

# to delete "t" from l1
l1 = [8,9,[0,8,7],["p","o",'y'],[8,'t']]
l1[-1].remove('t')
print('t')
      
#Combine the list in ["p","o",'y'],[8,'t'] lists in l1["p","o",'y',8,'t']
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)



#------>Tuple

***Characteristics of Tuple***
(1)Tuple have to  be souurounded by ()
(2)The elements inside tuple are not chanagable
(3)The elements inside tuple are indexed
(4)The elements will execute in order
(5)Its is hetergeneous
(6)It allow duplicate elements

'''
'''
#EG:
t1 = (8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
print(t1)
print(type(t1))


#Indexing ,Slicing are all same as list
#Ways to create tuple
t1=(8)
print(type(t1))

t2=(10,)
print (type(t2))

#len(),min(),max(),index(),count()----> all same as list


#To add elements inside tuple --->cannot add
#Cannot delete any element from tuple


#join 2 tuples
t1 = (8,9,0)
t2 = (6,7,8)
print(t1+t2)

#TO add all elements inside list and tuple
#sum()
l1=(8, 9, 7, 6)
print(sum(l1))

#Sort tuple
t1 = (8 ,9, 89, 0, 12)
print(tuple(sorted(t1)))


#Sorting the tuple
t1 =(8,9,0,89,12)
print(tuple(sorted(t1)))
print(tuple(Sorted(t1,reverse=True)))
'''
'''
#Iterate based on elements
l1 = [9,8,0,6,5]
for i in l1:
    print(i)
'''
'''
#Iterate based on index value
l1 = [9,8,0,6,5,56]
for i in range(0,len(l1)):
    print(l1[i])


#------>Strings

s1 = 'o'
print(type(s1))


s1 ="hello world"
#To access string
print(s1)

#Indexing and slicing ---->Arithmetic Error same ass list and tuple

str =("hello world")
print(str[0:5])
'''
'''
#----->Common functios of String
#len(),min(),max(),index(),count()
s1 ="hello world"
print(len(s1))
print(max(s1))
print(min(s1))

#ord()--->used to find the ASCII value of a character  
s1 = 'u'
print(ord(s1))

#functions of string
s1 ="hello world"

#To convert all charactrs to upper case
print(s1.upper())

#To convert all characters to lower case
print(s1.lower()) 


#Strip()--->to eliminate the space in beginning and end of string
s1 = "Where are you? "
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())


#split()--->to split the words in string based on character
s1 = "where are you?" 
print(s1.split(" "))
print(s1.split("r"))
print(s1.count('e'))

#replace()---->to replace a specific char in the string
s1 ="where are you?"
print(s1.replace('r','&&'))

#swapcase()--->to convert to small to capital at a time
s1 ="HEY there"
print(s1.swapcase())


#title()----> to write the string in format of title
s1 = 'never giveUP'
print(s1.title())


#Capitalize()----> 1st char of string will be converted to capital
s1 = 'never giveUP'
print(s1.capitalize())

#join the strings ()
s1 ="hello"
s2 = 'world'
print(s1+s2)

s1 = how are you
i am fine
hey there
'''
'''    
#splitlines ()---->used to split the string based on lines
print(s1.splitlines())


#find()---->to find the index based on a character
s1 ="hello world"
print(s1.find('h'))
print(s1.index('o'))


#join()---->

l1=["hey","there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "welcome to all"
print(s1.endswith('l'))
print(s1.startswith('l'))


s1 ="67"
print(type(s1))
print (s1.isdigit())


#print the string in reverse manner

s1 ="welcome to all"
print(s1[::-1])

#!----->Eg:1
s1 ="HEY there you aRE"
count = 0
for i in s1:
    if i.islower():
        count+=1
 print("The total number of lower case: ",count)                                                                                                                                                                                                                                                                                                                                         

'''
'''
#!----->EG:2 r--->
s1 = 'restarter'
fst = s1[0]
bal = s1[1:]
txt = bal.replace(fst,"$")
print(fst+txt)
'''

s1='''Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambledit to make a type
specimen book. It has survived not only five centuries,
but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing
Lorem Ipsum passages,and more recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsu'''

character = len(s1)
print(character)
words = s1.split(" ")
print(len(words))

sentences = s1.split('.')
for val in sentences:
    if val =='':
        index = sentences.index('')
        sentences.pop(index)
print(len(sentences))

space = 0
for val in s1:
    if val == " ":
      space=space+1
print(space)
      














      
