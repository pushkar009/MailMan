# MailR
<b>MailR </b> is a gmail automation bot that you can use for automating your mails.
## What it does
1. Logs into Gmail account securely.
2. Automates sending your report files (*.xlsx)

## Requirements
You can download requirements by running `libraries.bat` file or executing following in your terminal:
```
pip install -r requirements.txt
```

## 🌐Setup Gmail Access

### Step 1: Go to [Google Cloud Console](https://console.cloud.google.com)
* Click "Select a Project" → "New Project"
* Name: ```Gmail Bot```

### Step 2: Enable the Gmail API:
* In the sidebar: ```APIs & Services > Library```
* Search for “Gmail API” → Click it → Click Enable

### Step 3: Set up OAuth consent:
* Go to ```APIs & Services > OAuth Consent Screen```
* Go to <b>Branding</b>
* Fill out required fields (like app name, email, etc.) click save
* Choose External in <b>Audience</b> (it's just for you)

1. Scroll to “Test Users” section.
2. Click Add Users.
3. Enter the email address you’re using to run the script (e.g., your Gmail account).
4. Click Save.

This tells Google: “Hey, it’s okay, I trust this bot. It's just me using it for now.”

### Step 4: Create OAuth Credentials:
* Go to ```APIs & Services > Credentials```
* Click "Create Credentials" > "OAuth Client ID"
* App type: ```Desktop app```
* Click Create and then Download the ```credentials.json``` file

<b>Note:</b>Save this credentials.json file in the same folder as your Python script.

### Step 5: First Time Authorization
Run the script once manually:
`` python gmail_bot.py ``
You’ll get a Google login popup to give permission. After that, it will save a token.json file for future use—so no popup next time.
