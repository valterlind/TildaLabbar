import time
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

def linear_search(songs, target):
    for index, song in enumerate(songs):
        if song.låttitel == target:
            return index
    return -1

def binary_search(songs, target):
    left, right = 0, len(songs) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = songs[mid].låttitel
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def search_in_dict(song_dict, target):
    return song_dict.get(target, None)

def main():
    # Läs in låtar från fil
    songs = läs_in_låtar("unique_tracks.txt")

    # Testa linjär sökning
    target = "2 Da Beat Ch'yall"  # Ange en låttitel som ska sökas (uppdatera med en giltig titel)
    start_time = time.time()
    linear_result = linear_search(songs, target)
    linear_time = time.time() - start_time
    print(f"Linjär sökning: Index: {linear_result}, Tid: {linear_time:.6f} sekunder")

    # Testa binär sökning
    songs_sorted = sorted(songs)  # Sortera låtarna
    start_time = time.time()
    binary_result = binary_search(songs_sorted, target)
    binary_time = time.time() - start_time
    print(f"Binär sökning: Index: {binary_result}, Tid: {binary_time:.6f} sekunder")

    # Testa sökning i hashtabell
    song_dict = {song.låttitel: song for song in songs}  # Skapa en hashtabell med låttitel som nyckel
    start_time = time.time()
    hash_result = search_in_dict(song_dict, target)
    hash_time = time.time() - start_time
    print(f"Sökning i hashtabell: {hash_result}, Tid: {hash_time:.6f} sekunder")

if __name__ == "__main__":
    main()
