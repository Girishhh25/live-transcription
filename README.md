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
bash
Copy
Edit
git clone https://github.com/yourusername/live-transcription-app.git
cd live-transcription-app
Step 2: Install Dependencies
1. Install Python Dependencies
Create a virtual environment (optional but recommended):
bash
Copy
Edit
python -m venv env
source env/bin/activate    # On Windows: .\env\Scripts\activate
Install Python packages:
bash
Copy
Edit
pip install -r requirements.txt
2. Install Node.js Dependencies
Navigate to the Electron function folder:
bash
Copy
Edit
cd electron-function/
npm install
cd ..
Step 3: Ensure FFmpeg is Installed
Verify FFmpeg is installed by running:
bash
Copy
Edit
ffmpeg -version
If FFmpeg is not installed:
Windows: Download FFmpeg and add it to your system's PATH.
Linux: Install via:
bash
Copy
Edit
sudo apt install ffmpeg
MacOS: Install via Homebrew:
bash
Copy
Edit
brew install ffmpeg
Step 4: Test the Setup
1. Run the Python Transcription Script
Start the transcription service:
bash
Copy
Edit
python main.py
The script will start listening for audio input.
2. Test with Pre-Recorded Audio (Optional)
Modify main.py to use a pre-recorded audio file:
python
Copy
Edit
audio_path = "path/to/audio/file.wav"
result = model.transcribe(audio_path)
print(result["text"])
Replace "path/to/audio/file.wav" with the actual path to your audio file.
How to Use
Live Audio Transcription
Start the script:
bash
Copy
Edit
python main.py
Provide audio input:
Speak or play audio on your computer.
The transcription will appear in real-time.
Output Format
The transcription data will be sent in JSON format, for example:
json
Copy
Edit
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
bash
Copy
Edit
npm start
Interact with the UI:
Click on the Start Transcription button in the Electron window (if configured).
Check the Developer Tools console for logs and output.
Project Structure
plaintext
Copy
Edit
live-transcription-app/
├── main.py                   # Python transcription script
├── requirements.txt          # Python dependencies
├── electron-function/        # Electron-related Node.js functionality
│   ├── package.json          # Node.js package file
│   ├── index.js              # Node.js entry point (if applicable)
│   ├── ...
├── README.md                 # Project documentation
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
How to Push the Project to GitHub
Initialize the repository (if not already):

bash
Copy
Edit
git init
git remote add origin https://github.com/yourusername/live-transcription-app.git
Add all files and commit:

bash
Copy
Edit
git add .
git commit -m "Initial commit"
Push to GitHub:

bash
Copy
Edit
git branch -M main
git push -u origin main
