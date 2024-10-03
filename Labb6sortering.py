import timeit
from Songclass import Song

def läs_in_låtar(filnamn):
    låtlista = []
    with open(filnamn, "r", encoding="utf-8") as fil:
        for rad in fil:
            delar = rad.strip().split("<SEP>")  # Dela upp raden vid <SEP>
            if len(delar) == 4:  # Säkerställ att vi har 4 delar
                trackid, låtid, artistnamn, låttitel = delar
                låt = Song(trackid, låtid, artistnamn, låttitel)
                låtlista.append(låt)  # Lägg till låten i listan
    return låtlista

def bubble_sort(songs):
    n = len(songs)
    for i in range(n):
        for j in range(0, n-i-1):
            if songs[j].låttitel > songs[j+1].låttitel:
                # Byt plats om låttitlarna är i fel ordning
                songs[j], songs[j+1] = songs[j+1], songs[j]
    return songs

def quicksort(songs):
    if len(songs) <= 1:
        return songs  # Basfall: om listan har ett eller inget element är den redan sorterad

    pivot = songs[len(songs) // 2]  # Välj pivot-elementet
    left = [song for song in songs if song.låttitel < pivot.låttitel]
    middle = [song for song in songs if song.låttitel == pivot.låttitel]
    right = [song for song in songs if song.låttitel > pivot.låttitel]

    return quicksort(left) + middle + quicksort(right)

def main():
    filename = "unique_tracks.txt"

    songs_list = läs_in_låtar(filename)

    songs_list = songs_list[:10000]  # Justera storleken efter behov

    print('Antal element =', len(songs_list))

    bubble_time = timeit.timeit(stmt=lambda: bubble_sort(songs_list.copy()), number=1)
    print("Bubblesort tog", round(bubble_time, 4), "sekunder")

    quick_time = timeit.timeit(stmt=lambda: quicksort(songs_list.copy()), number=1)
    print("Quicksort tog", round(quick_time, 4), "sekunder")

if __name__ == "__main__":
    main()
