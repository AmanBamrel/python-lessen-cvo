print ("=" * 45)
print ("korting checker - PrimaBouw BV")
print ("=" * 45 )

totaalbedrag = float(input("Voer het totale orderbedrag in (€): "))

if totaalbedrag > 1000:
    print("Hoera! Deze klant heeft recht op een volumekorting.")
else:
    print("Status: Standaard tarief van toepassing (geen korting).")
