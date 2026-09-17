while True:
    print("--- Меню ---")
    print(" a - фигура a")
    print(" b - фигура b")
    print(" c - фигура c")
    print(" d - фигура d")
    print(" e - фигура e")
    print(" f - фигура f")
    print(" g - фигура g")
    print(" h - фигура h")
    print(" i - фигура i")
    print(" j - фигура j")
    choice = input(" Выберете букву: ")
    if choice == "ext":
        print("выход из программы.")
        break
    elif choice == "a":
        n = 5
        for p in range(n):
            for k in range(n):
                if k >= p:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == "b":
        n = 5
        for p in range(n):
            for k in range(n):
                if k <= p:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == "c":
        n = 5
        for p in range(n):
            for k in range(n):
                if k >= p and k <= n - 1 - p:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == "d":
        n = 5
        for p in range(n):
            for k in range(n):
                if k <= p and k >= n - 1 - p:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == "e":
        n = 5
        for p in range(n):
            for k in range(n):
                if (k >= p and k <= n - 1 - p) or (k <= p and k >= n - 1 - p):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == "f":
        n = 5
        for p in range(n):
            for k in range(n):
                if (k <= p and k <= n - 1 - p) or (k >= p and k >= n - 1 - p):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == "g":
        n = 5
        for p in range(n):
            for k in range(n):
                if k >= p and k >= n - 1 - p:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == "h":
        n = 5
        for p in range(n):
            for k in range(n):
                if k <= p and k <= n - 1 - p:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == "i":
        n = 5
        for p in range(n):
            for k in range(n):
                if k <= p:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif choice == "j":
        n = 5
        for p in range(n):
            for k in range(n):
                if k >= p:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
