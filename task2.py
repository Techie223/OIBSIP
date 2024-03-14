import random
import string

#function to generate numeric password
def numeric_password(leng):
   x=''.join(random.choice(string.digits) for _ in range(leng))
   return x

#function to generate alphabetic password
def alphabetic_password(leng):
   x=''.join(random.choice(string.ascii_letters) for _ in range(leng))
   return x

#function to generate symbolic password
def symbolic_password(leng):
   x=''.join(random.choice(string.punctuation) for _ in range(leng))
   return x

#function to generate mixed password
def mixed_password(leng):
   all_chars=string.ascii_letters+string.punctuation+string.digits
   x=''.join(random.choice(all_chars) for _ in range(leng))
   return x

leng=int(input("Enter the length of password required :"))
type=int(input("choise 1:numbers only\nchoise 2:letters only\nchoise 3:symbols only\nchoise 4:mixed\nEnter choise number of charcters: "))

if type==1:
    password=numeric_password(leng)
    print(password)
elif  type==2: 
    password=alphabetic_password(leng)
    print(password)
elif  type==3: 
    password=symbolic_password(leng)
    print(password)
elif  type==4: 
    password=mixed_password(leng)
    print(password)
else:
    print("Invalid choise")


