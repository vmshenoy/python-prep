# ===================================================================
#  Reading Input from Command line
#  To run file call <file_name>.py <a1> <a2> <a3> ...
# ===================================================================

# import the commnadline argument 
from sys import argv

# read the arguments and store them in variables
# the first argument is always the file name
# count of argument passed should match the variables declared
fileName, a1, a2, a3= argv

print("File   : ",fileName)
print("1st arg:", a1)
print("2nd arg:", a2)
print("3rd arg:", a3)