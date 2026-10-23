-------------------- Input a student's name and age. Output them on one line as Name: Ali, Age: 17------------------------- 

Name = input("Name: ")
Age = int(input("Age: "))
print(f"Name: {Name}, Age: {Age}")
-------------------- Input a quantity (INTEGER) and a unit price (REAL). Output the total cost rounded to 2 decimal places as Total cost: 7.47-----------------

quantity = int(input("Quantity: "))
price = float(input("Unit price: "))
print("Total cost:", round(quantity*price, 2))
--------------------#Input two positive integers. Output the result of the first DIV the second, then the first MOD the second, on two lines---------------------

Num1=int(input("Num1: "))
Num2=int(input("Num2: "))
print(Num1 // Num2)
print(Num1 % Num2)
-----------------#Input a string of digits. Output its LENGTH, then the number it represents plus 1-------------------

digits = input()
print(len(digits))
print(int(digits) + 1)
---------------#Input Y or N for whether a book is on loan. Store it as a BOOLEAN OnLoan and output the BOOLEAN-----------------------
answer = input("On loan (Y/N): ")
OnLoan = answer == "Y"
print(OnLoan)












