
class Voertuig:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = int(bouwjaar)

    def __str__(self):
        # D5: Bepaalt de exacte __str__ tekstuitvoer
        return f"{self.merk} {self.model} ({self.bouwjaar})"

vloot = []

while True:
    merk = input("Voer het merk in (of 'q' om te stoppen): ")
    if merk.lower() == 'q':
        break
    model = input(f"Voer het model in van {merk}: ")
    bouwjaar = input(f"Voer het bouwjaar in van {merk} {model}: ")
    

    vloot.append(Voertuig(merk, model, bouwjaar))
    print("[Object succesvol aangemaakt]\n")

print("\n--- D5: VOLLEDIG OVERZICHT (Via __str__ methode) ---")
for v in vloot:
    print(v)
print("-" * 50)

print("\n--- D5: GEFILTERD OVERZICHT (Bouwjaar >= 2020) ---")
for v in vloot:
    if v.bouwjaar >= 2020:
        print(v)