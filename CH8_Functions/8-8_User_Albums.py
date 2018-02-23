def make_album(name, title, tracks=''):
    albums = {'Name': name, 'Title': title}
    if tracks:
        albums['Tracks'] = tracks

    return albums

albums = []
while True:
    print("Please enter details: ")
    print("(enter 'q' anytime to quit)")

    name = input("Artist Name : ")
    if name == 'q':
        break

    title = input("Album Title : ")
    if title == 'q':
        break

    tracks = input("No. of tracks (optional): ")

    album = make_album(name, title, tracks)
    albums.append(album)

for album in albums:
    for k, v in album.items():
        print("Album {0} : {1}".format(k, v))
    print()