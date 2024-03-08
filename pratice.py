
#Write a Python program to find the sum of all elements in an list.

# listOfElement = [1,2,3,4,5,6,7,8,9,10]
# sumOfEl = 0
# length = len(listOfElement)
# for i in range(length+1):
#     sumOfEl = sumOfEl+listOfElement[i]
# print(sumOfEl)


# listOfElementSecond = [6,7,8,9,10]
# sumOfElement =sum(listOfElementSecond)
# print(sumOfElement)

# #Given an array, find the maximum element in it.

# listOfElement = [1,2,3,4,5,6,7,8,9,10,11]

# #1st way iterable way
# maxEle = listOfElement[0]
# for i in range(len(listOfElement)):
#     if maxEle > listOfElement[i]:
#              maxEle = maxEle[i]
#     else : 
#        maxEle = listOfElement[i]
# print(maxEle)
# #2nd optimize way
# maximumElement = max(listOfElement)
# print(maximumElement)

#Rotate an array to the right by a given number of steps. For example, if the array is [1, 2, 3, 4, 5] and the rotation step is 2, the output should be [4, 5, 1, 2, 3].

# listOfElement = [1,2,3,4,5]
# breakPoint  =2
# newArr  = []

# for i in range(len(listOfElement)-breakPoint,len(listOfElement)):
#     newArr.append(listOfElement[i])


# for j in range(len(listOfElement)-breakPoint):
#     newArr.append(listOfElement[j])
# print(newArr)

# Perform the following operations on a list:


# listEle =  [1,3,5,6,7]

# # Append an element to the end of the list.
# listEle.append(10)
# print(listEle)
# # Insert an element at a specific position.
# listEle.insert(2,12)
# print(listEle)
# # Remove an element from the list.
# listEle.remove(10)
# print(listEle)
# # Check if a specific element is present in the list.
# num = 1
# number = num in listEle
# print(number)


#Find the intersection of two arrays. Intersection is the common elements that exist in both arrays.

# arrOne = [1,2,3,4,5,6]
# arrTwo = [7,8,9,10,12,6]
# for i in range(len(arrOne)):
#     if arrOne[i] : 
#         for j in range(len(arrTwo)):
#             if arrTwo[j]==arrOne[i]:
            
#                  print(arrTwo[j])


#Write a Python program to remove duplicates from a list.

# duplicatesArray  = [1,2,3,4,3,2,6,5]

# #1st optimize code
# noDuplicateEle = list(set(duplicatesArray))
# print(noDuplicateEle)

# #2nd way 
# uniqueEl = []

# for i in duplicatesArray:
#     if i not in uniqueEl:
#          uniqueEl.append(i)
# print(uniqueEl)    

#Given a list containing n distinct numbers taken from the range 0 to n, find the one missing number. (Hint: Consider the sum of the first n natural numbers)
# 

# sumList = [1,2,3,4,6,7,8]
# n = len(sumList)

# sum_of_natural_number =(n+1)*((n+1)+1)//2
# print(sum_of_natural_number)
# sum_inital = 0
# for i in sumList:
#      sum_inital = sum_inital+i
# print(sum_inital)  

# missingNumber  = sum_of_natural_number-sum_inital
# print(missingNumber)


#Given an array of integers, find the maximum product of two distinct integers in the array.


#1st approach
# max_product = float('-inf')
# product_of_two_number = 0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#      product_of_two_number  = arr[i]*arr[j]
#      if(product_of_two_number > max_product):
#         max_product = product_of_two_number
# print(max_product)

#2nd approach
# arr = [1,2,3,4,5,6]
# arr.sort()
# print(arr)

# largestNumber = arr[-2:]
# smallestNumber = arr[:2]

# product_of_two_number =max( largestNumber[0]*largestNumber[1],smallestNumber[0]*smallestNumber[1])

# print(product_of_two_number)
#3rd approach

# arr = [1,2,3,4,5,6]
# sortedArr=sorted(arr)
# print(sortedArr)

# largestNumber = sortedArr[-2:]
# smallestNumber = sortedArr[:2]

