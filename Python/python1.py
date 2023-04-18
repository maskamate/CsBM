Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> decimalis = int(input("Kérlek adj meg egy 10es számrendszerbeli számot: "))
Kérlek adj meg egy 10es számrendszerbeli számot: 10
>>> maradekok = []
>>> while decimalis > 0:
	maradekok.append(decimalis%2)
	decimalis = decimalis//2

>>> print(maradekok)
[0, 1, 0, 1]
>>> 
>>> 