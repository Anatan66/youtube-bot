import webbrowser
import time

# odkaz na vaše video
video_link = "https://www.youtube.com/watch?v=8cLSJadaxlo&t=14s"

# otevření video v prohlížeči
webbrowser.open(video_link)

import webbrowser
import time

# odkaz na vaše video
video_link = "https://www.youtube.com/watch?v=kvYn7CaTxNk&t=8s"

# otevření video v prohlížeči
webbrowser.open(video_link)

import webbrowser
import time

# odkaz na vaše video
video_link = "https://youtu.be/HnAWsUWG6L8"

# otevření video v prohlížeči
webbrowser.open(video_link)

# otevření video v prohlížeči
webbrowser.open(video_link)

# otevření video v prohlížeči
webbrowser.open(video_link)

# sledování videa po dobu 60 sekund
time.sleep(600)

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CLIENT_SECRETS_FILE = 'client_secret.json'

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def main():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()

    youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    request = youtube.videos().rate(
        id="HnAWsUWG6L8",
        rating="like"
    )
    response = request.execute()

    print("Video bylo úspěšně označeno jako líbivé.")

if __name__ == '__main__':
    main()

from selenium import webdriver
import time

# otevřít webový prohlížeč
driver = webdriver.Chrome()
driver.get('http://www.example.com')

# počkat 60 sekund a poté obnovit stránku
time.sleep(600)
driver.refresh()

# zavřít prohlížeč
driver.quit()
