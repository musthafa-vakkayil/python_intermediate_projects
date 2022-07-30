# Defining Empty Array
array = []

# getting Array Size
n = int(input("Enter Array Size"))

# Getting Array Elements
print("Enter Array Elements")
for i in range(n):
    x=int(input())
    array.append(x)

# Printing Array Elements
print("the array is")
for i in range(n):
    print(array[i])

res = 0
current = 0

for i in range(n):
    if array[i] == 0:
        current=0
    else:
        current+=1
        res = max(res, current)

print(f"The Maximum Consecutive Number of Ones are {res}")