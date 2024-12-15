def answer(question):
    question = question.lower().strip('?')
    question = question.replace('multiplied by', 'multiplied').replace('divided by', 'divided')
    words = question.split()
    formula = []

    # Parsing the question
    for word in words:
        if word.isnumeric() or (word.startswith('-') and word[1:].isdigit()):
            formula.append(int(word))
        elif word in ['plus', 'minus', 'multiplied', 'divided']:
            formula.append(word)
        else:
            # Raise an error for unsupported operations or non-math questions
            raise ValueError("unknown operation")
            
    # Validation of formula length
    if len(formula) % 2 == 0 or len(formula) == 0:
        raise ValueError("syntax error")
    
    # If there's only one number, return it
    if len(formula) == 1 and isinstance(formula[0], int):
        return formula[0]
    
    answer = formula[0]
    item = 1
    
    while item < len(formula):
        operator = formula[item]
        next_number = formula[item + 1]
        
        if operator == 'plus':
            answer += next_number
        elif operator == 'minus':
            answer -= next_number
        elif operator == 'multiplied':
            answer *= next_number
        elif operator == 'divided':
            if next_number == 0:
                raise ValueError("Division by zero is not allowed")
            answer //= next_number
        
        item += 2
    
    return answer

# Example test cases to validate the code
try:
    print(answer("What is 5 plus 5?"))  # Should output 10
    print(answer("What is 52 cubed?"))  # Should raise ValueError("unknown operation")
except ValueError as e:
    print(e)

try:
    print(answer("Who is the President of the United States?"))  # Should raise ValueError("unknown operation")
except ValueError as e:
    print(e)

try:
    print(answer("What is 1 2 plus?"))  # Should raise ValueError("syntax error")
except ValueError as e:
    print(e)

try:
    print(answer("What is plus 1 2?"))  # Should raise ValueError("syntax error")
except ValueError as e:
    print(e)
