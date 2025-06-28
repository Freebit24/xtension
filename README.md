# X-Feed Viewer Extension

A Chrome/Firefox browser extension to view the **X (formerly Twitter)** home feed of any public user who shares their token with you. This tool is intended for read-only access to simulate how someone else's feed looks — just like peeking into their timeline (with permission).

## 🔍 Problem Statement

> Build a **browser extension** that simulates any public user's X feed using their shared login token. The goal is to enable **view-only access** to see what tweets and content your friend sees.

---

## 🧠 Features

- 🔐 View the home feed of any public user who shares their token.
- 🔁 Switch between multiple shared feeds or your own feed.
- 📵 Strictly **read-only** access — no likes, replies, or retweets.
- 🧩 Seamlessly integrates with X.com homepage.
- 🌐 Compatible with **Chrome** and **Firefox**.

---

## 🛠️ Tech Stack

### 🔌 Extension
- HTML, CSS, JavaScript
- `manifest.json` (Manifest v3)
- `popup.html` + `popup.js` for the frontend interface
- `background.js` for persistent background tasks

### 🐍 Backend
- Python with Flask (in `backend/app.py`)
- Requirements listed in `backend/requirements.txt`

---

## 🧪 How It Works

1. The user shares their X login token securely.
2. The extension uses that token to fetch their home feed via network interception or using Twikit APIs.
3. You can toggle between accounts inside the popup.
4. The data is displayed in a simulated feed inside the extension window.

---

## 📦 Folder Structure

```
feed/
├── a.html                      # Sample HTML for feed rendering
├── backend/                   # Python backend (Flask server)
│   ├── app.py                 # Main backend application
│   └── requirements.txt       # Python dependencies
└── extension/                 # Browser extension files
    ├── background.js          # Background script handling events
    ├── manifest.json          # Chrome/Firefox extension manifest
    ├── popup.html             # Popup UI layout
    ├── popup.js               # Logic for popup interactions
    ├── icon.png               # Extension icon
    ├── plus.png               # Additional icon (UI)
    └── trash.png              # Additional icon (UI)
```

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x
- Flask (`pip install -r backend/requirements.txt`)
- Chrome or Firefox browser

---

### 🔧 Running the Backend

```bash
cd feed/backend
pip install -r requirements.txt
python app.py
