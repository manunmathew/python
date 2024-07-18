# write a program to print "Hello World" if the user input 10

num = int(input("Enter the number: "))
if (num==10):
   print("Hello World")


# Print welcome if user input number in the range 1 and 10
num = int(input("Enter the number: "))
if (num >= 1 and num <= 10):
    print("Welcome")

# Write a program to print Welcome if user input any number 100

num = int(input("Enter the number: "))
if (num != 100):
   print("Welcome")
take alphabet from user and it should print vowel if the user input a,e,i,o,u

a = input("Enter the alphabet: ")
vowel = ['a', 'e' , 'i', 'o', 'u']
if (a in vowel):
   print("Vowel")

