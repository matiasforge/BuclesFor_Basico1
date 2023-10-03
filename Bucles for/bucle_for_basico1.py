# Básico
for i in range(151):
    print(i)

# Múltiplos de 5
for i in range(5, 1001, 5):
    print(i)

# Contar a la manera del Dojo
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa Es un gran idiota
sum_impares = 0
for i in range(1, 500001, 2):
    sum_impares += i
print(sum_impares)

# Cuenta regresiva de a 4
for i in range(2018, 0, -4):
    print(i)

# Contador flexible
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
