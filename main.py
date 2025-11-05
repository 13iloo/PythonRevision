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


# import random
# import string

# letters = list(string.ascii_letters.lower())
# password_list = []
# for _ in range(4):
#     password_list.append(random.choice(letters))

# show_this = []
# print(password_list)
# hidden_word = password_list
# for n in hidden_word:
#     show_this.append("_")

# trials = 6
# i = 6
# # given_word = input("write a letter")

# def check():
#     match = False

#     for n in range(0, len(hidden_word)):
#         if given_word == hidden_word[n]:
#             show_this[n] = hidden_word[n]
#             match = True

#     return match


# while trials >0:
#     given_word = input("write a letter:  ")

#     check()
#     print(check())
#     if check()==False:
#         trials -= 1
#     print(trials)
#     print(" ".join(show_this))
#     if "_" not in show_this:
#         print("You win." )
#         break


# if trials == 0:
#     print("hanged!!")

# Function
# import math
# test_h = int(input("What is the height of the wall?"))
# test_w = int(input("What is the weight of the wall?"))
# coverage = 5

# num_cans = 0

# def paint_calc(height,weight,cover):
#     num_cans  = (height* weight)/cover
#     print(f"You ll need {math.ceil(num_cans)} cans of paint")

# paint_calc(height=test_h,weight=test_w,cover=coverage)


# prime number checker
# num = int(input("insert the number: "))
# def prime_num_checker(num):
#     is_prime = True
#     for i in range(2, num):
#         if num%i == 0:
#             is_prime = False
#     if is_prime:
#         print("Its a prime number")
#     else:
#         print("Its not a prime number")
# prime_num_checker(num)


# Caesar Cipher Part 1 - Encryption

# import string

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print(letters[-26-1])
# # list(string.ascii_letters)

# direction= input("Type 'encode' to encrypt,type 'decode' to decrypt: ")
# text= input("Type your message:")
# shift =int(input("Type the shift number:"))

# def encrypt(text,shift,direction):
#     text_list = list(text)
#     final_encrypted_word = ""
#     for n in text_list:
#         encrypted_word = []
#         position = letters.index(n)
#         new_position = position + shift
#         # while new_position>25:
#         if position <=25:
#             new_position = new_position % 26
#         else:
#             new_position = (new_position % 26) +26
#                 # break
#             # print(new_position)
#         new_letter = letters[new_position]

#         encrypted_word.append(new_letter)
#         final_encrypted_word += "".join(encrypted_word)
#     print(f" the encrypted word is {final_encrypted_word}")
#     return final_encrypted_word


# def decrypt(text,shift,direction):
#     text_list = list(text)

#     final_decrypted_word = ""
#     for n in text_list:
#         decrypted_word = []
#         position = letters.index(n)
#         new_position = position - shift
#         # while new_position>51:
#         if position <=25:
#             new_position = new_position % 26
#         else:
#             new_position = (new_position % 26) +26
#                 # break
#             # print(new_position)
#         new_letter = letters[new_position]

#         decrypted_word.append(new_letter)
#         final_decrypted_word += "".join(decrypted_word)
#     print(f" the decrypted word is {final_decrypted_word}")


# # encrypt(text,shift,direction)
# # decrypt(encrypt(text,shift,direction),shift,direction)


# def caeser(text,shift,direction):
#     final_word = ""
#     text_list = list(text)
#     print(text_list)
#     for n in text_list:
#         transformed_word = []
#         if n in letters:
#             position = letters.index(n)
#             if direction=="decode":
#                 new_position = position - shift
#             else:
#                 new_position = position + shift
#             # while new_position>51:
#             if position <=25:
#                 new_position = new_position % 26
#             else:
#                 new_position = (new_position % 26) +26
#                     # break
#                 # print(new_position)
#             new_letter = letters[new_position]

#             transformed_word.append(new_letter)
#             final_word += "".join(transformed_word)
#         else:
#             new_letter = n

#             transformed_word.append(new_letter)
#             final_word += "".join(transformed_word)
#     print(f" the {direction}d word is :{final_word}")

# caeser(text,shift,direction)


# Dictionaries
# student_scores = {
#     "Harry":81,
#     "Ron":78,
#     "Hermione":99,
#     "Draco":74,
#     "Neville":62,
# }

# for student in student_scores:
#     if student_scores[student]>90:
#         student_scores[student] = "Outstanding"
#     elif student_scores[student]<=90 and student_scores[student] > 80:
#         student_scores[student] = "Exceeds expectation"
#     elif student_scores[student]<=80 and student_scores[student] > 70:
#         student_scores[student] = "Acceptable"
#     elif student_scores[student] < 70:
#         student_scores[student] = "Fail"
# print(student_scores)

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": [
#             "Paris",
#             "lille",
#             "Di jon",
#         ],
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": [
#             "Berlin",
#             "Hamburg",
#             "Stuttgart",
#         ],
#     },
# ]


