
from Calculator import Calculator


if __name__ == "__main__":

    calc = Calculator()
    switcher = {
          1: 'addition',
          2: 'subtraction',
          3: 'mul',
          4: 'div'
        }

   

    print('''Operation to perform
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division ''')

    # Take input from user
    choice = int(input("Select operation from 1,2,3,4 : "))
    operation = getattr(calc, choice)
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = operation(a, b)  
    print ("Your result is...",result)