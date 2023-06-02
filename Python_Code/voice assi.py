from __future__ import print_function
import  os
import  time
import playsound
import  speech_recognition as sr
from gtts import gTTS



import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


import subprocess



from time import sleep


def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

def get_audio ():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        audio =r.listen(source)
        said=""

        try:
            said =r.recognize_google(audio)
            print("you said:",said)
        except Exception as e:
            print("Exception:"+str(e))
    return  said
# text = get_audio()
# if "hello " in text :
#     speak("hello ,how are you")
#
# if "what is your name " in text:
#     speak("my name is Tim ")
def speak(text):
    tts= gTTS(text=text,lang="en")
    date = datetime.datetime.now()
    filem = str(date).replace(":", "-")
    filename= filem+".mp3"
    tts.save(filename)

    playsound.playsound(filename)

def note(text):
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "" \
                                                  "-note.txt"
        with open(file_name, "a") as f:
            f.write(text)
            # WORD="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.exe"
            subprocess.Popen(["notepad.exe", file_name])

            #         subprocess.Popen(WORD)

service = authenticate_google()
# speak(" welcome "
#       )
# speak("how are you")
# speak("My name is Tim"
#           )
#
#
#
#     # Call the Calendar API
# # def get_events(n,service):
# #     now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
# #     print(f'Getting the upcoming {n} events')
# #     events_result = service.events().list(calendarId='primary', timeMin=now,
# #                                         maxResults=n, singleEvents=True,
# #                                         orderBy='startTime').execute()
# #     events = events_result.get('items', [])
#
#     # if not events:
#     #     print('No upcoming events found.')
#     # for event in events:
#     #     start = event['start'].get('dateTime', event['start'].get('date'))
#     #     print(start, event['summary'])
#
#
# # get_events(2,service)
#
print("20 ms per dire  hello  oppure how are you 1 sola votla")
sleep(5)
print("ora ")
text = get_audio()
# note(text)
print("2 ms per verifica di speak")
sleep(2)
print("test:",text)
if "hello " in str(text):

    speak("how are you")
if "what is your name" in text:
    speak("My name is Tim"
           )
#
# #note("leeon tutoria da tech with tim file 8 open")
# # NOTE_STRS =   ["MAKE A NOTE ".lower(),"Write THIS NOTE","rim this"]
#
NOTE_STRS = ["make a note ","write this "]
# # import time
# # while True:
# #     print("10 ms per dire make a note o write this")
# #     time.sleep(10)
#
print("10 ms per dire make a note o write this")
sleep(10)
print(" di make a note")
text1 = get_audio()
note(text1)
for phrase in NOTE_STRS:
    if phrase in text1:
         speak("what you like to wirte")
         note_text = get_audio()

         note(note_text)
         speak("i have made note ")
print(5)