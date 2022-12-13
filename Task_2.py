from os import system


system('cls')

print("\nПрограмма проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.\n")
print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z на PYthon: not (X or Y or z) == (not X and not Y and not z)\n")

for X in [False, True]:
    for Y in [False, True]:
        for z in [False, True]:
            print(f"not({X} or {Y} or {z})",
                  f" == not {X} and not {Y} and not {z}",
                  f" == {not (X or Y or z) == (not X and not Y and not z)}",
                  sep=f'{" " * (int(X) + int(Y) + int(z))}')

print()
