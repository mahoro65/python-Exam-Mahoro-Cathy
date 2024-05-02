

'A(1(i))'

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "Fail"

def main():
    try:
        percentage = float(input("Enter the student's percentage score: "))
        if 0 <= percentage <= 100:
            grade = calculate_grade(percentage)
            print("Grade:", grade)
        else:
            print("Percentage should be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()



'(ii)'
# Formula F = (9/5C+32)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

def main():
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Temperature in Celsius:", celsius)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()





'b(i)'
def calculate_area(base, height):
    return 0.5 * base * height

def main():
   
    base = 2
    height = 3

    
    area = calculate_area(base, height)
    



'b(ii)'
# sample_list=(9,2,3,5,8)
def sum_list_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = [9, 2, 3, 5, 8]
print("Sum of numbers in the list:", sum_list_numbers(sample_list))
