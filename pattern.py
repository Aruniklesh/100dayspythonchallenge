no_of_row = int(input("Enter the rows that u want to print: "))
for j in range(1, no_of_row+1): #1 represents the starting range and +1 representss the increment of the input so it will print 1 and hold

    for i in range(1, j+1):
        print(i , end=" ")
    print("")