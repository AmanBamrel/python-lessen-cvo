getal1 = int(input('voer een getal in '))
getal2 = int(input(' voer een getal in '))

som = getal1 + getal2
verschil = getal1 - getal2 
product = getal1 * getal2
deling = getal1 / getal2

print (f' som : {som}')
print (f' verschil:{verschil}')
print (f' product:{product}')
print (f'deling : {deling}')


if getal1 % 2 == 0: 
    print (' het eerste getal is even')
else :
    print ( 'het eerste getal is oneven')
###
kwadraat = getal1 ** 2
print (f' kwadraat van eerste getal {kwadraat}')
