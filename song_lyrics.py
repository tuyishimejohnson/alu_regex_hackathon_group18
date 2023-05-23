#!/usr/bin/python3

import song

def check_song_lyrics(lyrics):
    pattern = r"\[Verse (\d+)\] (.*)"
    matches = song.findall(pattern, lyrics)
    
    for match in maches:
        verse_number = match[0]
        lyrics_text = match[1]
        print(f"verse {verse_number}: {lyrics_text}")
    
    # example of usage
    lyrics = 
    """
    [verse 1]: I sit by myself
    [verse 2]: talking to the moon
    """
    check_song_lyrics(lyrics)
    
    
