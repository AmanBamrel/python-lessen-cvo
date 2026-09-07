producten = []
producten.append('Brood')
print(producten) 

producten.append('Melk')
print(producten)  
producten.append('Kaas')
print(producten) 
producten.insert(0, 'Boter')
print(producten)  
producten.insert(2, 'Yoghurt')
print(producten)  
print(len(producten))


scores = [88, 45, 92, 67, 45, 100, 55]

scores.remove(45)
print("Na stap 1 (remove 45):", scores)

verwijderde = scores.pop()
print("Na stap 2 (pop) - verwijderde waarde:", verwijderde)
print("Lijst na pop:", scores)


del scores[1]
print("Na stap 3 (del scores[1]):", scores)
print()

namen = ['Ali', 'Bianca', 'Carlos', 'Diana', 'Elias']

print("Deelstap 1 (Aparte lijnen):")
for naam in namen:
    print(naam)

print("\nDeelstap 2 (Welkomstbericht):")
for naam in namen:
    print(f"Welkom, {naam}!")

print("\nDeelstap 3 (Namen langer dan 5 letters):")
for naam in namen:
    if len(naam) > 5:
        print(naam)
print()

for nummer, naam in enumerate(namen, start=1):
    print(f"{nummer}. {naam}")

print(f"Dat waren alle deelnemers, {namen[-1]}.")