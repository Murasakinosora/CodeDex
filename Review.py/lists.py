keywords = ["Operator","Integer","Character"]
temp_num =[1,2,3,4,5]

print(keywords)

#getting values in the list by range

print(keywords[0:2])

#adding list to another list
#keywords.extend(temp_num)
print(keywords)

#adding at the end of the list

keywords.append("additional")
print(keywords)

#inserting to a certain place

keywords.insert(5,"inserted")

print(keywords)

#removing a certain element

keywords.remove("inserted")
print(keywords)

#removing all would be keywords.clear()
#pop
temp = keywords.pop() #has the popped value
print(keywords)

#checking if the value exists in the list

print(keywords.index("Operator"))

#sorting
keywords.sort()
print(keywords)

#reversing
temp_num.reverse()
print(temp_num)

#copying a list
keywords.extend(temp_num)
copy = keywords.copy()
print(copy)