
from calculator import Calculator

if _name_ == "__main__":
    
switcher = {
    1: addition,
    2: subtraction,
    3: mul,
    4: division,
    5: module
}
def switch(operation, a, b):
  return switcher.get(operation, default)(a, b)

print('''Operation to perform
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Module ''')

# Take input from user
choice = int(input("Select operation from 1,2,3,4 : "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print (switch(choice, a, b))