# def add_new_country(country, visits, cities):
#     new_dict = {"country":country, "visits":visits, "cities":cities}
#     travel_log.append(new_dict)
#     print(travel_log)


# add_new_country("Russia", 2, ["Moscow", "Saint petersburg"])


# # Returns
# def formatter(f_name,l_name):
#     if f_name== "" or l_name == "":
#         return "You didnt provide valid inputs"
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f_name +" "+ l_name

# print(formatter(input("What is your first name?"),input("What is your first name?")))


# capstone project blackjack

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# my_ace = False
# com_ace = False
# ## The cards in the list have equal probability of beiøg drawn.
# ## Cards are not removed from the deck as they are drawn.

# import random


# def play_game():
#     start_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' :  ")
#     # ace = False
#     my_cards = []
#     computers_cards = []
#     com_total = 0
#     my_total = 0

#     if start_play == "y":
#         for card in range(1):
#             computers_cards.append(random.choice(cards))
#         for card in range(2):
#             my_cards.append(random.choice(cards))

#         print(f"\nYour cards: {my_cards}")

#         print(f"Computer's first card: {computers_cards}\n")
#         if sum(my_cards) == 21 and len(my_cards)== 2:
#             print("You win !! BLACK JACK !!")
#             play_game()


#         deal_card = input("Type 'y' to get another card, type 'n' to pass: ")
#         if deal_card == "y":
#             add_all(my_cards, computers_cards,deal_card,my_ace,com_ace)
#         else:
#             add_all(my_cards, computers_cards,deal_card,my_ace,com_ace)


# def check(my_total, com_total):
#     if my_total > 21:
#         print("Bust! You Lost")
#     if com_total > 21:
#         print("You Win")
#     elif my_total > com_total:
#         print("Y0u win")
#     elif my_total == com_total:
#         print("draw")
#     elif my_total < com_total:
#         print("You lost")

# def add_all(my_cards, computers_cards,deal_card,my_ace,com_ace):
#     com_total = 0
#     my_total = 0
#     if deal_card == "y":
#         for card in range(1):
#             computers_cards.append(random.choice(cards))
#             print(f"\n computer final card: {computers_cards}\n")

#         for card in range(1):
#             my_cards.append(random.choice(cards))
#             print(f"\nYour final card: {my_cards}\n")
#     else:
#         while com_total<17 or com_total==21:
        
#             for card in range(1):
#                 computers_cards.append(random.choice(cards))
#                 for card in computers_cards:
#                     if card == 11:
#                         com_ace = True
#                     com_total = sum(computers_cards)

#                 print(f"\n computer final card: {computers_cards}\n")
#     while com_total<17 or com_total==21:
        
#             for card in range(1):
#                 computers_cards.append(random.choice(cards))
#                 for card in computers_cards:
#                     if card == 11:
#                         com_ace = True
#                     com_total = sum(computers_cards)
#                     print(f"\n computer final card: {computers_cards}\n")

#     for card in my_cards:
#         if card == 11:
#             my_ace = True
#         my_total = sum(my_cards)
#     print(f"user: {my_total} vs computer:{com_total}")


#     if com_total > 21 and com_ace == True:
#         com_ace -= 10
#     if my_total > 21 and my_ace == True:
#         my_total -= 10
#         check(my_total, com_total)
#     else:
#         check(my_total, com_total)
#     play_game()

# play_game()



import random
print(
""" 
                                                                                                                         
 ,----.                                      ,--.  ,--.                ,--.  ,--.                  ,--.                  
'  .-./   ,--.,--. ,---.  ,---.  ,---.     ,-'  '-.|  ,---.  ,---.     |  ,'.|  |,--.,--.,--,--,--.|  |-.  ,---. ,--.--. 
|  | .---.|  ||  || .-. :(  .-' (  .-'     '-.  .-'|  .-.  || .-. :    |  |' '  ||  ||  ||        || .-. '| .-. :|  .--' 
'  '--'  |'  ''  '\   --..-'  `).-'  `)      |  |  |  | |  |\   --.    |  | `   |'  ''  '|  |  |  || `-' |\   --.|  |    
 `------'  `----'  `----'`----' `----'       `--'  `--' `--' `----'    `--'  `--' `----' `--`--`--' `---'  `----'`--'    
                                                                                                                          
Welcome to the Number Guessing Game !
I'm thinking of a number between 1 and IØØ.""" 
)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


if difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
    trials_left = 10
else:
    print("You have 5 attempts remaining to guess the number.")
    trials_left = 5

print(trials_left)

generated_num  = random.randint(0,100)

def check(trials_left):
    guessed_num = int(input("Make a guess: "))

    if guessed_num == generated_num:
        print("You win")
        return
    elif guessed_num < generated_num:
        print("too low")
    elif guessed_num > generated_num:
        print("too high")
    trials_left = trials_left - 1
    if trials_left <1:
        print(f"You have lost")
        return
    print(f"You have {trials_left} attempts remaining to guess the number.")
    check(trials_left)

check(trials_left)



