klant_naam = input( 'wat is jouw naam :')
aantal_producten = int(input('aantal producten: '))
if aantal_producten < 0:
    print("Fout: Het aantal producten kan niet negatief zijn!")
else:
    prijs_per_stuk = float(input("Prijs per stuk: "))
    btw_percentage = float(input("Voer het BTW-percentage in  6, 12 of 21: "))

    subtotaal = aantal_producten * prijs_per_stuk
    btw_bedrag = subtotaal * (btw_percentage / 100)
    totaalbedrag = subtotaal + btw_bedrag

    subtotaal_afgerond = round(subtotaal, 2)
    btw_afgerond = round(btw_bedrag, 2)
    totaal_afgerond = round(totaalbedrag, 2)


print(f"Factuur voor: {klant_naam}")
print(f"Aantal producten: {aantal_producten}")
print(f"Prijs per stuk: € {prijs_per_stuk:.2f}")
print(f"Subtotaal: € {subtotaal_afgerond:.2f}")

print(f"BTW ({btw_percentage}%): € {btw_afgerond:.2f}")
print(f"TOTAAL: € {totaal_afgerond:.2f}")

