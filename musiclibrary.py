"""Music Library for Orion Voice Assistant"""

# Music database with YouTube links
music = {
    # ==================== ENGLISH SONGS ====================
    # Pop/Rock
    "blinding_lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    "shape_of_you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "bad_guy": "https://www.youtube.com/watch?v=DyDfgMOUjCI",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
    "senorita": "https://www.youtube.com/watch?v=Pkh8UtuejGw",
    "drivers_license": "https://www.youtube.com/watch?v=ZmDBbnmKpqQ",
    "levitating": "https://www.youtube.com/watch?v=TUVcZfQe-Kw",
    "dance_monkey": "https://www.youtube.com/watch?v=q0hyYWKXF0Q",
    
    # ==================== HINDI SONGS ====================
    "kesariya": "https://www.youtube.com/watch?v=Is5hox8Wprc",
    "tum_hi_ho": "https://www.youtube.com/watch?v=Umqb9KENgmk",
    "shayad": "https://www.youtube.com/watch?v=7IiJUpn4Rug",
    "levi_ki_adi": "https://www.youtube.com/watch?v=5e6EcWxkbgI",
    "dil_bechara": "https://www.youtube.com/watch?v=nU7qFN0Rzdg",
    "raabta": "https://www.youtube.com/watch?v=O-vO8QRB5kA",
    
    # ==================== KANNADA SONGS ====================
    "rajeev_shetty": "https://www.youtube.com/watch?v=1FQZR7Rk7dY",
    "karna_nadu": "https://www.youtube.com/watch?v=jT1kN9x6GpA",
    "hebbuli_song": "https://www.youtube.com/watch?v=f0yfUM9ETiM",
    "anjanappa_song": "https://www.youtube.com/watch?v=1lX5u6t6Fok",
}

def get_songs_by_language(language):
    """Filter songs by language category"""
    # This would require metadata, simple implementation for now
    return music

def get_all_song_names():
    """Get all song names in readable format"""
    return [song.replace("_", " ").title() for song in music.keys()]

def search_song(query):
    """Search for a song by partial name match"""
    query = query.lower().replace(" ", "_")
    matches = [song for song in music.keys() if query in song]
    return matches

def get_song_url(song_key):
    """Get URL for a specific song"""
    return music.get(song_key.lower().replace(" ", "_"))

# Total songs count
def get_song_count():
    """Return total number of songs in library"""
    return len(music)