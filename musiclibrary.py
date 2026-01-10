"""Music Library for Orion Voice Assistant"""

# Music database with YouTube links
music = {
    # ==================== ENGLISH SONGS ====================
    # Original Pop/Rock
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
    
    # New English Songs (10 additional)
    "as_it_was": "https://www.youtube.com/watch?v=H5v3kKSFVQE",
    "flowers": "https://www.youtube.com/watch?v=OPf0YbXqDm0",
    "anti_hero": "https://www.youtube.com/watch?v=r7zBmKVGQSk",
    "heat_waves": "https://www.youtube.com/watch?v=mRD0WrmXF-M",
    "good_4_u": "https://www.youtube.com/watch?v=SzCp7fz95Oo",
    "without_me": "https://www.youtube.com/watch?v=V1Pl8CzNzCw",
    "someone_you_loved": "https://www.youtube.com/watch?v=1-xGerv5FOk",
    "falling": "https://www.youtube.com/watch?v=NOuBjPmg4Kk",
    "bohemian_rhapsody": "https://www.youtube.com/watch?v=fJ9rUzIMt7o",
    "stairway_to_heaven": "https://www.youtube.com/watch?v=QkF3G8mB8OQ",
    
    # Additional English Songs (10 more)
    "imagine": "https://www.youtube.com/watch?v=YkADj74e7M8",
    "hotel_california": "https://www.youtube.com/watch?v=EqLBSOQeZWw",
    "thriller": "https://www.youtube.com/watch?v=sOnqjkSntDY",
    "like_a_virgin": "https://www.youtube.com/watch?v=p-Z3YrHJ1uI",
    "hey_jude": "https://www.youtube.com/watch?v=A47-zlqnWqE",
    "sweet_child_o_mine": "https://www.youtube.com/watch?v=1w7OgIMMRc4",
    "smells_like_teen_spirit": "https://www.youtube.com/watch?v=hTWKbfoikeg",
    "one": "https://www.youtube.com/watch?v=WM8bTpUjweA",
    "enter_sandman": "https://www.youtube.com/watch?v=CD-E-LDc384",
    "comfortably_numb": "https://www.youtube.com/watch?v=_FrXqUzHuzY",
    
    # ==================== HINDI SONGS ====================
    # Original Hindi Songs
    "kesariya": "https://www.youtube.com/watch?v=Is5hox8Wprc",
    "tum_hi_ho": "https://www.youtube.com/watch?v=Umqb9KENgmk",
    "shayad": "https://www.youtube.com/watch?v=7IiJUpn4Rug",
    "levi_ki_adi": "https://www.youtube.com/watch?v=5e6EcWxkbgI",
    "dil_bechara": "https://www.youtube.com/watch?v=nU7qFN0Rzdg",
    "raabta": "https://www.youtube.com/watch?v=O-vO8QRB5kA",
    
    # New Hindi Songs (10 additional)
    "ae_zindagi": "https://www.youtube.com/watch?v=wlcIINCLgYo",
    "chaleya": "https://www.youtube.com/watch?v=YUi3LAa-0Ns",
    "bekhayali": "https://www.youtube.com/watch?v=oAKqVNtDC10",
    "tera_intezaar": "https://www.youtube.com/watch?v=3YpYb5PBqC8",
    "pachtaoge": "https://www.youtube.com/watch?v=4p_QM_3bPqQ",
    "kabira": "https://www.youtube.com/watch?v=l_cc5rNz5GE",
    "malhari": "https://www.youtube.com/watch?v=l_cc5rNz5GE",
    "aajedo_parwah": "https://www.youtube.com/watch?v=oI_p8VYc2hM",
    "main_tera_hero": "https://www.youtube.com/watch?v=x_D85jZcqOA",
    "gerua": "https://www.youtube.com/watch?v=l_cc5rNz5GE",
    
    # Additional Hindi Songs (10 more)
    "baarish": "https://www.youtube.com/watch?v=kJSvxM1kO7Y",
    "yaad_piya_ki_aaye": "https://www.youtube.com/watch?v=rJ6-VzLkqrM",
    "tune_mere_jaana": "https://www.youtube.com/watch?v=m5RpBY3tPpQ",
    "mere_sapnon_ki_rani": "https://www.youtube.com/watch?v=Jz49wgJ3fls",
    "lag_ja_gale": "https://www.youtube.com/watch?v=eL51wI4U9DY",
    "abhi_na_jao_chod_kar": "https://www.youtube.com/watch?v=2K5XC8wxVqY",
    "mere_dil_ki_sunoj": "https://www.youtube.com/watch?v=Mg6VqqL-Jqo",
    "kuch_to_log_kahenge": "https://www.youtube.com/watch?v=bX9yyDdK1g4",
    "janam_janam_se": "https://www.youtube.com/watch?v=BfFWMxRANOU",
    "raaste_hain_mushkil": "https://www.youtube.com/watch?v=gzPAe_hHR5I",
    
    # ==================== KANNADA SONGS ====================
    # Original Kannada Songs
    "rajeev_shetty": "https://www.youtube.com/watch?v=1FQZR7Rk7dY",
    "karna_nadu": "https://www.youtube.com/watch?v=jT1kN9x6GpA",
    "hebbuli_song": "https://www.youtube.com/watch?v=f0yfUM9ETiM",
    "anjanappa_song": "https://www.youtube.com/watch?v=1lX5u6t6Fok",
    
    # New Kannada Songs (10 additional)
    "aadharashangara": "https://www.youtube.com/watch?v=Y_T3F_dIBkk",
    "nee_partha_vizhigal": "https://www.youtube.com/watch?v=XC2F4P0mUWk",
    "chandamama_raaga": "https://www.youtube.com/watch?v=qI0c6xrxbh0",
    "neene_ninne": "https://www.youtube.com/watch?v=TwPdzLAFM3I",
    "muggu_muggu": "https://www.youtube.com/watch?v=c8Jmti4j3H0",
    "usire_usire": "https://www.youtube.com/watch?v=9BT1YHH3-OY",
    "nannage_nannage": "https://www.youtube.com/watch?v=CqGZFw6yqpE",
    "tilak_kannada": "https://www.youtube.com/watch?v=6pLtQwvXfh4",
    "ye_kannada_manege": "https://www.youtube.com/watch?v=JcdV3qh29zY",
    "ganapa_gananayaka": "https://www.youtube.com/watch?v=VSsozVGZqaM",
    
    # Additional Kannada Songs (10 more)
    "manjula_gururaja": "https://www.youtube.com/watch?v=fvvg0LrU0mg",
    "nodu_kannu": "https://www.youtube.com/watch?v=g6T_BqTBLSE",
    "ulidavva_ulidavva": "https://www.youtube.com/watch?v=HdNb_3dHsgo",
    "kunidhi_kunidhi": "https://www.youtube.com/watch?v=JzKc-5jxJQI",
    "malaya_maruta": "https://www.youtube.com/watch?v=eXWfKgJLl4w",
    "kanokkana": "https://www.youtube.com/watch?v=gA0YMfqLXCQ",
    "nanna_kandha": "https://www.youtube.com/watch?v=b3rPFvzJBvg",
    "yaakshagana_padya": "https://www.youtube.com/watch?v=VXLXCqEHpYU",
    "raaga_sudha": "https://www.youtube.com/watch?v=nOiXeJEhkCw",
    "suddha_dhanyasi": "https://www.youtube.com/watch?v=1n5-Moz-Ir4",
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