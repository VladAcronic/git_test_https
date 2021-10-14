# this is nowel file for testing prnt func

# prine empty line
print ()

# print some string
print ("file was modified under tracking")

# also print some string:
print ("string for presicion tracking diff")

# добавим работу с классами
from fibo_function import cls__fibo

fibo_count = 100
fibo_number = cls__fibo.Fibo (fibo_count)
fibo_number.calculate_fibo_number ()
print (fibo_number)

