#time complexity:--This doesn't mean amount of time a code takes cuz pc speed falls as a factor too in such case, but the number of lines the code takes to run cuz it's independed of pc speed
#Space complexity:--Mem taken by code
#Time complextity types:--worst case, avg case, best case
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)
#time complexity=O(n)


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)
#time complexity=O(n^2)

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
print_items(10)
#time complexity=O(n^3)

def print_items(n):
    for i in range(n):
        for k in range(n):
            print(i)
    
    for j in range(n):
        print(j)
print_items(10)
#time complexity=O(n^2)

def add_items(n):
    return n+n+n+n+n+n+n+n+n+n+n
#time complexity=O(1)


#binary search :--O(log n)


#O(n^2):-loop inside loop
#O(n):--Proportional
#O(logn):--divide and conquer
#O(1):--Constant