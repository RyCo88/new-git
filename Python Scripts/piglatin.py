def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    piggy = ''
    letters = ''
    words = text.split()
    for i in words:
        if i[:2] == 'xr' or i[:2] == 'yt':
            return text + 'ay'
        if text[0] in vowels:
            return text + 'ay'
        if text[0] == 'y':
            return text[1:] + 'yay'
        if text[0] not in vowels and 'y' in text:
            i = 0
            while text[i] != 'y':
                if text[i] in vowels:
                    return text[len(letters):] + letters + 'ay'                
                else:
                    letters += text[i]
                    i += 1
            return text[len(letters):] + letters + 'ay'
        if text[0] not in vowels and 'qu' in text:
            i = 0
            while letters.endswith('qu') == False:
                letters += text[i]
                i += 1
            return text[len(letters):] + letters + 'ay'
        if text[0] not in vowels:
            i = 0
            while text[i] not in vowels:
                letters += text[i]
                i += 1
            return text[len(letters):] + letters + 'ay'