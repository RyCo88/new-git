'''#def to_alternating_case(string):
stringlist = list("Should 123Work for fixed tests (provided in the description)")
alt = []
for i in stringlist:
    if i.isupper() == True:
        alt.append(i.lower())
    elif i.isupper() != True:
        alt.append(i.upper())
    else:
        pass
print(''.join(alt))

numbers = list(str(162))
print(numbers)

def is_armstrong_number(number):
    numbers = [int(digit) for digit in str(number)]
    x = len(numbers)
    armposs = 0
    if sum(numbers) == number:
        for i in numbers:
            armposs += i ** x
        return armposs
    else:
        return False

is_armstrong_number(9)

aaa = "Okay if like my  spacebar  quite a bit?   ".split()
print(aaa)

values = {'J' : 10, 'Q' : 10, 'K': 10, 'A' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10}

first = values['J']
second = values['Q']
dealt_total = first + second
print(dealt_total)

word = 'happiness'
print(word[-5])
print(word[:-5] + 'y')
print(word[:-4])
def is_valid(isbn):
    number = []
    if isbn == '':
        return False
    if isbn[-1].lower() == 'x':
        for i in isbn:
            if i.isdigit():
                number.append(int(i))
        number.append(10)
        if len(number) == 10:
            return (number[0] * 10 + number[1] * 9 + number[2] * 8 + number[3] * 7 + number[4] * 6 + number[5] * 5 + number[6] * 4 + number[7] * 3 + number[8] * 2 + number[9] * 1) % 11 == 0
    for i in isbn:
        if i.isdigit():
            number.append(int(i))
        if len(number) != 10:
            return False
        if len(number) == 10:
            return (number[0] * 10 + number[1] * 9 + number[2] * 8 + number[3] * 7 + number[4] * 6 + number[5] * 5 + number[6] * 4 + number[7] * 3 + number[8] * 2 + number[9] * 1) % 11 == 0
        

def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    total = 0
    for i in range(10):
        if isbn[i].isdigit():
            total += int(isbn[i]) * (10-i)
        elif i == 9 and isbn[i] == 'X':
            total += 10
        else:
            return False
    return total % 11 == 0

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):

    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    if ticket_type == 2:
        normal_queue.append(person_name)
        return normal_queue
    
print(add_me_to_the_queue(['a','b','c'],['d','e','f'], 1, 'Eli'))

def label(colors):
    color_code = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    if colors[2] == 'black':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + ' ohms'
    if colors[2] == 'brown':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + '0 ohms'
    if colors[2] == 'red':
        resist_number = str(color_code.index(colors[0]))
        return str(int(resist_number)) + ' kiloohms'
    if colors[2] == 'orange':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + ' kiloohms'
    if colors[2] == 'yellow':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + '0 kiloohms'
    if colors[2] == 'green':
        resist_number = str(color_code.index(colors[0]))
        return str(int(resist_number)) + ' megaohms'
    if colors[2] == 'blue':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + ' megaohms'
    if colors[2] == 'violet':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + '0 megaohms'
    if colors[2] == 'grey':
        resist_number = str(color_code.index(colors[0]))
        return str(int(resist_number)) + ' gigaohms'
    if colors[2] == 'white':
        resist_number = str(color_code.index(colors[0])) + str(color_code.index(colors[1]))
        return str(int(resist_number)) + ' gigaohms

def is_paired(input_string):
    string_letter = 0
    while string_letter < len(input_string):
        if input_string[string_letter] == '[' or input_string[string_letter] == '(' or input_string[string_letter] == '{':
            for letter in input_string[string_letter:]:
                if letter == ']' or letter == ')' or letter == '}':
                    continue
                return False
        string_letter += 1
    return True

def is_paired(input_string):
    string_char = 0
    while string_char < len(input_string):
        if input_string[string_char] == '(':
            for char in input_string[string_char:]:
                if char == ')':
                    continue
                return False
        if input_string[string_char] == '[':
            for char in input_string[string_char:]:
                if char == ']':
                    continue
                return False
        if input_string[string_char] == '{':
            for char in input_string[string_char:]:
                if char == '}':
                    continue
                return False
        string_char += 1

def is_paired(input_string):
    if input_string.count('(') == input_string.count(')') and input_string.count('[') == input_string.count(']') and input_string.count('{') == input_string.count('}'):
        input_char = 0
        while input_char < len(input_string):
            if input_string[input_char] == '(':
                if ')' in input_string[input_char:]:
                    return True
            if input_string[input_char] == '[':
                if ']' in input_string[input_char:]:
                    return True
            if input_string[input_char] == '{':
                if '}' in input_string[input_char:]:
                    return True
            input_char += 1
        return True
    return False'''

