decimalis = int(input("Kérlek adj meg egy 10es számrendszerbeli számot: "))
maradekok = []
    while decimalis > 0:
	maradekok.append(decimalis%2)
	decimalis = decimalis//2
print(maradekok)