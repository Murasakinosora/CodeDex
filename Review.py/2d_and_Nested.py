#2d array
number_grid = [
    [1,2,3],[4,5,6],[7,8,9],[0]
]

#printing the index 2 element of list on index one
print(number_grid[1][2])

#using for loop

for row in number_grid:
    print(row)
"/n"
#accessing individually using nested loops
for row in number_grid:
     for col in row:
        print(col)
#col has the value of each element of the list that is held by
#the variable row, col iterates through the list that is on the variable
#row which makes it possible to print the numbers individually

