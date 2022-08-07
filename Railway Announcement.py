import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename):
   mytext = str(text)
   language = 'en'
   myjob = gTTS(text=mytext, lang=language, slow= False)
   myjob.save(filename)

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios :
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

# 1 - Generate: intro sound
    start = 0000
    finish = 1500
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_eng.mp3", format="mp3")
   
    audio = AudioSegment.from_mp3('railway_eng.mp3')
# 2 - Generate: May i have your attention please,Train number
    start = 0000
    finish = 3200
    audioProcessed = audio[start:finish]
    audioProcessed.export("2_eng.mp3", format="mp3")

# 3 - train number and name
    
# 4 - Generate: From
    start = 8000
    finish = 8790
    audioProcessed = audio[start:finish]
    audioProcessed.export("4_eng.mp3", format="mp3")
# 5- from city

# 6 - Generate: To
    start = 9940
    finish = 10390
    audioProcessed = audio[start:finish]
    audioProcessed.export("6_eng.mp3", format="mp3")
# 7- To city
    
# 8 - Generate: Via
    start = 10800
    finish = 11700
    audioProcessed = audio[start:finish]
    audioProcessed.export("8_eng.mp3", format="mp3")
# 9 - via city

# 10 - Generate: Will depart from platform number
    start = 13000
    finish = 15250
    audioProcessed = audio[start:finish]
    audioProcessed.export("10_eng.mp3", format="mp3")
# 11 - Platform number

# 12 - Generate: At its scheduled time
    start = 15900
    finish = 17600
    audioProcessed = audio[start:finish]
    audioProcessed.export("12_eng.mp3", format="mp3")

    audio = AudioSegment.from_mp3('railway.mp3')

# 13 - Generate: outro sound
    start = 200
    finish = 1500
    audioProcessed = audio[start:finish]
    audioProcessed.export("13_eng.mp3", format="mp3")

def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index , item in df.iterrows():
        # 3- Generate-train number and name
        textToSpeech(item["train_no"] + " " + item["train_name"],"3_eng.mp3")
        #5-Generate-from city
        textToSpeech(item["from"],"5_eng.mp3")
        #7-Generate-To city
        textToSpeech(item["to"],"7_eng.mp3")
        #9-Generate-via city
        textToSpeech(item["via"],"9_eng.mp3")
        #11-Generate-Platform number
        textToSpeech(item["platform"],"11_eng.mp3")

        audios= [f"{i}_eng.mp3" for i in range(1,14)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_name']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcements...")
    generateAnnouncement("announce_eng.xlsx")