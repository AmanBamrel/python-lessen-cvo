winst_input = input("Voer de geschatte winst in (€): ")
personeel_input = input("Voer het aantal beschikbare personen in: ")
risico = input("Voer de risicofactor in (Laag, Medium, Hoog): ").strip().lower()

if winst_input.isdigit() and personeel_input.isdigit():

    winst = float(winst_input)
    personeel = int(personeel_input)

else:
    print(" Fout: Ongeldige invoer! Voer alleen hele getallen in.")
    winst = 0.0
    personeel = 0


if risico == "hoog" and winst < 5000:
    status = "Geweigerd (bij hoog risico in combinatie met lage winst)"
elif personeel < 3:
    status = "on hold te weinig personeel"
else:
    status = "Goedgekeurd"


print("-" * 45)
print(f"Evaluatie Resultaat: {status}")
print("=" * 45)