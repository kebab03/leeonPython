#!/usr/bin/python

import http.client
import httplib2
import os

import videoDetails

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

from oauth2client import client # Added
from oauth2client import tools # Added
from oauth2client.file import Storage # Added


# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, http.client.NotConnected,
  http.client.IncompleteRead, http.client.ImproperConnectionState,
  http.client.CannotSendRequest, http.client.CannotSendHeader,
  http.client.ResponseNotReady, http.client.BadStatusLine)

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

CLIENT_SECRETS_FILE = 'client_secrets.json'

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')



def get_authenticated_service(): # Modified
    credential_path = os.path.join('./', 'credential_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, SCOPES)
        credentials = tools.run_flow(flow, store)
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def initialize_upload(youtube, options):
  tags = None
  if options.keywords:
    tags = options.keywords.split(',')

  body=dict(
    snippet=dict(
      title=options.getFileName().split(".", 1)[0],
      description=options.description,
      tags=tags,
      categoryId=options.category
    ),
    status=dict(
      privacyStatus=options.privacyStatus
    )
  )

  # Call the API's videos.insert method to create and upload the video.
  videoPath = "D:\\Videos\%s" % (options.getFileName())
  insert_request = youtube.videos().insert(
    part=','.join(body.keys()),
    body=body,
    media_body=MediaFileUpload(videoPath, chunksize=-1, resumable=True)
  )

  resumable_upload(insert_request)

# This method implements an exponential backoff strategy to resume a
# failed upload.
def resumable_upload(request):
  response = None
  error = None
  retry = 0
  while response is None:

      print('Uploading file...')
      status, response = request.next_chunk()
      if response is not None:
        if 'id' in response:
          print ('Video id "%s" was successfully uploaded.')





if __name__ == '__main__':
  args = videoDetails.Video
  youtube = get_authenticated_service()


  initialize_upload(youtube, videoDetails.Video)

