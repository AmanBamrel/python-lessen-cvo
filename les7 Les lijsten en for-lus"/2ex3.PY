vloot = []

while True:
    merk = input("Voer een merk in (of typ 'q' om te stoppen): ")
    if merk.lower() == 'q':
        break
    vloot.append(merk)

print(f"\n[GEREGISTREERD] Er zijn {len(vloot)} voertuigen succesvol geregistreerd.")

print("\n--- D2: VLOOTOVERZICHT (AutoTrack NV) ---")

for nummer, merk in enumerate(vloot, start=1):
    print(f"{nummer}. {merk}")
print("-" * 40)


while True:
    te_verwijderen = input("Welk voertuig moet verwijderd worden? ")
    
    if te_verwijderen in vloot:
        vloot.remove(te_verwijderen)
        print(f"\n[BEVESTIGING]: {te_verwijderen} is succesvol verwijderd uit de vloot.")
        break  
    else:
        print(f"[FOUTMELDING]: {te_verwijderen} staat niet in de vloot! Probeer opnieuw.")


if not vloot:
    print("(De vloot is momenteel leeg)")
else:
    for nummer, merk in enumerate(vloot, start=1):
        print(f"{nummer}. {merk}")