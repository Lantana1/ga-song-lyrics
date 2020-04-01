# -*- coding: utf-8 -*-

import lyricsgenius
genius = lyricsgenius.Genius("your-Genius-bearer-authtoken-here")

genius.excluded_terms = ["(Remix)", "(Live)", "(Radio)", "(Club)", "(Extended)"]

"""
record_title = "Power, Corruption & Lies"
record_year = "1983"
record_tracklist = [
        "Age of Consent",
        "We All Stand",
        "The Village",
        "586",
        "Your Silent Face",
        "Ultraviolence",
        "Ecstasy",
        "Leave Me Alone"
    ]

#  Note: Genius API for song 4, "5 8 6" Returned -> National Equipment Rental v. Szukhent by\u00a0The\u00a0Supreme Court of the United States (Ft.\u00a0Justice\u00a0Potter Stewart :-(

record_title = "Low Life"
record_year = "1985"
record_tracklist = [
        "Love Vigilantes",
        "The Perfect Kiss",
        "This Time Of Night",
        "Sunrise",
        "Elegia",
        "Sooner Than You Think",
        "Sub-Culture",
        "Face Up"
        ]

record_title = "Brotherhood"
record_year = "1986"
record_tracklist = [
    "Paradise",
    "Weirdo",
    "As It Is When It Was",
    "Broken Promise",
    "Way Of Life",
    "Bizarre Love Triangle",
    "All Day Long",
    "Angel Dust",
    "Every Little Counts"
    ]

record_title = "Technique"
record_year = "1989"
record_tracklist = [
    "Fine Time",
    "All The Way",
    "Love Less",
    "Round & Round",
    "Guilty Partner",
    "Run",
    "Mr. Disco",
    "Vanishing Point",
    "Dream Attack"
    ]

record_title = "Republic"
record_year = "1993"
record_tracklist = [
    "Regret",
    "World",
    "Ruined In A Day",
    "Spooky",
    "Everyone Everywhere",
    "Young Offender",
    "Liar",
    "Chemical",
    "Times Change",
    "Special",
    "Avalanche"
    ]

record_title = "Get Ready"
record_year = "2001"
record_tracklist = [
    "Crystal",
    "60 Miles An Hour",
    "Turn My Way",
    "Vicious Streak",
    "Primitive Notion",
    "Slow Jam",
    "Rock The Shack",
    "Someone Like You",
    "Close Range",
    "Run Wild"
    ]

record_title = "Waiting For The Sirens' Call"
record_year = "2005"
record_tracklist = [
    "Who's Joe?",
    "Hey Now What You Doing",
    "Waiting For The Sirens' Call",
    "Krafty",
    "I Told You So",
    "Morning Night And Day",
    "Dracula's Castle",
    "Jetstream",
    "Guilt Is A Useless Emotion",
    "Turn",
    "Working Overtime"
    ]

record_title = "Lost Sirens"
record_year = "2005"
record_tracklist = [
    "I'll Stay With You",
    "Sugarcane",
    "Recoil",
    "Californian Grass",
    "Hellbent",
    "Shake It Up",
    "I've Got A Feeling",
    "I Told You So (Crazy World Mix)"
    ]

---
band_name = "Joy Division"
record_title = "Unknown Pleasures"
record_year = "1979"
record_tracklist = [
    "Disorder",
    "Day Of The Lords",
    "Candidate",
    "Insight",
    "New Dawn Fades",
    "She’s Lost Control",
    "Shadowplay",
    "Wilderness",
    "Interzone",
    "I Remember Nothing"
    ]
"""

record_title = "Closer"
record_year = "1980"
record_tracklist = [
    "Atrocity Exhibition",
    "Isolation",
    "Passover",
    "Colony",
    "A Means To An End",
    "Heart And Soul",
    "Twenty Four Hours",
    "The Eternal",
    "Decades"
    ]

#artist = genius.search_artist(band_name, max_songs=3)

i = 0
for track in record_tracklist:
    i += 1
    song = genius.search_song(track, band_name)
    song.save_lyrics(str(record_title) + "_" + str(i))
