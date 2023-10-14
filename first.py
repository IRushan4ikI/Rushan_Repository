import matplotlib.pyplot as plt

choise = input("Выберите график(цифру): 1.парабола(y=x^2) 2.прямая(y=2x+1) 3.модульный график(y=|x|) ")



if int(choise) == 1:
    x = []
    y = []
    for i in range(6):
        x1 = int(input('Введите отрицательные числа(-10000<x<0): '))
        x.append(x1)
        y.append(x1**2)
    x.append(0)
    y.append(0)
    for i in range(6):
        x2 = int(input('Введите положительные числа(0<x<100000): '))
        x.append(x2)
        y.append(x2**2)
    plt.plot(x, y)
    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')
    plt.title('Пример графика')
    plt.show()

elif int(choise) == 2:
    x = []
    y = []
    for i in range(2):
        x1 = int(input("Введите два любых числа: "))
        x.append(x1)
        y.append(2*x1+1)
    plt.plot(x, y)
    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')
    plt.title('Пример графика')
    plt.show()
else:
    x = []
    y = []
    for i in range(4):
        x1 = int(input('Введите отрицательные числа(-10000<x<0: '))
        x.append(x1)
        y.append(-1*x1)
    x.append(0)
    y.append(0)
    for i in range(4):
        x2 = int(input('Введите положительные числа(0<x<100000): '))
        x.append(x2)
        y.append(x2)
    plt.plot(x, y)
    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')
    plt.title('Пример графика')
    plt.show()
        




"""
plt.plot(x, y)
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('Пример графика')
plt.show()
"""