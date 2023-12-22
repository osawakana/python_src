def sample_func(x, l=[]):
    l.append(x)   #.append>リストの最後に要素を追加する
    return l

y = [1, 2, 3]
r = sample_func(100, y)
print(r)

y = [1, 2, 3]
r = sample_func(200, y)
print(r)