print('menu')
print('1 voor BTW rekenen')
print('2 voor Temperatuur omrekenen')
print('3 Stoppen')

keuze = input ("maak een keuze 1 , 2 of 3 : ")
if keuze == "1" : 
    bedrag_str  = input("Voer het bedrag in (excl. BTW, in €): ")
    bedrag      = float(bedrag_str)
    tarief_str  = input("Welk BTW-tarief? (6, 12 of 21): ")
    tarief      = int(tarief_str)

    btw_bedrag  = bedrag * (tarief / 100)
    totaal      = bedrag + btw_bedrag 
    print("-" * 45)
    print(f"Bedrag excl. BTW : €{bedrag:.2f}")
    print(f"BTW ({tarief}%)        : €{btw_bedrag:.2f}")
    print(f"Totaal incl. BTW : €{totaal:.2f}")
    print("=" * 45)

elif keuze == "2":
    print("=" * 40)

    temp_f = input("Voer de temperatuur in Fahrenheit in: ")
    temp_farenheit = float(temp_f)

    temp_celcius = (temp_farenheit - 32) / 1.8
    print(f"De temperatuur in Celsius is: {temp_celcius:.1f}°C")

    temp_C = input("Voer de temperatuur in Celcius in: ")
    temp_celcius = float(temp_C)

    temp_farenheit = (temp_celcius * 1.8) + 32
    print(f"De temperatuur in Farenheit is : {temp_farenheit:.1f}°F") 

elif keuze == "3":
     print ("gestopt")