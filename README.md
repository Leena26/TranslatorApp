# TranslatorApp

# AI Voice Translator 🌍🔊

A web-based translation application built with **Flask** that translates text between multiple languages and converts the result into high-quality AI speech using **ElevenLabs**.

## 🚀 Features
- **Bi-directional Translation:** Select both source and target languages via a dynamic dropdown menu.
- **AI Text-to-Speech:** Generates natural-sounding audio for translations using the ElevenLabs Multilingual v2 model.
- **Interactive UI:** A clean, centered interface with a "Listen" button to trigger audio playback.
- **Dynamic Configuration:** Languages are managed via a central `languages.json` file for easy updates.

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3 (Flexbox), JavaScript
- **APIs:** - [MyMemory](https://mymemory.translated.net/) (Translation)
  - [ElevenLabs](https://elevenlabs.io/) (Text-to-Speech)

## 📋 Prerequisites
- Python 3.x
- An ElevenLabs API Key
- A valid ElevenLabs Voice ID (e.g., "Rachel")

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd TranslationApp
   ```
2. Install Dependencies
   ```
   pip install flask requests python-dotenv
   ```
3. Create a .env file in the root directory and add your credentials:
   - AUDIO_APIKEY=your_elevenlabs_api_key_here
   - VOICE_ID=your_chosen_voice_id
4. Ensure you have a static folder for the audio output:
    ```mkdir static```
5. Run the Application:
   ```python translate.py```

Access the app at http://127.0.0.1:5000. 

##📝 Usage
 - Type the text you want to translate in the left box.
 - Select your Starting Language and Target Language.
 - Click Translate.
 - Once the translation appears, click the 🔊 Listen button to hear it.

## Project Structure
├── translate.py        # Main Flask application logic
├── languages.json      # List of supported language codes and names
├── .env                # Private API keys (do not commit to GitHub)
├── templates/
│   └── index.html      # Main web interface
└── static/
    ├── style.css       # Custom styling
    └── output.mp3      # Generated speech file (temp)



