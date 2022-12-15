# Jamie Etienne
# A combination of programming exercises and code
# demonstrated in module resources (along with some other required content)
# in a robust, user-friendly, well documented, well written, cohesive program.

# A print statement without any modifications
print("Hello, Welcome to my integration project")

# A print statement with a comma to create a space
print("Hello, Welcome to my integration project", 1)

# A print statement with a \n to move the rest of the statement to a new line
print("Hello, Welcome to my integration project \nI hope that you enjoy it")

# A print statement that uses + to concatenate two or more strings
print("Hello, Welcome to my integration project" + " " + "I hope that you "
                                                         "enjoy it")

# An input function with a final print function output
color = input("Enter the name of a color: ")
animal = input("Enter the name of an animal: ")
food1 = input("Enter the name of a food: ")
food2 = input("Enter the name of a food: ")
food3 = input("Enter the name os a food: ")
meal = input("Enter either breakfast, lunch, or dinner: ")
print("The " + color + " " + animal + " went to the store to buy "
      + food1 + "," +  "\n" + food2 + " and, " + food3 + " for " + meal + ".")

# A print statement that uses + for mathematical operations: Addition
print("34 + 56 =", 34 + 56)

# A print statement that uses - for mathematical operations: Subtraction
print("34 - 35=", 34 - 56)

# A print statement that uses * for mathematical operations: Multiplication
print("34 * 56 =", 34 * 56)

# A print statement that uses ** for mathematical operations: Exponential
print("34 ** 56 =", 34 ** 56)

# A print statement that uses / for mathematical operations: Division float int
print("34 / 56 =", 34 / 56)

# A print statement that uses // for mathematical operations: Division only
# int no remainder
print("34 // 56 =", 34 // 56)

# A print statement that uses % for mathematical operations:
# Division but only the remainder
print("34 % 56 =", 34 % 56)

# An assignment statement
Name = "Jamie"
print("My name is", Name)

# An assignment program that calculates the cost of a meal.
# It shows knowledge about assignment statements and how to use them
# to do mathematical equations and combine them with Str
# to make a cohesive program
cost_of_hamburger = float(2.00)
cost_of_fries = float(1.50)
cost_of_drinks = float(1.00)
print(" Hai welcome to Sumis Berger's and Satisfries "
      "what can I get for you today")
Str_hamburger = input("How many hamburgers do you want:")
Int_hamburger = float(Str_hamburger)
Final_hamburger = Int_hamburger * cost_of_hamburger
print(Final_hamburger)
Str_fries = input("How many orders of fries do you want:")
Int_fries = float(Str_fries)
Final_fries = Int_fries * cost_of_fries
print(Final_fries)
Str_drinks = input("How many drinks do you want:")
Int_drinks = float(Str_drinks)
Final_drinks = Int_drinks * cost_of_drinks
print(Final_drinks)
Total_cost = Final_hamburger + Final_fries + Final_drinks
print("Your total is ", Total_cost)

# An input and mathematical operation program(number of books by the millions)
numBooks = 6
booksLent = 3
remainingBooks = numBooks - booksLent
print("The number of books remaining is: ", remainingBooks)

# An input and mathematical operation program(number of books by the millions)
# formatted to include decimals
numBooks = 6.745
booksLent = 3.389
remainingBooks = numBooks - booksLent
print("The number of books remaining is: ", format(remainingBooks, '3.7f'))

# A print statement using sep=' '
print("books", "books", "books", sep=' yes ')

# A Boolean Expression: Less Than
boolean1 = 16 < 10
# A Boolean Expression: Greater than
boolean2 = 16 > 10
# A Boolean Expression: Less than and equal to
boolean3 = 16 <= 10
# A Boolean Expression: Greater than and equal to
boolean4 = 16 >= 10
# A Boolean Expression: Equal to
boolean5 = 16 == 10
# A Boolean Expression: Not equal to
boolean6 = 16 != 10

# A boolean expression that tests for the amount of candy eaten
# using an if else statement
candy = int(100)
candyEaten = int(input("How much candy have you eaten:"))
amountLeft = candy - candyEaten
if candyEaten < amountLeft:
    print("Aju Nice")
else:
    print("Naughty Naughty")

# An if/elif statement for comparing sales to bonus
sales = int(input("Enter your sales for the week: "))
if sales >= 100000:
    bonus = 10000
elif sales >= 75000:
    bonus = 5000
elif sales >= 50000:
    bonus = 2500
elif sales >= 25000:
    bonus = 1000
    print('Your bonus is: ', bonus)

# A For loop the print 5 to 500 in increment of 5
for num in range(5, 501):
    if num % 5 == 0:
        print(num)

# a While loop
valid_letter = False
while not valid_letter:
    letter = input("Enter a letter from 'a-z': ")
    if 'a' <= letter <= 'z':
        valid_letter = True
        print("Thank you for your input")
    else:
        print("Sorry, that is not a valid letter. Please try again.")

# A nested if/else command loop using the and boolean
for i in range(3):
    student_id = input("Enter the student's ID: ")
    total_grade = 0
    for j in range(3):
        quiz_grade = float(input("Enter the quiz grade: "))
        total_grade += quiz_grade
    average_grade = total_grade / 3
    print("Student {}: average grade = {:.2f}"
          .format(student_id, average_grade))
    if 70 <= average_grade <= 100:
        print("Congratulation!\nYou pass the class")
    else:
        print("Sorry please they again next year")


# A defined function for multiply
def multiply(x, y):
    return x * y


multDefNum = input("Enter two numbers with a space between them: ")
num1, num2 = multDefNum.split()
multDefnum1 = float(num1)
multDefnum2 = float(num2)
result = multiply(multDefnum1, multDefnum2)
print("The multiplication result is:", result)

#
