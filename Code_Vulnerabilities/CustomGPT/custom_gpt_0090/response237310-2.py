
x = Sum(1, 2)
print(str(x))  # 'Sum(1, 2)'

x.a = 2
x.update()
print(str(x))  # 'Sum(2, 2)  # sum=3'
