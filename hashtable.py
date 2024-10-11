class HashNode:

    def __init__(self, key="", data=None):
        self.key = key
        self.data = data
        self.next = None  # Länkad lista för att hantera krockar


class Hashtable:
    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        self.table = [None] * size  # Skapa en tabell med angiven storlek

    def store(self, key, data):
        index = self.hashfunction(key)

        if self.table[index] is None:
            self.table[index] = HashNode(key, data)
        else:
            # Hantera krockar med länkade listor
            current = self.table[index]
            while current:
                if current.key == key:
                    current.data = data  # Uppdatera om nyckeln redan finns
                    return
                if current.next is None:
                    break
                current = current.next
            # Lägg till ny nod i slutet av listan
            current.next = HashNode(key, data)

    def search(self, key):
        """key är nyckeln
           Hämtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
           Om "key" inte finns ska det bli KeyError """
        index = self.hashfunction(key)  # Beräkna hashindex

        current = self.table[index]
        while current:
            if current.key == key:
                return current.data  # Returnera datan om nyckeln hittas
            current = current.next  # Gå till nästa nod om det finns en krock

        # Om vi inte hittade nyckeln
        raise KeyError(f"Nyckeln '{key}' finns inte i hashtabellen")

    def hashfunction(self, key):
        """key är nyckeln
           Beräknar hashfunktionen för key"""
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size  
