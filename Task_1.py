from os import system


system("cls")

print("\nПрограмма принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.\n")

def WathIsADaY(num):
    if num in [6, 7]:
        return f"Да, {num}-й день недели - это выходной день\n"
    elif num in range(6):
        return f"Нет, {num}-й день недели - это рабочий день\n"


num = input("Введите порядковый номер дня недели: ")
if num.isdigit():
    num = int(num)
    if num in range(1, 8):
        print(f"\n{WathIsADaY(num)}")

    else:
        print(f"\nВы ввели число: \"{num}\". Не могу определить с какой вы планеты...\n")
        
else:
    print(f"\nВы ввели: \"{num}\". Не понимаю, что вы хотите узнать...")
    print(f"В следующий раз, введите число > 0 означающее день недели...\n")
