print ("=" * 45)
print ("korting checker - PrimaBouw BV")
print ("=" * 45 )

totaalbedrag = float(input("Voer het totale orderbedrag in (€): "))


if totaalbedrag >= 2500:
    korting_pct = 15
elif totaalbedrag >= 1000:
    korting_pct = 10
elif totaalbedrag >= 500:
    korting_pct = 5
else:
    korting_pct = 0


kortingsbedrag = totaalbedrag * (korting_pct / 100)
eindbedrag = totaalbedrag - kortingsbedrag
print("-" * 45)
print(f"Bruto orderbedrag : €{totaalbedrag:.2f}")
print(f"Kortingspercentage: {korting_pct}%")
print(f"Kortingsbedrag : €{kortingsbedrag:.2f}")
print(f"Netto te betalen : €{eindbedrag:.2f}")
print("=" * 45)

