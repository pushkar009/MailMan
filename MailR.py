import os.path
import base64
from email.message import EmailMessage
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def gmail_auth():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def send_email():
    creds = gmail_auth()
    service = build('gmail', 'v1', credentials=creds)

    message = EmailMessage()
    message.set_content("----------------------")

    message['To'] = 'recipient@example.com'
    message['From'] = 'me'
    message['Subject'] = 'Subject'

    # Attach the file
    file_path = 'filename.xlsx'
    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)
    message.add_attachment(file_data, maintype='application', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=file_name)

    # Encode and send
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    send = {'raw': encoded_message}
    service.users().messages().send(userId='me', body=send).execute()

if __name__ == '__main__':
    send_email()
