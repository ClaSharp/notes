a = [[1,2,3],
     [4,5,6]]

#One way to traverse a 2d list
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        print(a[i][j],end=' ')
#    print()

#Another way to traverse a 2d list
#def print_2dlist(1st):
#    for row in a:
#        for element in row:
#            print(element,end=' ')
#        print()


# Add all elements in 2d list
#sum = 0
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        sum += a[i][j]
#print(sum)

#for row in a:
#    for element in row:
#        print(element,end=' ')
#    print()
    
#for i in range(len(a)):
#    for j in range(len(a)):
#        a[i][j] += 1
#print_2dlist(a)

# Creating 2d list
#x = [[0] * 5]*8 DOES NOT WORK!!!
x = [[0]*5 for i in range(8)]
x[0][0] = 100
print(x)
        