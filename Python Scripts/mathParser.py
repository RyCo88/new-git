def answer(question):
    question = question.lower().strip('?')
    question = question.replace('multiplied by', 'multiplied').replace('divided by', 'divided')
    words = question.split()
    formula = []
    
    for word in words:
        if word.isnumeric() or (word.startswith('-') and word[1:].isdigit()):
            formula.append(int(word))
        elif word in ['plus','minus','multiplied','divided']:
            formula.append(word)
            
    if len(formula) % 2 == 0 or len(formula) == 0:
        raise ValueError("syntax error")
    
    if len(formula) == 1 and type(formula[0]) == int:
        return formula[0]
    
    item = 1
    answer = formula[0]
    
    while item < len(formula):
        operator = formula[item]
        next = formula[item + 1]
        
        if formula[item] == 'plus':
            answer += next
        elif formula[item] == 'minus':
            answer -= next
        elif formula[item] == 'multiplied':
            answer *= next
        elif formula[item] == 'divided':
            answer = answer // next
        
        item += 2
    
    return answer