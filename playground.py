''' basics '''
a = 7
a += 2 # a = a + 2
a -= 2 # a = a - 2
a *= 2 # a = a * 2
a **= 2 # a = a ** 2
# print(a)

text = "    Here is Playground.     "
text = text.strip()
text = text.lower()
text = text.upper()
text = text.replace('.', '!')
tokens = text.split()
# print(len(tokens))

text += "!@#$%^"
print(text)

b = True
c = False
print(b and c)
print(b or c)
print(not b)

'''data structure'''

# list
l = ['I', 'have', 'an', 'apple']
print(l[1])
print(l[-1])
print(l[1:3])
print(l[1:])
print(l[:-1])

l.append('pineapple')
l.append(1)
print(l)

x = l.pop()
print(x)

'''loop'''
for x in l:
	print(x)

for a in range(3):
	print(a)

for i in range(len(l)):
	print(l[i])

for i, x in enumerate(l):
	print("#" + str(i) + ":")
	print(x)

i = 0
while(i < len(l)):
	print(l[i])
	i += 1

print(l + tokens)
l.extend(tokens)
print(l)

'''list comprehension'''
squares = [x ** 2 for x in range(10)]
print(squares)
even_squares = [x **2 for x in range(10) if x % 2 == 0]
print(even_squares)

'''map'''
m = {}
for i, x in enumerate(l):
	m[i] = x
print(m)

del m[0]
print('I' in m)
print('I' in l)
print(m)

# m[100]
print(m.get(100))
print(m.get(100, 'pen'))

# iterate
for i in m:
	x = m[i]

for i, x in m.items():
	print('#%d' % i)
	print(x)

'''function'''
def my_func(tokens, sep = ','):
	text = sep.join(tokens)
	return text
print(my_func(tokens))
print(my_func(tokens, sep = '!'))

'''read & write'''
f = open('toRead', 'r')
new_m = {}
for line in f.readlines():
	sentence, order = line[:-1].split('.')
	new_m[sentence] = int(order)

w_f = open('toWrite', 'w')
for sentence in sorted(new_m, key = new_m.__getitem__, reverse = True):
	print(new_m[sentence])
	w_f.write(sentence + '\n')