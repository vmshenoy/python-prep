# ===================================================================
#  List Type
# ===================================================================
print("\nList Type")
a = [1,2,3,4,5]
b = ["sun","mon","tue","wed"]
c = [1,"sun",False]
print(f"Interger list: {a}")
print(f"String list: {b}")
print(f"Mixed list: {c}")
print(f"Type of list is {type(a)}")

# size of list using len(<list>)
print(f"Size of a:{a} is {len(a)}")

# assignment
a[0] = 10
print(f"a[0] = 10 a:{a}")

# list of list
nest = [[2,[12]],5,["hello"]]
print(f"\nnest:\t\t{nest}")
print(f"nest[0]:\t{nest[0]}")
print(f"nest[0][1:2]:\t{nest[0][1:2]}")
print(f"nest[1]:\t{nest[1]}")
print(f"nest[2]:\t{nest[2]}")
print(f"nest[2][0][1]:\t{nest[2][0][1]}")
print(f"")

# copy list
l1 = a[:]
print("l1 = a[:]")
print(f"a:{a} \nl1:{l1}")
a[0] = 1
print(f"a[0] = 1 \na:{a} \nl1:{l1}")

# list comparision using (==) and (is:check object reference)
l1 = [1,2,3]
l2 = [1,2,3]
l3 = l2
print(f"\nl1:{l1} \nl2:{l2} \nl3:{l3}")
print(f"l1 == l2 is {l1 == l2}")
print(f"l3 == l2 is {l3 == l2}")
print(f"l1 is l2 is {l1 is l2}")
print(f"l3 is l2 is {l3 is l2}")
l2[0] = 0
print("set l2[0] = 0")
print(f"l1 == l2 is {l1 == l2}")
print(f"l3 == l2 is {l3 == l2}")
print(f"l1 is l2 is {l1 is l2}")
print(f"l3 is l2 is {l3 is l2}")

# list concatenation: generates new list
l3 = l1 + l2
print(f"\nl3 = l1 + l2 is {l3}")
print(f"l3 == l2 is {l3 == l2}")
print(f"l3 is l2 is {l3 is l2}")

# ===================================================================
# Advance list operations
# ===================================================================
str = "it is a small world in his hand"
# convert the string to word array using split()
words = str.split(' ')

print(f"\nstr: {str}")
print(f"word array: {words}")

# sort the string array
words = sorted(words)
print(f"Sorted array: {words}")

# remove the last item from array using list.pop()
last = words.pop()
print(f"\nRemoved last item words.pop() = {last}")
print(f"word array: {words}")

# remove the first item from array using list.pop(0)
first = words.pop(0)
print(f"\nRemoved last item words.pop(0) = {first}")
print(f"word array: {words}")

# convert the word array to single string 
# using <seperators_string>.join(<word_list>)
print("\nJoin List: <seperators_string>.join(<word_list>)")
print(" ".join(words))
print("-".join(words))
print("_".join(words))
print(" ".join(words))
print("\nJoin part List")
print(" ".join(words[3:]))

# ===================================================================
# Dictionary Operations
# ===================================================================
print("\nDictionary demo")
days = {1 : 'Mon',2:'Tue',3:"Wed",4:"Thu",5:"Fri",6:"Sat",7:"Sun"}
grades = {"A":"Good ","B":"Satisfactory ","c":"Average","D":"Poor"}
print("days: ",days);
print("grades: ",grades);

# adding new item to days dictionary
days[8] = "new_day";
print("\ndays: ",days);

# get item by it's key value
print(f"\ngrades['A']: {grades['A']}");

# convert dicitionary to list,  using dictionary.items()
print("\n",grades.items());

# iterating over the dictionary
for a,b in list(grades.items()):
	print(f"{a} stands for {b}");
	
# get items by using .get(key)
print(f"\ndays.get(8): {days.get(8)}");

# Handling for missing keys
# Using .get(key,msg) function
# msg is returned if keyis not present
print(f"\ndays.get(9,'NA'): {days.get(9,'NA')}");
