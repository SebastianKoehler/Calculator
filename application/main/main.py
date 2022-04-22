import os
import sys
import time

import calculation as calc


def programm_wiederholen():
    print("Wollen Sie eine weitere Berechnung durchführen oder das Programm beenden?\n")
    auswahl = input("Geben Sie bitte 1. Weiter oder 2. Beenden ein: ")

    if auswahl.lower().strip().replace(".", "") == "weiter" or \
            auswahl.lower().strip().replace(".", "") == "1":
        clear()
        main()
    elif auswahl.lower().strip().replace(".", "") == "beenden" or \
            auswahl.lower().strip().replace(".", "") == "2":
        clear()
        sys.exit("Bis Bald!")
    else:
        clear()
        programm_wiederholen()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    try:
        input_auswahl = input("Welche Operation möchtest du nutzen?\n"
                              "1. Addition\n"
                              "2. Subtraktion\n"
                              "3. Multiplikation\n"
                              "4. Division\n"
                              "5. Division mit Rest\n"
                              "6. Beenden\n"
                              "Deine Auswahl: ")
        print(input_auswahl)
        if input_auswahl.lower().strip().replace(".", "") == 'addition' or \
                input_auswahl.lower().strip().replace(".", "") == "1":
            clear()
            operation = "Addition"
            print(f"Operation: {operation}")
            input_ersterWert = int(input("Wie lautet der erste Wert: "))
            input_zweiterWert = int(input("Wie lautet der zweite Wert: "))
            ergebnis = calc.addition(input_ersterWert, input_zweiterWert)
            print(f"Das Ergebnis von {input_ersterWert} + {input_zweiterWert} lautet: {ergebnis}")

        elif input_auswahl.lower().strip().replace(".", "") == 'subtraktion' or \
                input_auswahl.lower().strip().replace(".", "") == "2":
            clear()
            operation = "Subtraktion"
            print(f"Operation: {operation}")
            input_ersterWert = int(input("Wie lautet der erste Wert: "))
            input_zweiterWert = int(input("Wie lautet der zweite Wert: "))
            ergebnis = calc.subtraktion(input_ersterWert, input_zweiterWert)
            print(f"Das Ergebnis von {input_ersterWert} - {input_zweiterWert} lautet: {ergebnis}")

        elif input_auswahl.lower().strip().replace(".", "") == "multiplikation" or \
                input_auswahl.lower().strip().replace(".", "") == "3":
            clear()
            operation = "Multiplikation"
            print(f"Operation: {operation}")
            input_ersterWert = int(input("Wie lautet der erste Wert: "))
            input_zweiterWert = int(input("Wie lautet der zweite Wert: "))
            ergebnis = calc.multiplikation(input_ersterWert, input_zweiterWert)
            print(f"Das Ergebnis von {input_ersterWert} * {input_zweiterWert} lautet: {ergebnis}")

        elif input_auswahl.lower().strip().replace(".", "") == "division" or \
                input_auswahl.lower().strip().replace(".", "") == "4":
            clear()
            operation = "Division"
            print(f"Operation: {operation}")
            input_ersterWert = int(input("Wie lautet der erste Wert: "))
            input_zweiterWert = int(input("Wie lautet der zweite Wert: "))
            ergebnis = calc.division(input_ersterWert, input_zweiterWert)
            print(f"Das Ergebnis von {input_ersterWert} / {input_zweiterWert} lautet: {ergebnis}")

        elif input_auswahl.lower().strip().replace(".", "") == "division mit rest" or \
                input_auswahl.lower().strip().replace(".", "") == "5":
            clear()
            operation = "Division mit Rest"
            print(f"Operation: {operation}")
            input_ersterWert = int(input("Wie lautet der erste Wert: "))
            input_zweiterWert = int(input("Wie lautet der zweite Wert: "))
            ergebnis = calc.modulo(input_ersterWert, input_zweiterWert)
            print(f"Das Ergebnis von {input_ersterWert} % {input_zweiterWert} lautet: {ergebnis}")

        elif input_auswahl.lower().strip().replace(".", "") == "beenden" or \
                input_auswahl.lower().strip().replace(".", "") == "6":
            clear()
            sys.exit("Bis Bald!")

        else:
            clear()
            print("Falsche Eingabe!")
            time.sleep(3)
            clear()

        programm_wiederholen()

    except ZeroDivisionError:
        clear()
        print("Division durch 0 ist nicht erlaubt! Bitte versuche es erneut...")
        time.sleep(5)
        clear()
        main()


if __name__ == '__main__':
    main()
