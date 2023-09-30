import os


if os.path.exists('toDo.txt'):
    print("the toDo list is here")
else:
    with open('toDo.txt','w') as file:
        file.write()
        
#convert the list from toDo.txt into list

toDotxt = open ('toDo.txt','r')
data = toDotxt.read()
toDolist = data.split("\n")

#loop to come back to this point after modify/add/delete
while True:
    print("here is your toDo list")
    print("--------------------")
    num =0
    for i in toDolist:
        num+=1
        print(str(num)+" "+i)
    print("--------------------")

#give options to add / delete modify the list

    action = input("add a list (a). modify a list (m). delete a list (d). quit (q): ").lower()
    if action == "a":
        
        last_index = len(toDolist) - 1 
        print(last_index)
        #last_index+=1
        item=input("what do you want to add?: ")
        #toDolist.append(item)
        toDolist.insert(last_index,item)
        last_index+=1
        #with open('toDo.txt','w') as file:
        #    text=toDolist
            
    elif action == "m":
        j =int(input("which one do you want to modify? :"))
        j-=1
        toDolist[j]=input("please type the change: ")
        #with open('toDo.txt','w') as file:
        #    text=toDolist
            
    elif action == "d":
        r =int(input("which item number you want to delete?: "))
        r-=1
        print(r)
        toDolist.pop(r)
        #with open('toDo.txt','w') as file:
        #    text=toDolist
            
    elif action == "q":
        break
    
for item in toDolist:
        with open('toDo.txt','w') as file:
            file.write("%s\n" % item)
file.close()
    
