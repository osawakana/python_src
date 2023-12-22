d = {'x':10, 'y':20}
print(d)
print(d.keys())
print(d.values())

d2 = {'x':1000, 'j':500}
d = {'x':10, 'j':20}
print(d2)
d.update(d2)
print(d)
print(d2)

