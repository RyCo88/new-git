#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places
time_traveled1 = int(input())
time_traveled2 = int(input())
time_traveled3 = int(input())

total_miles_traveled = (time_traveled1 * 15.62) + (time_traveled2 * 41.85) + (time_traveled3 * 32.67)

print(f'Distance: {total_miles_traveled:.2f} miles')

#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces
ounces = int(input())

tons = ounces // (16 * 2000)
ounces = ounces % (tons * (16 * 2000))
pounds = ounces // 16
ounces = ounces % (pounds * 16)

print(f'Tons: {tons}\nPounds: {pounds}\nOunces: {ounces}')

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value
index = int(input())
data_type = type(various_data_types[index]).__name__

print(f'Element {index}: {data_type}')

#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height 
#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h
b1 = int(input())
b2 = int(input())
height = int(input())
area = ((b1 + b2) / 2) * height

print(f'Trapezoid area: {area} square meters')

#solution accepts five integer inputs
#solution outputs three sums of input values; convert before calculating sum
#first output: sum of five inputs maintained as integer values
#second output: sum of five inputs converted to float values
#third output: sum of five inputs converted to string values (concatenate)
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

int_sum = num1 + num2 + num3 + num4 + num5
float_sum = float(num1) + float(num2) + float(num3) + float(num4) + float(num5)
string_con = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

print(f'Integer: {int_sum}\nFloat: {float_sum}\nString: {string_con}')

#hint: modulo (%) and floored division (//) may be used
#solution accepts a 9-digit integer representing an unformatted student identification number (i.e.,"5417543010")
#solution outputs formatted student identification number as a string (i.e.,"541-75-3010")
number = int(input())

first_3 = number // 1000000
mid_2 = (number // 10000) % 100
last_4 = number % 10000

print(f'{first_3}-{mid_2}-{last_4}')

predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is greater than the maximum value when compared to predef_list
check = int(input())
t_or_f = check > max(predef_list)

print(f'Greater Than Max? {t_or_f}')

#temperature >= 212, water state is "Boiling"
#temperature (115, 211], water state is "Hot"
#temperature [80, 115], water state is "Warm"
#temperature [33, 80), water state is "Cold"
#temperature < 33, water state is "Frozen"
#temperature = 212, safety comment "Caution: Hot!"
#temperature < 33, safety comment "Watch out for ice!"
#solution accepts integer input representing a water temperature
#solution outputs the water state and potential safety comment based on temperature
temperature = int(input())

if temperature >= 212:
    print("Boiling")
    if temperature == 212:
        print("Caution: Hot!")
elif temperature >= 115 and temperature <= 211:
    print("Hot")
elif temperature >= 80 and temperature <= 114:
    print("Warm")
elif temperature >= 33 and temperature <= 79:
    print("Cold")
else:
    print("Frozen")
    print("Watch out for ice!")

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input
index = int(input())

try:
    print(frameworks[index])
except:
    print("Error")

stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places
num_stocks = int(input())
total = 0

for i in range(num_stocks):
    total += stocks[input()]
    
print(f'Total price: ${total:.2f}')

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

item = input()
num_items = int(input())

if num_items >= 21:
    total = (purchase[item] * num_items) * 0.9
elif num_items >= 10 and num_items <= 20:
    total = (purchase[item] * num_items) * 0.95
else:
    total = purchase[item] * num_items


print(f'{item} ${total:.2f}')

#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence
filename = input()

with open(filename, 'r') as myfile:
    content = [word.strip() for word in myfile]
    
with open('newfile.txt', 'w') as newfile:
    for i in content:
        newfile.write(i + '\n')
    newfile.write(' '.join(content))
    
with open('newfile.txt', 'r') as new:
    print(new.read())

#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file (i.e., "input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements
import csv

filename = input()

with open(filename, 'r') as myfile:
    reader = csv.reader(myfile)
    for line in reader:
        file_dict = {}
        for item in range(0, len(line), 2):
            key = line[item]
            key = key.strip()
            value = line[item + 1]
            value = value.strip()
            file_dict[key] = value
        print(file_dict)

#import math module and call factorial()
#solution accepts integer input
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is >100
import math

number = int(input())
fact = math.factorial(number)
big_facts = fact > 100

print(fact)
print(big_facts)

#import pigAge module and call pigAge_converter()
#one pig year is equivalent to five human years
#solution accepts integer input representing a pig's age
#solution outputs the human equivalent age for a pig (i.e. "8 is 40 in human years")
'''import pigAge
age = int(input())
pig_age = pigAge.pigAge_converter(age)

print(f'{age} is {pig_age} in human years')'''


#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces
ounces = int(input())


tons = (ounces / 16) // 2000
pounds = ounces / 16
pounds = pounds % 2000
ounces = (pounds - int(pounds)) * 16


print(f'Tons: {int(tons)}\nPounds: {int(pounds)}\nOunces: {int(ounces)}')