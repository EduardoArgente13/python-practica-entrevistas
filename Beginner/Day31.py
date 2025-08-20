'''
Ejercicio 1: Agrupar canciones por artista
Tienes una lista de canciones, cada una representada como una tupla (artista, título).
Queremos agrupar las canciones por artista usando defaultdict(list).
'''

# from collections import defaultdict

# def songs_by_artist(songs):
#     if not songs:
#         return {}
    
#     grouped = defaultdict(list)
    
#     for artist, song in songs:
#         grouped[artist].append(song)
        
#     for artist in grouped:
#         grouped[artist].sort()
        
#     return dict(grouped)

# canciones = [
#     ("Radiohead", "Paranoid Android"),
#     ("Radiohead", "Karma Police"),
#     ("Daft Punk", "Harder Better Faster Stronger"),
#     ("Daft Punk", "One More Time"),
#     ("Nirvana", "Smells Like Teen Spirit"),
# ]

# print(songs_by_artist(canciones))
        

'''
Ejercicio: Contar géneros únicos por artista
Supón que tienes una lista de canciones en forma de tuplas: (artista, canción, género). Queremos agrupar por artista y contar cuántos géneros distintos toca cada uno.
''' 
# from collections import defaultdict

# def genres_by_artist(songs):
#     if not songs:
#         return {}
    
#     genres = defaultdict(set)
    
#     for artist, song, genre in songs:
#         genres[artist].add(genre)
        
#     genre_count = {artist: len(genres[artist]) for artist in genres}

#     return genre_count

# canciones = [
#     ("Radiohead", "Paranoid Android", "Alternative"),
#     ("Radiohead", "Karma Police", "Alternative"),
#     ("Radiohead", "Everything In Its Right Place", "Electronic"),
#     ("Daft Punk", "Harder Better Faster Stronger", "Electronic"),
#     ("Daft Punk", "One More Time", "Electronic"),
#     ("Daft Punk", "Get Lucky", "Funk"),
#     ("Nirvana", "Smells Like Teen Spirit", "Grunge"),
#     ("Nirvana", "Come As You Are", "Grunge"),
#     ("Nirvana", "The Man Who Sold the World", "Rock"),
# ]

# print(genres_by_artist(canciones))    


'''
Dada una lista de tuplas con formato:
(artista, canción, género)
Queremos devolver un diccionario donde las llaves sean los nombres de artistas y los valores el género más frecuente en sus canciones.
'''
# from collections import defaultdict
# from collections import Counter

# def most_listen_genres(songs):
#     if not songs:
#         return {}
    
#     count = defaultdict(Counter)
    
#     for artist, song, genre in songs:
#         count[artist][genre] += 1
        
#     res = {}
#     for artist,genre_counts in count.items():
#         most_common = genre_counts.most_common(1)[0][0]
#         res[artist] = most_common
        
#     return res

# songs = [
#     ("Radiohead", "Paranoid Android", "Alternative"),
#     ("Radiohead", "Karma Police", "Alternative"),
#     ("Radiohead", "Everything In Its Right Place", "Electronic"),
#     ("Daft Punk", "Harder Better Faster Stronger", "Electronic"),
#     ("Daft Punk", "One More Time", "Electronic"),
#     ("Daft Punk", "Get Lucky", "Funk"),
#     ("Nirvana", "Smells Like Teen Spirit", "Grunge"),
#     ("Nirvana", "Come As You Are", "Grunge"),
#     ("Nirvana", "The Man Who Sold the World", "Rock"),
# ]

# print(most_listen_genres(songs))


'''
top_genre_by_artist
Objetivo:
Dado un listado de canciones con su artista y género, devuelve por cada artista el género más frecuente que aparece en sus canciones.
'''
# from collections import defaultdict
# from collections import Counter

# def top_genre_by_artist(songs):
#     if not songs:
#         return {}
    
#     count = defaultdict(Counter)
    
#     for artist, song, genre in songs:
#         count[artist][genre] += 1
        
#     res = {}
#     for artist, genres in count.items():
#         most_common = genres.most_common(1)[0][0]
#         res[artist] = most_common
        
#     return res 

# songs = [
#     ("Radiohead", "Paranoid Android", "Alternative"),
#     ("Radiohead", "Karma Police", "Alternative"),
#     ("Radiohead", "Everything In Its Right Place", "Electronic"),
#     ("Daft Punk", "Harder Better Faster Stronger", "Electronic"),
#     ("Daft Punk", "One More Time", "Electronic"),
#     ("Daft Punk", "Get Lucky", "Funk"),
#     ("Nirvana", "Smells Like Teen Spirit", "Grunge"),
#     ("Nirvana", "Come As You Are", "Grunge"),
#     ("Nirvana", "The Man Who Sold the World", "Rock"),
# ]

# print(top_genre_by_artist(songs))



'''
Canciones más populares por género
Objetivo: Dado un listado de canciones con su título, artista, género y número de reproducciones, queremos encontrar la canción más popular por cada género.
'''

# from collections import defaultdict

# def most_popular_by_genre(songs):
#     if not songs:
#         return {}
    
#     popula_songs = defaultdict(lambda: (0, ""))
    
#     for title, artist, genre, plays in songs:
#         if plays > popula_songs[genre][0]:
#             popula_songs[genre] = (plays, title)
        
#     res = {genre: title for genre, (plays, title) in popula_songs.items()}
#     return res
    
# songs = [
#     ("Paranoid Android", "Radiohead", "Alternative", 9500000),
#     ("Karma Police", "Radiohead", "Alternative", 8000000),
#     ("Everything In Its Right Place", "Radiohead", "Electronic", 6000000),
#     ("Harder Better Faster Stronger", "Daft Punk", "Electronic", 12000000),
#     ("One More Time", "Daft Punk", "Electronic", 12500000),
#     ("Get Lucky", "Daft Punk", "Funk", 13000000),
#     ("Smells Like Teen Spirit", "Nirvana", "Grunge", 15000000),
#     ("Come As You Are", "Nirvana", "Grunge", 11000000),
#     ("The Man Who Sold the World", "Nirvana", "Rock", 7000000),
# ]

# print(most_popular_by_genre(songs))
    
    
    
    
    
    
    
    

    