# ===================================================================
#  Control Flow
# ===================================================================
print("Control Flow")

# Conditional Execution
# if:..elif:..else:..
#x = int(input("Enter input:"))
x = 3
print(f"\nx = {x}")
if x == 1:
	print("inside if x == 1:")
elif x == 2:	
	print("inside elif x == 2:")
elif x == 3:	
	print("inside elif x == 3:")
elif x == 4:	
	print("inside elif x == 4:")
else:
	print("Inside else")

# Repeated Execution	
# for loop using list
a = [1,2,3,4,5]
print(f"\nfor loop on list a:{a}")
for i in a:
	print(i)

# for loop using range()
print(f"\nfor loop on range(0,3)")
for i in range(0,3):
	print(i)

print(f"\nfor loop on range(3,5)")
for i in range(3,5):
	print(i)

# while loop	
print(f"\nwhile loop on list a:{a}")
count = 0
while count < len(a):	# enter if condition is True
	print("while a[{count}]:{a[count]}")
	count = count + 1	# progress towards termination