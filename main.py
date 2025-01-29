# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print(99.9 > 99.8 and 1000 != 1000.1)

# 3rd program
print(2 * 2 + 2)
print(2 * (2 + 2))
print((2 * 2 + 2) == (2 * (2 + 2)))

# 4th program variant 1
str_in = '123.456'
f_num_1 = float(str_in)
f_num_2 = f_num_1 * 10
i_num = int(f_num_2)
result = i_num % 10
print(result)

# 4th program variant 2
str_in = '123.456'
pnt = str_in.index('.')
result = str_in[pnt+1:pnt+2]
print(result)