# product_of_two_number =max( largestNumber[0]*largestNumber[1],smallestNumber[0]*smallestNumber[1])
# print(product_of_two_number)

#Given an array of integers, move all the zeroes to the end of the array without changing the order of non-zero elements.

# list_of_ele = [1, 0, 3, 0, 5, 8, 0, 2]
# n = len(list_of_ele)
# non_zero_elements = [ele for ele in list_of_ele if ele != 0]
# print(non_zero_elements)
# number_of_zeros = n - len(non_zero_elements)
# print(number_of_zeros)

# new_list = non_zero_elements + [0] * number_of_zeros
# print(new_list)

# arr = [15, 2, 45, 12, 7]
# n = len(arr)

# for i in range(1,n+1):
#     if(arr[i-1]==i):
#         print(arr[i-1]) 

#Write a function to generate the first n rows of Pascal's Triangle. Each number in the triangle is the sum of the two directly above it.

# def generate_pascals_triangle(n):
#     triangle = []

#     for i in range(n):
#         row = [1] * (i + 1)
#         for j in range(1, i):
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#         triangle.append(row)

#     return triangle

# # Example: Generate the first 5 rows of Pascal's Triangle
# result = generate_pascals_triangle(5)
# for row in result:
#     print(row)

#Write a Python program that takes a sentence as input and counts the number of vowels (a, e, i, o, u) in it.

# def countVowels(str):
#     vowels = 'aeiou'
#     count = 0
#     for i in range(len(str)):
#          if (str[i]==vowels[i]):
#                count = count+1
#     return  count    


# print(countVowels("aeiou"))

# #Write a Python program that finds the largest and smallest elements in a given list of numbers.

# listNumbers = [1,2,3,4,5,6,4,8,7,19]

# #to smallest numbers 1st way
# smallestNumbers = min(listNumbers)
# print(smallestNumbers)

# #to smallest numbers 2nd way

# minimum = float('inf')

# for num in listNumbers:
#     if num < minimum:
#         minimum = num

# print(minimum)

# #1st way to find the max numbers

# largestNumbers = max(listNumbers)
# print(largestNumbers)

# #2nd way to find the max numbers
# maximum = float('-inf')
# for i in listNumbers:
#     if num > maximum:
#       maximum = num
# print(maximum)


#Write a Python function that checks if a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward.


# def isPalindromeOrNot(str):
#     reverseString  = str[::-1]
#     if(str==reverseString):
#         print("The string is palindrome")
#     else:
#         print("The given string is not Palindrome")    

# isPalindromeOrNot("abbcbba")      

# Write a Python program that takes a string as input and prints its reverse.  

# def reversString(str):
#      string = str[::-1]
#      return string

# print(reversString("canal"))

# # Write a Python program that takes an integer as input and calculates the sum of its digits.



# def sumOfNanurel():
#     numb = int(input("Enter number = "))
#     naturelSum = (numb)*(numb+1)//2
#     return naturelSum

# print(sumOfNanurel())

# or
# def sum_of_digits(n):
#     # Initialize sum
#     digit_sum = 0
    
#     # Extract digits and add them to sum
#     while n > 0:
#         digit_sum += n % 10
#         n //= 10
    
#     return digit_sum

# # Test the function
# num = int(input("Enter a number: "))
# print("Sum of digits:", sum_of_digits(num))


# Write a Python program to calculate the factorial of a non-negative integer entered by the user.

# def fact(n):
#   fact=1
#   for i in range(1,n+1):
#       fact *=i
#   return fact   
  


# num  = int(input("Enter number = "))
# print(fact(num))

# def fact(n):
#     if n==1:
#       return 1
    
#     factorial  = n * fact(n-1)
#     return factorial

# print(fact(5))


#Write a Python program that takes a sentence as input and counts the number of words in it.


# def countWordNumber(str):
#     count = 0
#     n =len(str)
#     for i in range(0,n):
#         count = count+1
#     return count


