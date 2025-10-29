result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'

index1 = result1.index(':') + 2
number1 = int(result1[index1:])
print(number1 + 10)

index2 = result2.index(':') + 2
number2 = int(result2[index2:])
print(number2 + 10)

index3 = result3.index(':') + 2
number3 = int(result3[index3:])
print(number3 + 10)
