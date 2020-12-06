size_list=int(input("Enter the size of list:"))

def search_from_hash(key,hash_list):
    searched_index=hash_function(key)
    if hash_list[searched_index]:
        print("Value found")
    else:
        print("Value not in list")
    
def hash_function(value):
    global size_list
    return value%size_list

def map_hash2index(hash_return_value):
    return hash_return_value

def create_hash_table(list_values,main_list):
    for value in list_values:
        hash_return_value=hash_function(value)
        list_index=map_hash2index(hash_return_value)
        if main_list[list_index]:
            print("collision detected")
        else:
            main_list[list_index]=value

list_values =[11,21,31,41,51,61]

main_list=[None for x in range(size_list)]
print(main_list)
create_hash_table(list_values,main_list)
print(main_list)

search_from_hash(30,main_list)
