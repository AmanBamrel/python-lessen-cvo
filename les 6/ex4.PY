aantal_producten = 0
totaalbedrag = 0.0

while True:
    product = input('Productnaam (of "q" om te stoppen): ')
    
    if product == 'q':
        break  
        
    prijs = float(input(f'Wat is de prijs van {product}? '))
    
   
    aantal_producten = aantal_producten + 1
    totaalbedrag = totaalbedrag + prijs


print(f"Je hebt {aantal_producten} producten ingescand.")
print(f"Totaal: €{totaalbedrag:.2f}")