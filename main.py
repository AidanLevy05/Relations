import itertools

# get set
numElements = int(input("How many entries would you like in your set? "))
set = []
relations = []

for i in range(numElements):
    element = input("Enter element: ")
    set.append(element)
    
print("Current list:")
print(set)

# cartesian product
cart_prod = list(itertools.product(set, repeat=2))

# print all possible relations
# num relations = 2 ^ size of cartesian product
# which can also be done using bit shifting
num_relations = 1 << len(cart_prod)

print("All relations:")
for i in range(num_relations):
    # Using bitwise logic
    
    # if (i & (1 << j))
    # Determines whether we will include cart_prod[j] in the relation list
    
    # 1 << j shifts 1 left by j bits --> 2 ^ j
    # Ex. If j = 1, 1 << j results in 0001 --> 0010
    
    # i & (1 << j) --> bitwise operation between i and 2 ^ j
    # If jth bit of i is 1, result in true
    # Else, false

    relation = [cart_prod[j] for j in range(len(cart_prod)) if (i & (1 << j)) ]
    print(relation)
    relations.append(relation)
    
# make sure none of them match
isRelation = True; 

for i in range(num_relations):
    for j in range(num_relations):
        if not (i == j):
            if relations[i] == relations[j]:
                isRelation = False;
                break;
            
if (isRelation):
    print("This relation is correct.")
else:
    print("This relation is not correct.")
