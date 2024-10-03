from Songclass import Song

def läs_in_låtar(filnamn):
    låtlista = []
    with open(filnamn, "r", encoding="utf-8") as fil:
        for rad in fil:
            delar = rad.strip().split("<SEP>")  
            if len(delar) == 4: 
                trackid, låtid, artistnamn, låttitel = delar
                låt = Song(trackid, låtid, artistnamn, låttitel)
                låtlista.append(låt)  
    return låtlista

def main():
    filnamn = "unique_tracks.txt" 
    låtlista = läs_in_låtar(filnamn)

    # Testa inläsningen genom att skriva ut första 10 låtarna
    for låt in låtlista[:10]:
        print(låt)

if __name__ == "__main__":
    main()
