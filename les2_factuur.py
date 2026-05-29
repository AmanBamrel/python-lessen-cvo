klant_naam = input( 'wat is jouw naam :')
aantal_producten = int(input('aantal producten: '))
prijs_per_stuk = float(input("Prijs per stuk: "))

subtotal = aantal_producten * prijs_per_stuk
btw_bedrag = subtotal * 0.21
totalbedrag = subtotal + btw_bedrag

print (f'factuur voor : {klant_naam}')
print (f' aantal producten : { aantal_producten}')
print(f'prijs per stuk :{prijs_per_stuk:.2f}')

print(f"Subtotaal: € {subtotal:.2f}")
print(f"BTW (21%): € {btw_bedrag:.2f}")
print(f"TOTAAL: € {totalbedrag:.2f}")