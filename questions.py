# Write a function that takes a list of numbers and returns their sum.

# while True:
#     numbers = input("Enter a list of numbers to add: ")
#     def sum_of_numbers(numbers):
#         return sum(numbers)

#     numbers = list(map(int, numbers.split()))
#     print("The sum is:", sum_of_numbers(numbers))






# Write a function that finds the largest number in a list.

# while True:
#         numbers = input("Enter a list of numbers to find the largest: ")
#         def largest_number(numbers):
#             return max(numbers)

#         numbers = list(map(int, numbers.split()))
#         print("The largest number is:", largest_number(numbers))







# Implement a function that returns a new list with the items in reverse order

# while True:
#     numbers = input("Enter the number to get in reverse manner :")
#     def reverse_numbers(numbers):
#         return numbers[::-1]
    
#     numbers = list(map(int, numbers.split()))
#     print("the reverse number will be :", reverse_numbers(numbers))






# Write a function that receives a list of numbers and prints "Even" for even numbers and "Odd" for odd numbers.

# while True:
#     numbers = input("Enter a list of numbers to check if they are even or odd: ")
    
#     def even_odd(numbers):
#         for number in numbers:
#             if number % 2 == 0:
#                 print(f"{number} is Even")
#             else:
#                 print(f"{number} is Odd")

#     numbers = list(map(int, numbers.split()))
#     even_odd(numbers)







# Create a function that counts the number of vowels in a given string.

# while True:
#     words = input("enter the words to count the vowels inside it :")

#     def count_vowels(words):
#         count = 0
#         for word in words:
#             if word in "aeiouAEIOU":
#                 count += 1
#         return count
#     print("The number of vowels is:", count_vowels(words))






# Write a function that checks if a given number is prime.

# while True :
#     numbers = input("Enter a number to check if it is prime: ")
#     def prime_number(numbers):
#         if numbers < 2:
#             return False
#         for i in range(2, numbers):
#             if numbers % i == 0:
#                 return False
#         return True
#     print("Is the number prime?", prime_number(int(numbers)))