software_engineering = ['Introduction to IT',
                        'American Politics and the US Constitution',
                        'Introduction to Physical and Human Geography',
                        'Natural Science Lab',
                        'Web Development Foundations',
                        'Technical Communication',
                        'Health, Fitness, and Wellness',
                        'Network and Security - Foundations',
                        'Data Management - Foundations',
                        'Composition: Successful Self-Expression',
                        'Hardware and Operating Systems Essentials',
                        'Data Management - Applications',
                        'Introduction to Systems Thinking',
                        'Version Control',
                        'Cloud Foundations',
                        'Scripting and Programming - Foundations',
                        'Applied Probability and Statistics',
                        'Business of IT - Project Management',
                        'Applied Algebra',
                        'Introduction to Programming in Python',
                        'Ethics in Technology',
                        'Business of IT - Applications',
                        'Data Structures and Algorithms 1',
                        'IT Leadership Foundations',
                        'Front-End Web Development',
                        'JavaScript Programming',
                        'Software Engineering',
                        'Java Fundamentals',
                        'Java Frameworks',
                        'User Interface Design',
                        'User Experience Design',
                        'Back-End Programming',
                        'Advanced Java',
                        'Software Design and Quality Assurance',
                        'Advanced Data Management',
                        'Software Security and Testing',
                        'Mobile Application Development(Adroid)',
                        'Software Engineering Capstone',]
computer_science = ['Introduction to IT',
                    'Applied Probability and Statistics',
                    'Network and Security - Foundations',
                    'Scripting and Programming - Foundations',
                    'Data Management - Foundations',
                    'Web Development Foundations',
                    'Calculus 1',
                    'Scripting and Programming - Applications',
                    'Introduction to Physical and Human Geography',
                    'Health, Fitness, and Wellness',
                    'Discrete Mathematics 1',
                    'Version Control',
                    'Discrete Mathematics 2',
                    'Introduction to Communication: Connecting with Others',
                    'Computer Architecture',
                    'Composition: Successful Self-Expression',
                    'Data Management - Applications',
                    'American Politics and the US Constitution',
                    'Global Arts and Humanities',
                    'Java Frameworks',
                    'Data Structures and Algorithms 1',
                    'Back-End Programming',
                    'Linux Foundations',
                    'Advanced Java',
                    'Ethics in Technology',
                    'Fundamentals of Information Security',
                    'Operating Systems for Programmers',
                    'Data Structures and Algorithms 2',
                    'Natural Science Lab',
                    'Business of IT - Applications',
                    'Software Engineering',
                    'Advanced Data Management',
                    'IT Leadership Foundations',
                    'Technical Communication',
                    'Introduction to Artificial Intelligence',
                    'Software Design and Quality Assurance',
                    'Computer Science Capstone',
                    'Java Fundamentals']

not_in_software_engineering = []
not_in_computer_science = []
both = []
for course in computer_science:
    if course not in software_engineering:
        not_in_software_engineering.append(course)
for course in software_engineering:
    if course not in computer_science:
        not_in_computer_science.append(course)
for course in computer_science:
    if course in software_engineering:
        both.append(course)
print(len(not_in_computer_science))
print(len(not_in_software_engineering))
print(len(both))
print(not_in_computer_science)
print(not_in_software_engineering)
print(both)