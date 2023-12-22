def say_something(word, *fumi):
    print('word =', word)
    for arg in fumi:
        print(arg)
        
say_something('ねこ', 'ひげ', 'おみみ')