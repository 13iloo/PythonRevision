# sdfsdfsdfsdf
# print(('Hello\n')*3 + input("who are you?"))

# input
# a = input("a:")
# b = input("b:")
# c=a
# a=b
# b=c
# print(b)

# operators
# print("Hello")
# City = input("what city did u grow up in?\n")
# Pet = input("what is the name of your pet?\n")
# result = int(City) / int(Pet)
# #/Pet
# myResult = str(result)
# print(myResult)

# string,data types
# my_input = input("put in the number here\n")
# first_digit = my_input[0]
# second_digit = my_input[1]
# sum  = int(first_digit)  +  int(second_digit)
# print(first_digit + " + " + second_digit + " = " + str(sum))


# weight = input("weight: \n")
# height = input("height: \n")

# BMI = float(weight)//(float(height)**2)
# print(round(BMI,2))
# print("{:.2f}".format(BMI))


# age = input("Whatis your current age?  ")
# age_as_int = int(age)
# remaining_years = 90 - age_as_int
# age_in_months = remaining_years * 12
# age_in_weeks = remaining_years * 52
# age_in_days = remaining_years * 365
# print(f"ÿou have" )


# input_num = int(input("ïnsert the number: "))
# if input_num%2==0:
#     print("it is even")
# else:
#     print("it is odd")



# elif
# height = float(input("what is your height(m): "))
# weight = float(input("what is your weight: "))

# BMI = weight / height**2

# if BMI < 18.5:
#     print("underweight")
# elif BMI < 25:
#     print("normal weight")
# elif 30 > BMI:
#     print("overweight")
# elif 35 > BMI:
#     print("obese")
# else:
#     print("clinically obese")

# print("{:.2f}".format(weight / height**2))
# print(f"{round(BMI,2)}")



# nested if
# year = int(input("Which year do you want to check?"))

# if year % 4 ==0:
#     if year % 100 ==0:
#         if year % 400 ==0:
#             print("it is a leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("it is a leap year")
# else:
#     print("not a leap year")




# print("Welcome to Python Pizza Deliveries! ")
# size = input("What size pizza do you want? S, M,or L:  ")
# add_pepperoni = input("Do you want pepperoni? Y,or N:  ")
# extra_cheese = input("Do you want extra cheese? Y,or N:  ")

# bill = 0

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(bill)


# height = float(input("what is your height(m): "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? " ) )
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5." )
#     elif age < 18:
#         bill = 7
#         print("Youth tickets are $7." ) 
#     elif age >= 45 & age <= 55:
#         bill = 0
#         print("Your tickets are free." ) 
#     else:
#         bill = 12
#         print("Adult tickets are $12." )
#     wants_photo  = input("Do you want a photo taken? Y or N.")
#     if wants_photo == "Y":
#         bill +=3
# print(bill)


# # ❤️ Love Score Calculator
# print("Welcome to the Love Calculator! ")
# namel = (input("What is your name? \n")).lower()
# name2 = (input("What is their name? \n")).lower()

# t_count = namel.count("t")+ name2.count("t")
# r_count = namel.count("r")+ name2.count("r")
# u_count = namel.count("u")+ name2.count("u")
# e_count = namel.count("e")+ name2.count("e")

# l_count = namel.count("l")+ name2.count("l")
# o_count = namel.count("o")+ name2.count("o")
# v_count = namel.count("v")+ name2.count("v")
# e2_count = namel.count("e")+ name2.count("e")

# tenth = t_count + r_count+ u_count+ e_count
# ones = l_count + o_count+ v_count+ e2_count

# percentage = tenth*10 + ones

# print(percentage)

# if percentage < 10 or percentage>90 :
#     print(f" Your score is {percentage}, you go together like coke and mentos. ")
# elif percentage >= 40 and percentage <= 50 :
#     print(f" Your score is {percentage}, you are alright together.")
# else:
#      print(f" Your score is {percentage}")


