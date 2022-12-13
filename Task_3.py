from os import system


system('cls')

print("\nПрограмма принимает на вход координаты точки (X и Y), X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.\n")

X = input("Введите X, напоминаю X ≠ 0: ")
Y = input("Введите Y, напоминаю Y ≠ 0: ")

if not X.isdigit() or not Y.isdigit():
    print("\nПривет, неизвестная форма жизни... \nОставайтесь на месте, за вами уже вылетели...\n")
    exit()

X = int(X)
Y = int(Y)
if X != 0 and Y != 0:
    if Y > 0:
        res = 1 if X > 0 else 2
        
    else:
        res = 3 if X < 0 else 4
        
    print(f"\nТочка ({X=}, {Y=}) находится в {res}-й четверти плоскости\n")

else:
    print(f"\nВы ввели {X=} и {Y=}. Внимательнее, по условию X ≠ 0 и Y ≠ 0...\n")
