import timeit
from Songclass import Song


filename = "unique_tracks.txt"
n = 100000
testlåt = 'Weekend Love'

def readfile(filename):
    låtlista = []
    with open(filename, "r", encoding="utf-8") as fil:
        for rad in fil:
            delar = rad.strip().split("<SEP>")  # Dela upp raden vid <SEP>
            if len(delar) == 4:  # Säkerställ att vi har 4 delar
                trackid, låtid, artistnamn, låttitel = delar
                låt = Song(trackid, låtid, artistnamn, låttitel)
                låtlista.append(låt)  # Lägg till låten i listan
    return låtlista

def linear_search(songs, target):
    for index, song in enumerate(songs):
        if song.låttitel == target:
            return index
    return -1


def binary_search(sorted_songs, target):
    
    left, right = 0, len(sorted_songs) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = sorted_songs[mid].låttitel

        if mid_val == target:
            return mid  # Returnera index om låttiteln hittades
        elif mid_val < target:
            left = mid + 1  # Flytta till höger om mittenvärdet är mindre än målet
        else:
            right = mid - 1  # Flytta till vänster om mittenvärdet är större än målet

    return -1  # Om låttiteln inte hittades

def hash_search(song_dict, target):
    return song_dict.get(target, None)



def sökningar(songs, sorted_songs, song_dict, target):

    # Testa linjär sökning
    linear_result = linear_search(songs, target)
    print(f"Linjär sökning: Index: {linear_result}")

    # Testa binär sökning
    binary_result = binary_search(sorted_songs, target)
    print(f"Binär sökning: Index: {binary_result}")

    # Testa sökning i hashtabell
    hash_result = hash_search(song_dict, target)
    print(f"Sökning i hashtabell: {hash_result}")


def tidtagning(songs, sorted_songs, song_dict, target):

    linjtid = timeit.timeit(stmt = lambda: linear_search(songs, target), number = 1000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    bintid = timeit.timeit(stmt= lambda: binary_search(sorted_songs, target), number = 1000)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")

    hashtid = timeit.timeit(stmt= lambda: hash_search(song_dict, target), number = 1000)
    print("Hashsökningen tog", round(hashtid, 4) , "sekunder")

def main():

    songs = readfile(filename)

    length = len(songs)
    #length = len(songs)/2
    #length = len(songs)/4

    songs = songs[:length]
    sista = songs[len(songs) - 1]
    #target = input("Vilken låt ska vi söka efter? ")
    target = sista.låttitel

    # Sorterar listan för binärsökning
    sorted_songs = sorted(songs, key=lambda x: x.låttitel)

    # Skapar en hashtabell med låttitel som nyckel
    song_dict = {song.låttitel: song for song in songs} 

    inp = input('t för tidtagning, s för sökning: ')

    if inp == 't':
        print(f"Tiden för {length} element:")
        tidtagning(songs, sorted_songs, song_dict, target)
    elif inp == 's':
        sökningar(songs, sorted_songs, song_dict, target)
    else: 
        return

if __name__ == "__main__":
    main()
