from operator import index


list_1=["hello","book","tom","harry", "hecka"]
new_list=[]
string_holder=""
last_item = ""

for items in list_1:
    if items[-1] > string_holder:
        new_list.append(items)
        string_holder = items[-1]
        
    else:

        new_list.insert(int(list_1.index(last_item)),items)
    last_item = items
     

print(new_list)
