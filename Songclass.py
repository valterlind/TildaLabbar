class Song:
    def __init__(self, trackid, låtid, artistnamn, låttitel):
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __str__(self):
        return(f'Track ID: {self.trackid}\n Låt ID: {self.låtid}\n Artist: {self.artistnamn}\n Titel: {self.låttitel}')

    def __lt__(self, other):
        """
        Jämför två Song-objekt baserat på artistnamn (alfabetiskt).
        :param other: Ett annat Song-objekt.
        :return: True om artistnamnet på self är mindre än artistnamnet på other, annars False.
        """
        return self.artistnamn < other.artistnamn
    print(f"Sökning i hashtabell: {hash_result}, Tid: {hash_time:.6f} sekunder")

if __name__ == "__main__":
    main()
