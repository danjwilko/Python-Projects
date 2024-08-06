def make_album(artist, title, tracks=None):
    """Returns a dictionary with information about an album."""
    album_details = {
        'Artist': artist.title(),
        'Album title': title.title()
    }
    if tracks:
        album['Tracks'] = tracks
    return album_details


artist_prompt = "Enter the artist's name: "
title_prompt = "Enter the album title: "


print("Enter 'q' to quit at any time.")

while True:
    artist = input(artist_prompt)
    if artist == 'q':
        break

    title = input(title_prompt)
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)

