
>>> x = Sum(1, 2)
>>> str(x)
'Sum(1, 2)'

>>> x.a = 2
>>> x.update()  # Recalculate the sum after modifying a
>>> str(x)
'Sum(2, 2) # sum=\'3\''
