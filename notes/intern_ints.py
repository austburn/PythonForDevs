a = 1
b = 1

while a is b:
    a += 1
    b += 1

print a,b
print hex(id(a)), hex(id(b))
