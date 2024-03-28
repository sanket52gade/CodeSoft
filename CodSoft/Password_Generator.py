#Password Generator in Python
import random
import string

Uper_a =  int(input("Enter The Size OF The Upper Alphabet Password "))
lower_a =  int(input("Enter The Size OF The Lower Alphabet Password "))
special_c =  int(input("Enter The Size OF The Special Character Password "))
Numebr =  int(input("Enter The Size OF The Digital "))

c = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
     
password = ''.join(random.sample(c,Uper_a + lower_a + special_c + Numebr ))

print(f' Genrated password is : {password}')