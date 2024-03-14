import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

if not 2 <= len(sys.argv) <= 3:
    sys.exit(1, "Must pass only 1 spotify artist link as parameter and size indicator")

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

if sys.argv[1] == 0:
    sys.exit(1)


def add_relate_artist(artist_id: str, related_dict: dict, detail_dict:dict):
    """
    Add all artist that relate to artist parameter to related_dict param
    :param artist_id: Spotify artist link
    :param related_dict: Dict that has 4 keys [artist_name, artist_id, related_artist_name, related_artist_id]
    """

    artist = sp.artist(artist_id)
    artist_relate = sp.artist_related_artists(artist_id)

    print(f"Add {artist['name']} relate artist")

    if artist['id'] not in detail_dict['artist_id']:
        add_artist_detail(artist, detail_dict)

    for relate in artist_relate['artists']:
        related_dict['artist_name'].append(artist['name'])
        related_dict['artist_id'].append(artist['id'])
        related_dict['related_artist_name'].append(relate['name'])
        related_dict['related_artist_id'].append(relate['id'])

        if relate['id'] not in detail_dict['artist_id']:
            add_artist_detail(relate, detail_dict)


def add_artist_detail(artist: dict, detail_dict: dict):

    print(f"Add {artist['name']} to detailed table")

    detail_dict['artist_name'].append(artist['name'])
    detail_dict['artist_id'].append(artist['id'])
    detail_dict['genres'].append(", ".join(artist['genres']))
    detail_dict['followers'].append(artist['followers']['total'])
    try:
        detail_dict['img_url'].append(artist['images'][2]['url'])
    except IndexError:
        detail_dict['img_url'].append('None')

    detail_dict['external_url'].append(artist['external_urls']['spotify'])


def created_20x20_related_table(artist_id: str, level:int):
    """
    Create csv file by querying from spotify API by find 20 artist that similar to artist that pass in as parameter.
    For each related artist there will be more 20 artist that relate to that relate artist.
    :param artist_id: Spotify artist link
    """

    assert isinstance(level, int)

    link_table = {
        'artist_name': [],
        'artist_id': [],
        'related_artist_name': [],
        'related_artist_id': []

    }
    detail_table = {
        'artist_name': [],
        'artist_id': [],
        'genres': [],
        'followers': [],
        'img_url': [],
        'external_url': []
    }

    add_relate_artist(artist_id, link_table, detail_table)

    for i in range(level):
        more_related_id = [related
                           for related in link_table['related_artist_id'] if
                           related not in link_table['artist_id']]
        [add_relate_artist(related_id, link_table, detail_table) for related_id in more_related_id]

    pd.DataFrame(link_table).to_csv(
        f'result/{level}_level_{link_table["artist_name"][0]}_related.csv',
        index=False
    )
    pd.DataFrame(detail_table).to_csv(
        f'result/{level}_level_{link_table["artist_name"][0]}_detail.csv',
        index=False
    )


try:
    created_20x20_related_table(sys.argv[1], int(sys.argv[2]))
    print("CSV created")
except spotipy.SpotifyException:
    sys.exit("Link invalid")



