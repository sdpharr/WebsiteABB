def optellen(a, b):
    return a + b

def aftrekken(a, b):
    return a - b

def vermenigvuldigen(a, b):
    return a * b

def delen(a, b):
    if b == 0:
        raise ValueError("Kan niet delen door nul.")
    return a / b

def get_getal(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Voer een geldig getal in.")

def rekenmachine():
    print("=== Python Rekenmachine ===")
    print("Bewerkingen: +  -  *  /")
    print("Typ 'stop' om af te sluiten.\n")

    while True:
        getal1_input = input("Eerste getal: ")
        if getal1_input.lower() == "stop":
            print("Tot ziens!")
            break

        try:
            getal1 = float(getal1_input)
        except ValueError:
            print("Voer een geldig getal in.\n")
            continue

        bewerking = input("Bewerking (+, -, *, /): ").strip()
        if bewerking not in ("+", "-", "*", "/"):
            print("Onbekende bewerking. Gebruik +, -, * of /.\n")
            continue

        getal2 = get_getal("Tweede getal: ")

        try:
            if bewerking == "+":
                resultaat = optellen(getal1, getal2)
            elif bewerking == "-":
                resultaat = aftrekken(getal1, getal2)
            elif bewerking == "*":
                resultaat = vermenigvuldigen(getal1, getal2)
            elif bewerking == "/":
                resultaat = delen(getal1, getal2)

            if resultaat == int(resultaat):
                print(f"Uitkomst: {getal1:g} {bewerking} {getal2:g} = {int(resultaat)}\n")
            else:
                print(f"Uitkomst: {getal1:g} {bewerking} {getal2:g} = {resultaat:.6g}\n")

        except ValueError as e:
            print(f"Fout: {e}\n")

if __name__ == "__main__":
    rekenmachine()
