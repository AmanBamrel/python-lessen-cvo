print("=" * 45)
print("  Kortingscalculator - PrimaBouw BV")
print("=" * 45)


totaalbedrag = float(input("Voer het totale orderbedrag in (€): "))
klant_type = input("Voer het type klant in (Standaard, Zilver, Goud): ")


if totaalbedrag >= 2500:
    korting_pct = 15
elif totaalbedrag >= 1000:
    korting_pct = 10
elif totaalbedrag >= 500:
    korting_pct = 5
else:
    korting_pct = 0

if klant_type.lower() == "goud":
    korting_pct += 5
elif klant_type.lower() == "zilver":
    korting_pct += 2


kortingsbedrag = totaalbedrag * (korting_pct / 100)
eindbedrag = totaalbedrag - kortingsbedrag


print("-" * 45)
print(f"Klantsegment      : {klant_type.capitalize()}")
print(f"Bruto orderbedrag : €{totaalbedrag:.2f}")
print(f"Kortingspercentage: {korting_pct}%")
print(f"Kortingsbedrag    : €{kortingsbedrag:.2f}")
print(f"Netto te betalen  : €{eindbedrag:.2f}")
print("=" * 45)