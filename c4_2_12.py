l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))
        
def sample_func(word):
    return word.capitalize()  #文字列の最初の文字を大文字に

change_words(l, sample_func)