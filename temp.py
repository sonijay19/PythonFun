# word = 'cemputer'
# print(len(word))
# print(word.index('e'))
# a = list(word)
# print(list(word))
# print(a)
# a[2] = 'X'
# word = ''.join(a)
# print(word)

print('soni')
s = 'Jay#Soni#e'
c = '#'
a = []
for i in range(0,len(s)) :
    if s[i] == c:
        a.append(i)
v = list(s)
for t in a:
    v[t] = 'T'
s = ''.join(v)
print(a)
print(s)