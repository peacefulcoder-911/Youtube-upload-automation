from datetime import datetime, timezone
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os, csv, time

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CLIENT_SECRET_FILE = "client_secrets.json"
CREDENTIALS_FILE = "token.json"


def get_authenticated_service():
    creds = None
    if os.path.exists(CREDENTIALS_FILE):
        creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(CREDENTIALS_FILE, 'w') as token:
            token.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)

def upload_video(file_path, title, description, tags, scheduled_time):
    # Convert scheduled_time to ISO 8601 in UTC
    local_dt = datetime.strptime(scheduled_time, "%Y-%m-%d %H:%M:%S")
    utc_dt = local_dt.astimezone(timezone.utc)
    publish_time = utc_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "private",
            "publishAt": publish_time,
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(file_path)
    request = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media)
    response = request.execute()
    print("✅ Uploaded:", title, "| Scheduled at:", publish_time, "| Video ID:", response['id'])

youtube = get_authenticated_service()

with open("Krishna_Gita_Video_Metadata_Scheduled.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tags = row["tags"].split("|") if row["tags"] else []
        upload_video(
            file_path=row["file_path"],
            title=row["title"],
            description=row["description"],
            tags=tags,
            scheduled_time=row["scheduled_time"]
        )
        time.sleep(5)  # Optional: Delay between uploads

# Keep existing imports and functions...

def upload_video_api(file_path, title, description, tags, scheduled_time):
    youtube = get_authenticated_service()

    local_dt = datetime.strptime(scheduled_time, "%Y-%m-%d %H:%M:%S")
    utc_dt = local_dt.astimezone(timezone.utc)
    publish_time = utc_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "private",
            "publishAt": publish_time,
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(file_path)
    request = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media)
    response = request.execute()
    return response['id']

# 🔒 Add this block so the upload only runs manually
if __name__ == "__main__":
    youtube = get_authenticated_service()
    with open("Krishna_Gita_Video_Metadata_Scheduled.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tags = row["tags"].split("|") if row["tags"] else []
            upload_video_api(
                file_path=row["file_path"],
                title=row["title"],
                description=row["description"],
                tags=tags,
                scheduled_time=row["scheduled_time"]
            )
            time.sleep(5)
