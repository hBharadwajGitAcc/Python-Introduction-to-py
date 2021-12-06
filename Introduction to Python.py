# Task 1

l1 = [1,2,3,4,5,6]
l2 = [6,5,4,3,2,1]
for i in range(0,6):
    if l1[i]>l2[i]:
        print("l1 element value is greater than l2 element value")
    else:
        print("l2 element value is greater than l1 element value")




# Task 2
        
Tuple = (10,20,30,40,50)
Tuple = tuple(list(map(lambda x : x + 5, Tuple)))
 
        ### or ###

Tuple = (10,20,30,40,50)
Tuple = list(Tuple)
Tuple = [x + 5 for x in Tuple]
Tuple = tuple(Tuple)
print(Tuple)

        ### or ###

Tuple = (10,20,30,40,50)
Tuple = list(Tuple)
for a in range(0,len(Tuple)):
    Tuple[a]+= 5
    continue
Tuple = tuple(Tuple)
print(Tuple)




# Task 3

def add_10(b):
    b += 10
    return b

add_10(20)




# Task 4

def check_odd_even(c):
    if c%2==0:
        print(c, 'is an even number')
    else:
        print(c, 'is a odd number')
    
check_odd_even(50)
check_odd_even(55)