# import random
# randomlntegeter= random.randint(1,5)
# print(randomlntegeter)
# randomFloat= random. random() * 5
# print ( randomFloat)
# love_score= random. randint(1, 100)
# print(f"Your love score is {love_score}")


# Coin Toss
# import random
# num = random.randint(0,1)
# result = ""
# if num == 1:
#     print("Heads")
# else:
#     print("Tails")


# import random
# names_string = input("Give me names_string everybody's names, seperated by a comma.")

# names = names_string.split(",") 

# # index = random.randint(0,len(names)-1)
# # print(f"{names[index]} is going to buy the meal today!")

# personwhowillpay = random.choice(names)
# print(personwhowillpay+ " is going to buy the meal today!")


# row1 = ["📦","📦","📦"]
# row2 = ["📦","📦","📦"]
# row3 = ["📦","📦","📦"]
# map =[ row1,row2 ,row3]
# print (f"{row1}\n{row2}\n{row3} " )
# position = input("do you want to put the key?")
# column = int(position[0])-1
# row = int(position[1])-1

# print(row)
# treasure = "🔑"
# map[row][column]= treasure
# print (f"{row1}\n{row2}\n{row3} " )


# import random

# rock = "🪨rock"
# paper = "📜paper"
# scissors = "✂️scissors"
# list = [rock,paper,scissors]
# player_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
# if 0 <= int(player_input) <= 2:
#     print("u lost")
#     player_choice = list[int(player_input)]
#     computers_choice = random.choice(list)
#     print(f"u chose \n{player_choice}\ncomputer chose\n{computers_choice}\n")
#     if player_choice == "🪨rock" and computers_choice == "✂️scissors":
#         print("u won")
#     elif player_choice == "✂️scissors" and computers_choice == "📜paper":
#         print("u won")
#     elif player_choice == "📜paper" and computers_choice == "🪨rock":
#         print("u won")
#     elif player_choice == computers_choice :
#         print("draw")
#     else:
#         print("u lost")
# else:
#     print("u lost")


# student_heights = input("lnput a list of student heights").split()
# sum = 0
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     sum += student_heights[n]
# avg = sum/len(student_heights)
# print(round(avg,0))

# student_scores = input("lnput a list of student scores").split()
# max = 0
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#     if student_scores[n] > max:
#         max = student_scores[n]
# print(max)

# add 1 to 100 
# sum = 0
# for n in range(1,101):
#     sum += n
# print(sum)

# add evens 2 to 100 
# sum = 0
# for n in range(2,101,2):
#     sum += n
# print(sum)


# fizzbuzz
# for n in range(1,101):
#     if n%3 == 0 and n%5 == 0:
#         n= "fizzbuzz"
#     elif n%3 == 0:
#         n= "fizz"
#     elif n%5 == 0:
#         n= "buzz"
#     print(n)



# Password Generator 💻
# import random
# import string
# print("Welcome to the Password Generator!")
# # Ask user for input
# letters_count = int(input("How many letters would you like in your password?\n"))
# symbols_count = int(input("How many symbols would you like?\n"))
# numbers_count = int(input("How many numbers would you like?\n"))

# # Create character pools
# letters = list(string.ascii_letters)
# symbols = list("!@#$%^&*()_+{}[];:,.<>?")
# numbers = list(string.digits)

# # Pick random characters
# password_list = []

# for _ in range(letters_count):
#     password_list.append(random.choice(letters))

# for _ in range(symbols_count):
#     password_list.append(random.choice(symbols))

# for _ in range(numbers_count):
#     password_list.append(random.choice(numbers))

# # Shuffle and join
# random.shuffle(password_list)
# password = "".join(password_list)

# print(f"\nYour generated password is: {password}")


# list = "dsfdfs,dgsdgsdg".split(",")
# list = (".").join(list)
# print(list)

# x=1
# for n in range(0,x):        # use this if u wanna do something with the every list or range iteration 
#     print("sjdfsljdfslkf")

# while x<3:
#     print("sjdfsljdfslkf")
#     x+=1
