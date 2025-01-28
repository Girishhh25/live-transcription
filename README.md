## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
   Live Audio Transcription with Whisper
This project provides real-time transcription of audio using OpenAI's Whisper and streams the transcription in JSON format. It captures audio from your computer (or pre-recorded audio) and processes it into text that can be easily integrated into other applications.

Features
Real-Time Transcription: Uses Whisper for accurate transcription of live audio.
JSON Output: Outputs transcriptions in JSON format for easy integration into other systems.
FFmpeg Support: Leverages FFmpeg for audio capture and processing.
Electron Functions: Provides UI-like functionality without a full-fledged Electron app.

Requirements
Python 3.10 or later
Node.js and npm (for Electron functionality)
FFmpeg (required for audio capture)

Dependencies:
Python: Install packages listed in requirements.txt
Node.js: Install necessary packages with npm install

Setup Instructions

Step 1: Clone the Repository
git clone https://github.com/yourusername/live-transcription-app.git
cd live-transcription

Step 2: Install Dependencies
1. Install Python Dependencies
Create a virtual environment (optional but recommended):
python -m venv env
source env/bin/activate    # On Windows: .\env\Scripts\activate

Install Python packages:
pip install -r requirements.txt

2. Install Node.js Dependencies
npm install

Step 3: Ensure FFmpeg is Installed
Verify FFmpeg is installed by running:
ffmpeg -version

If FFmpeg is not installed:

Windows: Download FFmpeg and add it to your system's PATH.

Linux: Install via:
sudo apt install ffmpeg

MacOS: Install via Homebrew:
brew install ffmpeg

Step 4: Test the Setup
1. Run the Python Transcription Script

Start the transcription service:
python main.py
The script will start listening for audio input.

2. Test with Pre-Recorded Audio (Optional)
Modify main.py to use a pre-recorded audio file:
audio_path = "path/to/audio/file.wav"
result = model.transcribe(audio_path)
print(result["text"])
Replace "path/to/audio/file.wav" with the actual path to your audio file.

How to Use
Live Audio Transcription
Start the script:
python main.py
Provide audio input:
Speak or play audio on your computer.
The transcription will appear in real-time.

Output Format
The transcription data will be sent in JSON format, for example:
{
  "timestamp": "2025-01-28T12:34:56",
  "text": "This is a sample transcription."
}

Pre-Recorded Audio Transcription
Place your audio file in the project directory.
Modify main.py as shown above and run the script to get transcription.
Electron Functions
The project includes Electron-related functionality for integration and UI-like behavior. While this is not a full Electron app, the functions allow for interaction and testing:

Start the Electron Functionality:
npm start

Troubleshooting
1. No Transcription Output
Ensure your audio input is working.
Verify FFmpeg is installed and accessible via PATH.
Check for errors in the Python script logs.

2. FFmpeg Not Found
Add FFmpeg to your system PATH or reinstall it.
Verify its installation with ffmpeg -version.

3. Python Errors
Ensure you're using Python 3.10+.
Activate the virtual environment before running main.py.

