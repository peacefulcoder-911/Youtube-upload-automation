# 📹 YouTube Upload Automation using Python

This project automates video uploads to a YouTube channel using the **YouTube Data API v3**. It allows developers or content creators to programmatically upload videos, set metadata, and manage privacy settings — all from the command line or an integrated script.

---

## 🚀 Features

- ✅ Upload videos directly to YouTube
- ✏️ Set title, description, tags, category, and privacy
- 📅 Schedule videos or upload immediately
- 🔒 OAuth 2.0 authentication flow for secure access
- 💬 Clean CLI/log messages for automation tracking

---

## 📂 Project Structure

```bash
.
├── app.py                       # Optional main launcher script
├── youtube_upload_automation.py # Core upload logic
├── requirements.txt             # Required Python packages
├── client_secrets.json          # Google API OAuth credentials (ignored in Git)
├── token.json                   # Stores access/refresh tokens (ignored)
├── venv/ or youtube-env/        # Virtual environments (ignored)
├── __pycache__/                 # Python bytecode (ignored)
└── README.md                    # Project documentation



🔧 Setup Instructions
1. 🔑 Get Google API Credentials
Go to Google Cloud Console

Create a project and enable YouTube Data API v3

Go to OAuth Consent Screen → Configure it

Create OAuth 2.0 credentials (client ID + secret)

Download the client_secrets.json and place it in the project root

2. 🛠️ Install Dependencies
Create a virtual environment and install packages:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
3. 🚀 Run the Uploader
bash
Copy
Edit
python youtube_upload_automation.py
The script will:

Trigger OAuth login (first-time only)

Upload your video with metadata

Print success or error messages