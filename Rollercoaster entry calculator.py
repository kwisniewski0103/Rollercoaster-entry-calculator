# 7. Rollercoaster entry calculator:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster :)")
  age = int(input("What is your age? "))
  if age >= 18:
    print(f"Your age is {age}, please pay 12 zł.")
  elif age >= 12:
    print(f"Your age is {age}, please pay 7 zł.")
  else:
    print(f"Your age is {age}, please pay 5 zł." )
else: 
  print(f"Sorry, your height is {height} cm, you have to grow taller before you can ride :(")

# 7.1. Rollercoaster entry calculator + photo taken:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster :)")
  age = int(input("What is your age? "))
  if age > 18:
    bill = 12
    print(f"Your age is {age}, you are an adult, please pay 12 zł." )
  elif age > 12:
    bill = 7
    print(f"Your age is {age}, you are a youth, please pay 7 zł.")
  else:
    bill = 5
    print(f"Your age is {age}, you are a child, please pay 5 zł.")
  wants_photo = input("Would you like a photo to be taken? Please put Y or N: ")
  if wants_photo == "Y":
    bill += 3
 
  print(f"Your final bill is {bill} zł.")
else:
  print(f"Sorry, your height is {height} cm, you have to grow taller before you can ride :(")

# 7.2. Rollercoaster entry calculator + photo taken + middle age crisis discount:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster :)")
  age = int(input("What is your age? "))
  if age < 12:
    bill += 5
    print(f"Your age is {age}, you are a child, please pay 5 zł." )
  elif age < 18:
    bill += 7
    print(f"Your age is {age}, you are a youth, please pay 7 zł.")
  elif age >= 45 and age <= 55:
    print(f"Congratulations, your age is {age}, you get a middle age crisis discount and you get your entry for free :)")
  else:
    bill += 12
    print(f"Your age is {age}, you are an adult, please pay 12 zł.")
  wants_photo = input("Would you like a photo to be taken? Please put Y or N: ")
  if wants_photo == "Y":
    bill += 3
  print(f"Your final bill is {bill} zł.")
else:
  print(f"Sorry, your height is {height} cm, you have to grow taller before you can ride :(")
