a=b=c = [1,2,3]
print(a,b,c)

print(id(a),id(b),id(c))
b.append(4)
print(a,b,c)
print(id(a),id(b),id(c))


x=10
y=10

print(id(x), id(y))
y=y+1234567890-1234567890
print(id(x), id(y))