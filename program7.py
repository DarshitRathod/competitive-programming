lt = [1,2,3,4,5,6,7,8]

number = 4


index = lt.index(4)

del lt[index]

sh = 4

temp = lt[0:sh]
temp2 = lt[sh:]

temp.reverse()
temp2.reverse()

lt = temp + temp2
lt.reverse()

lt.insert(index,number)

print(lt)