# string = input("Entre name = ")
# print(countWordNumber(string))        
             
 
# def countWordNumber(str):
#     count = 0
#     n = len(str)
#     for i in range(0,n):
#        if str[i]==" ":
#            if str[i+1]==" ":
#               continue
#            else :
#               count = count + 1
#     return count+1  
# inp = input("Enter one sentence = ")
# print(countWordNumber(inp))



# 28/02/24

# Write a Python program that takes a string as input and counts the number of vowels and consonants in it.

# def count_vowels_and_consonants(string):
#     vowels_str = "aeiouAEIOU"
#     vowels_count = 0
#     consonants_count = 0
    
#     for char in string:
     
#         if char.isalpha():
        
#             if char in vowels_str:
#                 vowels_count += 1
#             else:
#                 consonants_count += 1
    
#     return vowels_count, consonants_count

# # Input from user
# input_string = input("Enter a string: ")
# vowels, consonants = count_vowels_and_consonants(input_string)
# print("Number of vowels:", vowels)
# print("Number of consonants:", consonants)


#Write a Python program that checks if a given year is a leap year or not.

# def checkIsYearLeapOrNot(year):
#     if( year%4==0 and year%100!=0)  or ( year%400==0):
#         print("year is leap year")
#     else:
#         print("year is not leap year")


# checkIsYearLeapOrNot(2024)

# Write a Python program to find the second largest element in a given list of integers.

# def largestNumber(ls):
#     maxNum = 0
#     for i in range(0,len(ls)):
#         if(ls[i]>maxNum):
#             maxNum=ls[i]
            
#     return maxNum

# print(largestNumber([1,2,3,4,5,10]))

# def maxNum(l):
#    maxNum = max(l)
#    l.remove(maxNum)

#    secondMax = max(l)

#    return secondMax

# print(maxNum([1,2,3,4,5,6,7,8,9,7,50,45]))



#  Write a Python program that takes a list as input and reverses it without using any built-in functions or methods.


# def reverse_list(lst):
#     return lst[::-1]

# # Test the function
# original_list = [1, 2, 3, 4, 5]
# reversed_list = reverse_list(original_list)
# print("Original List:", original_list)
# print("Reversed List:", reversed_list)


#Write a Python function that takes two strings as input and checks if they are anagrams of each other. Anagrams are words or phrases formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# def is_anagram(str1, str2):
   
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
    
  
#     return sorted(str1) == sorted(str2)

# # Test the function
# string1 = "listen"
# string2 = "silent"
# if is_anagram(string1, string2):
#     print(f"'{string1}' and '{string2}' are anagrams.")
# else:
#     print(f"'{string1}' and '{string2}' are not anagrams.")


#Write a Python function that takes a list of integers from 1 to n (inclusive) with one missing number and returns the missing number.

# def missingNumber(lst):
#     n = len(lst) + 1
#     missingNumberFormula = n * (n + 1) // 2
#     sumList = sum(lst)
#     return missingNumberFormula - sumList

# # Input list from user
# listOfNumbers = list(map(int, input("Enter list (space-separated numbers): ").split()))

# print("Missing number:", missingNumber(listOfNumbers))


#Write a Python program that takes a list as input and removes all duplicates, preserving the original order of elements.

# def removeDuplicate(lst):
#     removeNum = set(lst)
#     return removeNum
# listOfNumbers = list(map(int, input("Enter list (space-separated numbers): ").split()))
# print("new number:", removeDuplicate(listOfNumbers))

#  Write a Python program that takes a string as input and reverses the order of words in it. For example, if the input string is "hello world", the output should be "world hello".

# def reverseString(string):
#      splitStr = string.split()
#      reversedWord = splitStr[::-1]
#      reversStr = " ".join(reversedWord)
#      return reversStr
# inputStr = input("Enter string here = ")

# print(reverseString(inputStr))

# Write a Python function that takes two integers as input, base and exponent, and calculates the power of the base raised to the exponent.

def expo(base, expo):
    return base ** expo


baseValue = int(input("Enter base value =  "))
expoValue = int(input("Enter Exponent value = "))

print(expo(baseValue,expoValue))