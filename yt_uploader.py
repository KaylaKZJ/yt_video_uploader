import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

def upload_video(request_body, video_path):
    try:
        # Set up OAuth 2.0 credentials
        scopes = ["https://www.googleapis.com/auth/youtube.upload"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            "client_secrets.json", scopes
        )
        credentials = flow.run_local_server()

        # Build the YouTube API client
        youtube = build("youtube", "v3", credentials=credentials)

        # Upload the video
        media = MediaFileUpload(video_path)
        youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        ).execute()

        print("Video uploaded successfully!")

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
