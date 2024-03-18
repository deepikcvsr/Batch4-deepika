###Day-7###
'''
#Assessment coding:
#EG:1
 
d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
d1.update(d2)
print(d1)


#EG:2

set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
flag=0
for val in range(3):
    c= c+1
    if c==1:
       for val in set1:
           if val in set2 or val in set3:
               flag=1
               break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break
            
    if c==3:
        for val in set3:
            if val in set2  or val in set1:
                flag=1
                break
if flag==0:
    print("Disjoint")
else:
    print("joint")


#EG:3
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result=[list1[i]+list2[i]
for i in range(len(list1))]
print(result)

#or
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
i=1
print(l3)
'''
'''
#! Functions:
#Defination:
(1)Function is a block of code which is udes to perform a specific functionality
(2)Function can be created using def keyword

# Generally Function has 3 parts
Function declaration
Function defination
Function call

'''
'''
#! EG :1
def greet(): *function defination
    print("Welcome User!!")
greet()
greet()
greet()
greet()  #function calling
'''

#!EG:2
def greeting(name):
    print("Welcome",name)

for val in range(3):
    username = input("Enter the name:")
    greeting(username) 
    

#EG:3
    

    
    




    




    










                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              






        
        
