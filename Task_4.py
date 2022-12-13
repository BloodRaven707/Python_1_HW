from os import system


system('cls')

print("\nПрограмма по введенному номеру четверти, показывает диапазон возможных координат точек в этой четверти (X и Y).\n")

num = input("Введите номер четверти, число от 1 до 4: ")

if not num.isdigit():
    print("\nПривет, неизвестная форма жизни... \nОставайтесь на месте, за вами уже вылетели...\n")
    exit()

num = int(num)
if num in range(1,5):
    print(f"\nДиапазон возможных координат точек в {num}-й четверти: ", end="")
    if num == 1:
        print(f"X > 0, Y > 0\n")
    elif num == 2:
        print(f"X < 0, Y > 0\n")
    elif num == 3:
        print(f"X < 0, Y < 0\n")
    else:
        print(f"X > 0, Y < 0\n")

else:
    print("\nЧервертей всего 4-е, в следующий раз, введите число от 1 до 4\n")
