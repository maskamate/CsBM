
def mghmsh(szo):
    magánhangzók = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
    mghdb = 0
    for i in szo:
        if i in magánhangzók:
            mghdb += 1

    print(mghdb, "darab magánhangzó és ", len(szo)-mghdb, "mássalhangzó van benne!")

be_szo = None
while be_szo != "":
    be_szo= input("Adj meg egy szót! ")
    if be_szo != "":
        mghmsh(be_szo)