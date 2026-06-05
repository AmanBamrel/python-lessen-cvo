# temp_calculator.py – gemaakt door [ Aman Bamrel]
print("=" * 40)
print("  Temperatuuromrekening F → C")
print("=" * 40)

temp_f = input("Voer de temperatuur in Fahrenheit in: ")
temp_farenheit = float(temp_f)

temp_celcius = (temp_farenheit - 32) / 1.8
print(f"De temperatuur in Celsius is: {temp_celcius:.1f}°C")

print("=" * 40)

temp_C = input("Voer de temperatuur in Celcius in: ")
temp_celcius = float(temp_C)

temp_farenheit = (temp_celcius * 1.8) + 32
print(f"De temperatuur in Farenheit is : {temp_farenheit:.1f}°F")