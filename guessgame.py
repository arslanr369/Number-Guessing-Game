import random

while True:
  cnumber=random.randrange(1,101)
  user=int(input("Enter the Number:---"))
  if cnumber > user:
    print("Cumputer Number",cnumber)
    print("Cumputer Number High")
  elif cnumber < user:
    print("Cumputer Number",cnumber)
    print("Cumputer Number Low")
  else:
    print("Equal")
