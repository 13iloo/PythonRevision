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


