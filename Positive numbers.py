#printing positive numbers in a list


#Input of the list

my_list1 = [12,-7,5,64,-14]
print("Positive numbers in ",my_list1," are : ")

#using list comprehension
positive_num = [num for num in my_list1 if num >=0]

print(positive_num)

#Input of the list

my_list2 = [12,14,-95,3]
print("Positive numbers in ",my_list2," are : ")

#using list comprehension
positive_num = [num for num in my_list2 if num >=0]

print(positive_num)



#Another way to print the same output by replacing the order of functions performed

#input of the list

my_list1 = [12,-7,5,64,-14]
positive_num = [num for num in my_list1 if num >=0]
print("Positive numbers in ",my_list1," are : ")
print(positive_num)



#Input of the list

my_list2 = [12,14,-95,3]
positive_num = [num for num in my_list2 if num >=0]
print("Positive numbers in ",my_list2," are : ")
print(positive_num)
   
