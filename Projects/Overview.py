# Print numerele care se impart la 3 din range(1,11)

# str = list(range(0,11,2))
# print(str)

# for num in range(1,50):
#     if num % 3 == 0:
#         print(num)

# Print cuvant care are lungimea para

# st = 'Print every word in this sentence that has an even number of letters'
#
# for wrd in st.split():
#     if len(wrd) % 2 == 0:
#         print(wrd)

# Inlocuieste numerele care sunt divizibile cu 3 si cele cu 5 in fizz respectiv buzz iar daca numerele sunt divizibile
# si cu 3 si cu cinci inlocuieste cu fizzbuzz

# st = list(range(1,100))

# for num in st:
#     if num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     elif num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     else:
#         print(num)

# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one
#  or both numbers are odd


# def less_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a > b:
#             return b
#         else:
#             return a
#     else:
#         if a > b:
#             return a
#         else:
#             return b

# Write a function takes a two-word string and returns True if both words begin with same letter

# def animal_cracker(a,b):
#     if a[0].split() == b[0].split():
#         return True
#     else:
#         return False
#
#
# print(animal_cracker('caine','cou'))

# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

# def makes_twenty(a, b):
#     if a + b == 20 or a == 20 or b == 20:
#         return True
#     else:
#         return False
#
#
# print(makes_twenty(17, 3))

# Write a function that capitalizes the first and fourth letters of a name

# def old_mcdonald(name):
#     first_letter = name[0].upper()
#     forth_letter = name[3].upper()
#
#     print(first_letter + name[slice(1,3)] + forth_letter + name[slice(4,9)])
#
# old_mcdonald('macdonald')

# Given a sentence, return a sentence with the words reversed

# def master_yoda(text):
#     sentance_list = text.split()
#
#     print(f'{sentance_list[-1]} {sentance_list[1]} {sentance_list[0]}')
#
#
# master_yoda('I am home')

# Given an integer n, return True if n is within 10 of either 100 or 200

# def almost_there(n):
#     return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
#
#
# print(almost_there(104))

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def has_33(nums):
#     for i in range(0, len(nums) - 1):
#
#         # nicer looking alternative in commented code
#         # if nums[i] == 3 and nums[i+1] == 3:
#
#         if nums[i:i + 2] == [3, 3]:
#             return True
#
#      return False

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

# def paper_doll(text):
#     new = ''
#     for letter in text:
#         new += letter * 3
#
#     print(new)
#
#
# paper_doll('Hello')

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

# def summer_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total
