# A VERY Brief Python Tutorial for EECS 486
## [Hengjia Zhang](www.blythez.com)
 /The aim of this tutorial is to let students quickly get familiar with Python for EECS 486 course works. [Kite](kite.com) is suggested./
## Basics
```python
a = 7
a += 2 # a = a + 2
a -= 2 # a = a - 2
a *= 2 # a = a * 2
a **= 2 # a = a ** 2

text = "    Here is Playground.     "
text = text.strip() # "Here is Playground."
text = text.lower() # "here is playground."
text = text.upper() # "HERE IS PLAYGROUND."
text = text.replace('.', '!') # "HERE IS PLAYGROUND!"
tokens = text.split()
# ['HERE', 'IS', 'PLAYGROUND!']

text += "!@#$%^"  # "HERE IS PLAYGROUND!!@#$%^"

b = True
c = False
print(b and c) #False
print(b or c) #True
print(not b) #False
```

## List
```python
l = ['I', 'have', 'an', 'apple']
print(l[1]) # 'have'
print(l[-1]) # 'apple'
print(l[1:3]) # ['have', 'an']
print(l[1:]) # ['have', 'an', 'apple']
print(l[:-1]) # ['I', 'have', 'an']

len(l) # 4
l.append('pineapple')
l.append(1)
print(l) # ['I', 'have', 'an', 'apple', 'pineapple', 1]
x = l.pop()
print(x) # 1

print(l + tokens) 
# ['I', 'have', 'an', 'apple', 'pineapple', 'HERE', 'IS', 'PLAYGROUND!']
# l.extend(tokens)
```

### Loop
```python
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
```

## List Comprehension
```python
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x **2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

## Map
```python
m = {}
for i, x in enumerate(l):
	m[i] = x
# {0: 'I', 1: 'have', 2: 'an', 3: 'apple', 4: 'pineapple', 5: 'HERE', 6: 'IS', 7: 'PLAYGROUND!'}
del m[0]
# {1: 'have', 2: 'an', 3: 'apple', 4: 'pineapple', 5: 'HERE', 6: 'IS', 7: 'PLAYGROUND!'}
m[100]
# KeyError
m.get(1) # 'have'
m.get(100) # None
m.get(100, 'pen') # 'pen'

for i in m:
	x = m[i]
for i, x in m.items():
	print('#%d' % i)
	print(x)
```

## Function
```python
def my_func(tokens, sep = ','):
	text = sep.join(tokens)
	return text
my_func(tokens) # "HERE,IS,PLAYGROUND!"
my_func(tokens, sep = '!') # "HERE!IS!PLAYGROUND!"
```

## Read and Write
```python
f = open('toRead', 'r')
new_m = {}
for line in f.readlines():
	sentence, order = line[:-1].split('.')
	new_m[sentence] = int(order)

w_f = open('toWrite', 'w')
for sentence in sorted(new_m, key = new_m.__getitem__, reverse = True):
	w_f.write(sentence + '\n')
```