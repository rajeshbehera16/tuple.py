fruits=("apple", "banana","cherry","date")
print("Original tuples:",fruits)
print("First fruit",fruits[0])
print("Last fruit",fruits[-1])

count_banana=fruits.count("banana") 
print("Count of banana",count_banana)
index_cherry=fruits.index("cherry")
print("Index of '.cherry'",index_cherry)
if "apple" in fruits:
    print("'apple' is in the tuple")
    print("Iterating over the tuple...")
    for fruit in fruits:
     print(fruit)
     print("Iterating over the tuple...")
     for fruit in fruits:
         print(fruit)
         fruit1, fruit2, fruit3, fruit4=fruits
         print("Unpacked fruits", fruit1, fruit2, fruit3, fruit4)
    try:
         fruits[0]="orange"
    except TypeError as e:
            print("Error",e)
            new_fruits=fruits+("elderberry",)
            print("New tuple after adding an element",new_fruits)
            print("Slied tuple(first two elements)",fruits[2])
            nested_tuple=(fruits,("grape","kiwi"))
            print("Nested tuple ",nested_tuple)
            print("Length of the tuple:", len(fruits))