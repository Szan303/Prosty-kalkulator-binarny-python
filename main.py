def Dodawanie(a, b):
    return a + b
def Odejmowanie(a, b):
    return a - b
def Mnozenie(a, b):
    return a * b
def Dzielenie(a, b):
    if b == 0:
        return "Dzielenie przez zero!"
    return a / b

while True:
    print("Wybierz 1 liczbę: ")
    input1 = input()
    print("Wybierz 2 liczbę: ")
    input2 = input()

    liczba1 = float(input1)
    liczba2 = float(input2)


    print("Wybierz działanie: ")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("0. Wyjście")

    input3 = input()
    wybor = int(input3)

    match wybor:
        case 1:
            wyn = Dodawanie(liczba1, liczba2)
            print(wyn)
            break
        case 2:
            wyn = Odejmowanie(liczba1, liczba2)
            print(wyn)
            break
        case 3:
            wyn = Mnozenie(liczba1, liczba2)
            print(wyn)
            break
        case 4:
            wyn = Dzielenie(liczba1, liczba2)
            print(wyn)
            break
        case 0: 
            break
