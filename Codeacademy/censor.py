__author__ = 'lyle'

def censor(text,word):
    output = []
    for  words in text.split():
        if words == word:
            output.append(len(words) * "*")
        else:
            output.append(words)
    return  ' '.join(output)
print(censor("this hack is wack hack", "hack"))
