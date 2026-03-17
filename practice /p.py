this_dict ={
    "model": "ford",
    "year": 2020,
    "colors": ["red", "blue", "white"]
    
}

print(this_dict["model"])


x= this_dict.keys()
print(x)
this_dict["price"] = 20000
print(this_dict)


if "model" in this_dict and this_dict["model"] == "ford":
    print("The model is ford")
else:    print("The model is not ford")

this_dict.update({"year": 2026})
print(this_dict)


del this_dict["price"]
print(this_dict)
print("looping through dictionary values:")
for x in this_dict:
    print(this_dict[x])
    
print("\n\nPrinting keys and values:")
for x,y in this_dict.items():
    print(x,y)
    
    
print("\n\ncreating a dictionary using dict() constructor:")
new_dict =dict(this_dict)

for x ,y in new_dict.items():
    print(x,y)



#multiple dictionaries
print("\n\nMultiple dictionaries:")

my_family = {
    "child1": {
        "name": "Alice",
        "age": 10
    },
    "child2":{
        "name": "Bob",
        "age": 8        
    },
    "child3"    :{
        "name": "Charlie",
        "age": 5
    }
}


#print(my_family["child1"]["name"])

for x , obj in my_family.items():
    print("" + x)
    for y in obj:
        print("\t" + y + ": " + str(obj[y]))