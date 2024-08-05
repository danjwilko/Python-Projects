def make_album(artist, title, tracks=None):
    """Returns a dictionary with information about an album."""
    album = {'Artist': artist.title(), 'Album title': title.title()}
    if tracks:
        album = {'Artist': artist.title(), 'Album title': title.title(), 'Number of tracks': tracks}
    else:
        album = {'Artist': artist.title(), 'Album title': title.title()}
    return album


album1 = make_album('nirvana', 'nevermind', 10)
print(album1)
album2 = make_album('ac-dc', 'back in black')
print(album2)
album3 = make_album('green day', 'american idiot')
print(album3)