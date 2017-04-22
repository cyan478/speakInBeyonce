import os

def parse():

    dSongs = {}

    for filename in os.listdir('songs'):
        f = open("songs/" + filename, "r")
        lines = f.readlines()
        f.close()

        title = lines[0]
        dEmotions = {}
        joyL = []
        angerL = []
        disgustL = []
        sadL = []
        fearL = []

        for l in lines:
            angerL.append({0.5 : "lyric"})

        dEmotions["j"] = joyL
        dEmotions["a"] = angerL
        dEmotions["d"] = disgustL
        dEmotions["s"] = sadL
        dEmotions["f"] = fearL

        dSongs[title] = dEmotions

    print dSongs

parse()
