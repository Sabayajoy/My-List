#list program
my_list = []

#appending
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
 
print ("after append:",my_list)

#inserting
my_list.insert(1,15)
print( "after inserting:",my_list)
  
#extending
my_list.extend([50, 60, 70])
print("after extending:",my_list)

#removing
my_list.pop()
print ("after removing:",my_list)

#sorting
my_list.sort()
print("after sorting:",my_list)

#print the index value of 30
print(my_list.index(30))

