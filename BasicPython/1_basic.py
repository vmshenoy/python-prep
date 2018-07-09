# ===================================================================
#  Assignment Statement: <variable> = <value/expression> 
# ===================================================================
i = 10
j = 12
print(f"Assignment statement \ni={i}, j={j} \n")

# ===================================================================
#  Numeric Type: Int, Float 
# ===================================================================
i = 179		# interger
j = 3.14	# float (mentisa + exponent)
print(f"Numeric Type \nInterger:{i} \nFloat:{j}")
# get the type of variable: type(<var>)
print(f"Type of i={i}  is {type(i)}")
print(f"Type of j={j} is {type(j)}")

# Operations on Numbers
# followa PEMDAS Parentheses>>Exponents>>Multiplication>>Division>>
# (modulus)>>Addition>>Subtraction
i = 10
j = 2
print(f"\ni:{i}, j:{j}")
# Addition
res = i + j
print(f"{i} + {j} = ", res)
# Subtraction
res = i - j
print(f"{i} - {j} = ", res)
# Multiplicaton
res = i * j
print(f"{i} * {j} = ", res)
# Division always returns a float
res = i / j
print(f"{i} / {j} = ", res)
# Quotient
res = i // j
print(f"{i} // {j} = ", res)
# Remainder
res = i % j
print(f"{i} % {j} = ", res)
# Exponent
res = i ** j
print(f"{i} ** {j} = ", res)

# ===================================================================
#  Boolean Type: True Flase 
# ===================================================================
t = True
f = False
print("\nBoolean Type: True Flase ")
print(f"Type of t={t} is {type(t)}")

# Logical operation:
print("\nLogical operation supported: and, or & not")
print(f"not {t} is {not t}; not {f} is {not f}")
print(f"x and y is True, if both are True else False")
print(f"x or y is True, if at lest one is True else False")

# Comparision operation
print("Comparision operation: (==), (!=), (<), (>), (<=) & (>=)");

# ===================================================================
#  String Type
# ===================================================================
str = "hello world"
print("\nString Type ")
print(f"Type of str='{str}' is {type(str)}")
print("""\nString values are enclosed inside quotes, 
single (') or double (\") quotes for Single-line string, 
triple (''') quotes for Multi-line string""")

# position of characters
# forward starts from 0,1,2...n-1
# backwards starts from -1,-2,...-n
str = 'world'
print(f"\nstr='{str}'")
print(f"First char: {str[0]}")
print(f"Last char: {str[-1]}")
print(f"Second char: {str[1]}")
print(f"Second from last: {str[-2]}")

# concatenation: str1 + str2 
str1 = "hello "
print(str + str1)

# string lenght: len(str)
print(f"Lenght of str:'{str}' : {len(str)}")

# substring: produces new string
str = 'world'
print(f"\nstr='{str}'")
print(f"str[0:1]: {str[0:1]}")
print(f"str[:2]: {str[:2]}")
print(f"str[2:]: {str[2:]}")
print(f"str[:]: {str[:]}")
print(f"str[5:1]: {str[5:1]}")	# no error
print(f"str[0:10]: {str[0:10]}")# no error

# ===================================================================
#  Printing 
# ===================================================================
print("\nPrint Demo")
aa = "nice"
tm = "Its a very {} {}."
# using the format function
print("Its a very {} day.".format('nice'))
print("Its a very {} day.".format(aa))
print(tm.format(aa,"day"))

# using the print(f"") syntax, only in py 3.6+
print(f"Its a very {aa} day.")

# ===================================================================
#  Reading Input
# ===================================================================
print("\nInput Demo")

# using input()
print("How old are you, in years?",end=' ')
age = input();
print(f"You are {age} years old")

# using input(<prompt_msg>)
age = input("What is your name? ")
print(f"Hello {age}, how are you?")