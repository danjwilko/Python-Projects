def make_album(artist, title, tracks=None):
    """Returns a dictionary with information about an album."""
    album = {'Artist': artist.title(), 'Album title': title.title()}
    if tracks:
        album = {'Artist': artist.title(), 'Album title': title.title(), 'Number of tracks': tracks}
    else:
        album = {'Artist': artist.title(), 'Album title': title.title()}
    return album


while True:
    print("Enter the artist's name: ")
    print("(enter 'q' to quit at any time.)")

    artist = input('Artist name: ')
    if artist == 'q':
        break
    print("Enter the album's title: ")
    title = input('Album title: ')
    if title == 'q':
        break
    formatted_album = make_album(artist, title)
    print(f"{formatted_album}")


