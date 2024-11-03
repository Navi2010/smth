x = {'Codingal':1, 'is':2, 'best':2, 'for':2, 'coding':3}

numb = int(input('enter a number (1,2,3): '))
numb_count = numb

cnt = 0
for key in x:
    if x[key] == numb_count:
       cnt += 1

print ('there are/is', cnt)

