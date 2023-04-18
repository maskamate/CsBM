import random

sebesseg = []
for i in range(33):
    sebesseg.append(random.randint(1, 12))
print("A sebességváltó állásai: " + ", ".join(str(s) for s in sebesseg))

for i in range(33):
    ora = i // 6
    perc = (i % 2) * 30
    if sebesseg[i] == 12:
        print("A(z) {}. órában sikerült először a legmagasabb fokozatba váltani.".format(ora+1))
        break
else:
    print("Nem sikerült a legmagasabb fokozatba váltani az út során.")