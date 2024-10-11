import csv

class DictHash:
    def __init__(self):
        self.dictionary = {}

    def store(self, nyckel, data):
        self.dictionary[nyckel] = data

    def search(self, nyckel):
        return self.dictionary.get(nyckel, None)

    def __getitem__(self, nyckel):
        return self.search(nyckel)

    def __contains__(self, nyckel):
        return nyckel in self.dictionary


class Drama:
    def __init__(self, name, rating, actors, viewship_rate, genre, director, writer, year, episodes, network):
        self.name = name
        self.rating = rating
        self.actors = actors
        self.viewship_rate = viewship_rate
        self.genre = genre
        self.director = director
        self.writer = writer
        self.year = year
        self.episodes = episodes
        self.network = network

    def __str__(self):
        return f"Drama({self.name}, {self.rating}, {self.actors}, {self.viewship_rate}, {self.genre}, {self.director}, {self.writer}, {self.year}, {self.episodes}, {self.network})"


def read_dramas_from_file(file_path):
    dramas_hash = DictHash()  
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            
            drama = Drama(
                row['Drama Name'],
                row['Rating(Out of 10)'],
                row['Actors'],
                row['Viewship Rate'],
                row['Genre'],
                row['Director'],
                row['Writer'],
                row['Year'],
                row['No of Episodes'],
                row['Network']
            )
            # Lagra dramaobjektet i hashtabellen, använd 'Drama Name' som nyckel
            dramas_hash.store(row['Drama Name'], drama)

    return dramas_hash 


def search_drama(dramas_hash):
    drama_name = input("""vilket drama vill du söka efter? """)
    if drama_name in dramas_hash:
        print(dramas_hash[drama_name])
    else:
        print("""dramat hittades inte""")


if __name__ == "__main__":

    file_path = "kdrama.csv"

    dramas_hash = read_dramas_from_file(file_path)

    search_drama(dramas_hash)
