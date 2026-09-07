aantal_producten = 0
totaalbedrag = 0.0

while True:
    product = input('Productnaam (of "q" om te stoppen): ')
    
    if product == 'q':
        break  
    while True: 
        prijs =(float(input(f'wat is de prijs van {product}?')))

        if prijs >=0.00 and prijs <= 999.99:
            break
        else: 
            print( "ongeldige prijs, probeer opnieuwe.")
    aantal_producten = aantal_producten + 1
    totaalbedrag = totaalbedrag + prijs 

kortingpercentage = 0
kortingbedrag = 0.0
if totaalbedrag >= 100.00:
    kortingbedrag = 10
    kortingbedrag = totaalbedrag * 0.10
elif totaalbedrag > 50.00:
    kortingbedrag = 5
    kortingbedrag = totaalbedrag * 0.05
te_betalen = totaalbedrag - kortingbedrag 

print(f"Je hebt {aantal_producten} producten ingescand.")
print(f"Totaal voor korting: €{totaalbedrag:.2f}")
print(f"Korting ({kortingpercentage}%):     -€{kortingbedrag:.2f}")
print(f"Te betalen:          €{te_betalen:.2f}")