def make_album(name, title, tracks=''):
    albums = {'Name': name, 'Title': title}
    if tracks:
        albums['Tracks'] = tracks

    return albums

album_1 = make_album('David Guetta', 'Like I Do')
album_2 = make_album('BoA', 'ONE SHOT, TWO SHOT', 7)
album_3 = make_album('Kendrick Lamar', 'Pray For Me')

albums = [album_1, album_2, album_3]
for album in albums:
    for k, v in album.items():
        print("Album {0} : {1}".format(k, v))
    print()