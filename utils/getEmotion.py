import os
import urllib
import json
from watson_developer_cloud import ToneAnalyzerV3

def getEmotion(s):
    tone_analyzer = ToneAnalyzerV3(
       username='53dd40c5-f790-493c-bf5f-4e271c23aa0b',
       password='IeQal50rwMC6',
       version='2016-05-19')

    results = json.dumps(tone_analyzer.tone(text=s))
    results = json.loads(results)
    results = results["document_tone"]["tone_categories"][0]["tones"]
    emotions = {}

    emotions[results[0]["score"]] = "anger"
    emotions[results[1]["score"]] = "disgust"
    emotions[results[2]["score"]] = "fear"
    emotions[results[3]["score"]] = "joy"
    emotions[results[4]["score"]] = "sad"
    #print results
    maxEmotion = sorted(emotions)
    e = emotions[maxEmotion[-1]]
    return {e : maxEmotion[-1]}

def parse():

    dSongs = {}

    for filename in os.listdir('utils/songs'):
        f = open("utils/songs/" + filename, "r")
        lines = f.readlines()
        f.close()

        title = lines[0]
        dEmotions = {}
        joyL = []
        angerL = []
        disgustL = []
        sadL = []
        fearL = []

        for l in lines[1:]:
            emotion = getEmotion(l)
            key = emotion.keys()[0]
            value = emotion.values()[0]
            if key == "joy":
                joyL.append({value : l})
            elif key == "anger":
                angerL.append({value : l})
            elif key == "disgust":
                disgustL.append({value : l})
            elif key == "sad":
                sadL.append({value : l})
            elif key == "fear":
                fearL.append({value : l})

        dEmotions["joy"] = joyL
        dEmotions["anger"] = angerL
        dEmotions["disgust"] = disgustL
        dEmotions["sad"] = sadL
        dEmotions["fear"] = fearL

        dSongs[title] = dEmotions

    with open('utils/result_test.txt', 'w') as outfile:
        json.dump(dSongs, outfile)
        outfile.close()

def getMatch(input):
    inputD = getEmotion(input)
    key = inputD.keys()[0] #emotion
    val = inputD.values()[0] #num

    #print val
    f = open("utils/result_test.txt", "r")
    text = f.read()
    f.close()
    result = json.loads(text)

    minVal = result[result.keys()[0]][key][0].values()[0]
    #print minVal

    possibleL = []

    for k in result:
        for line in result[k]:
            if line == key:
                for entry in result[k][line]:
                    possibleL.append(entry)
                    #print minVal
                    #print entry

    possibleL = sorted(possibleL)
    #print possibleL

    first = possibleL[0].keys()[0]
    first = float(first)
    absVal = abs(val - first)

    for element in possibleL:
        #print element
        entryVal = float(element.keys()[0])
        newVal = abs(val - entryVal)
        if newVal > absVal:
            break
        absVal = newVal
        #print newVal
        minVal = element.values()[0]

    #print val
    return minVal

#sparse("7_11.txt")
#parse()
#print getMatch("i hate him")
