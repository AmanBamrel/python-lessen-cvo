
while True:
    temperatuur = int(input("Voer de temperatuur in: "))
    
    if temperatuur >= -50 and temperatuur <= 60:
        print(f"Geldige temperatuur geregistreerd: {temperatuur} graden")
        break 
    else:
        print("Ongeldige temperatuur, probeer opnieuw.")
