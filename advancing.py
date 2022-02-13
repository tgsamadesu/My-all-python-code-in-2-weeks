# Calculator :
'''print ("Enter your fisrt num")
n1 = input ()
print ("Enter your second num")
n2 = input ()
print ("Your sum of following number is... ", int (n1) + int (n2))'''
# Dictionary :
'''d1 = {"Manga":"Whimsical-Pictures", "Nani":"What", "Kami":"God", "Nanda":"Why"}
print ("Search meaning for... ")
inp = input ()
print ("Results...")
print (d1[inp])'''
# If-Else-Elif :
'''var1 = 420
var2 = int(input())
if var2>var1:
    print ("Greater")
else:
    print ("Less")'''
'''print ("Enter your age... ")
age = int(input())
if age<7 or age>100:
    print ("Umm... are you serious??")
elif age==18:
    print ("We'll think about it...")
elif age>18:
    print ("Yes you can drive!")'''
# Faulty Calculator:
'''print ("Enter your number")
n1 = input ()
print ("Enter your second number")
n2 = input ()
print ("You've entered a invalid number.", "Please Enter a valid number")'''
# For Loop:
'''lsit1 = ["8000", "5", "90", "2"]
print ("Ask")
inp = input()
if lsit1>6:
    print ("It's a valid number")
else:
    print ("It's a invalid number")'''
'''items1 = [20, 29, 20, 190, 6, 3, 8, 9, 2,]
for item in items1:
    if str(item).isnumeric and item>6:
        print (item)'''
# While loop:
'''i = 0
while(i<45):
    print (i+1)
    i = i + 1 '''
'''print("enter a random number")
c = int(input())
if c>=100:
    print(c, "is valid")
while (c<=100):
    print("Error input another number")
    c = int(input())
    print(c, "is valid")'''
# My First Succsesful Quiz:
'''while (True):
    n1 = int(input))
        print("Enter your number...\n"))
    if n1==100:t ("You have entered a valid number\n")
        break'''
# A fail exercise:
'''n1 = input ("Enter your num..." ,)
n2 = input ("Enter your sec num..." ,) 
print ("Your answer is", int(n1) * int(n2))'''
'''while (True):
    print ("Guess the number. (9 Guesses left")
    inp = input()
    if inp==18:
        print ("You've entered a right number!")
        break
    elif inp>18:
        print ("You've entered the wrong number!")
        continue
    else:
        print ("You have 8 choices ")'''
# A Successful code of someone:
'''n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")'''
# Try except exception handling:
'''print ("Enter you first num")
n1 = input()
print ("Enter your sec num")   
n2 = input ()
try:
    print ("Your sum of these two numbers is",
    int (n1) + int (n2))
except Exception as e:
    print ("Sinjeki no kyojin")'''
# PYTHON FILE IO BASICS (IMPORTANT):
'''r : r mode opens a file for read-only. We do not have permission
 to update or change any data in this mode.
w : w mode does not concern itself with what is
 present in the file. It just opens a file
  for writing and if there is already some
   data present in the file, it overwrites it.
x : x is used to create a new file. It does
 not work for an already existing file, as
  in such cases the operation fails.
a : a stands for append, which means to
 add something to the end of the file. It
  does exactly the same. It just adds the
   data we like in write(w) mode but
   instead of overwriting it just adds
    it to the end of the file. It also
     does not have the permission of reading the file.
t : t mode is used to open our file in text
 mode and only proper text files can be opened
  by it. It deals with the file data as a string.
b : b stands for binary and this mode
 can only open the binary files, that are
  read in bytes. The binary files include
   images, documents, or all other files
    that require specific software to be read.
+ : In plus mode, we can read and write
 a file simultaneously. The mode is mostly
  used in cases where we want to update our file.'''
'''f = open("tg3.txt", "a")
f.write("Pokemon sarre kisne maare?")'''
# Someone's sccessful code:
'''print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()'''
# Reccursions and Iteratives:
'''# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
def factorial_iterative(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120

# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


number = int(input("Enter then number"))
# print("Factorial Using Iterative Method", factorial_iterative(number))
# print("Factorial Using Recursive Method", factorial_recursive(number))
print(fibonacci(number))'''
# BOTCHAT PROGRAM:
'''print ("Do you want to become a programmer?")
n1 = input("Yes or No\n")
if n1 == "Yes":
    print ("Good, Y'know I'm learning programming too!.\n")
elif "No":
    print ("Oh, so bad I was thinking if we could program together...\n")
else:
    ("You should, it's fun!\n")'''




    
   
        
    