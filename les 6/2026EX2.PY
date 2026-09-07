som = 0
teller = 1

while teller <= 49:
    if teller % 2 != 0:
        som = som + teller
    teller = teller + 1

print('De som van alle oneven getallen t/m 49 is:', som)