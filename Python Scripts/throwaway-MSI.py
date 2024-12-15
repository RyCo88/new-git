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

def label(colors): #colors will be a list of at least 3 values ['black','red','blue','brown']
    color_code = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    if colors[2] == 'black':
    if colors[2] == 'brown':
    if colors[2] == 'red':
    if colors[2] == 'orange':
    if colors[2] == 'yellow'
    if colors[2] == 'green'
    if colors[2] == 'blue'
    if colors[2] == 'violet'
    if colors[2] == 'grey'
    if colors[2] == 'white'
    '''
question = 'What is 5 plus 4 multiplied by 7 and some other stuff?'
def answer(question):
    operators = ['plus', 'minus', 'multiplied', 'divided']
    numbers ='1234567890'
    question = question.strip('?')
    words = question.split()
    formula = []
    print(words)
    for word in words:
        if word.isnumeric():
            formula.append(int(word))
        elif word in operators:
            if word == 'multiplied' or word == 'divided':
                if words[words.index(word) + 1] == 'by':
                    continue
                else:
                    pass
            formula.append(word)
    if len(formula) % 2 == 0:
        raise Exception("Sorry the formula isn't possible")
    print(formula)
    for word in formula:
        if word == 'multiplied' or word == 'divided':
            if word == 'multiplied':
                print(formula[formula.index(word) - 1] * formula[formula.index(word) + 1])

answer(question)