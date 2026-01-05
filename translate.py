from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests
import os
import json

load_dotenv()
with open('static/languages.json', 'r') as f:
    SUPPORTED_LANGUAGES = json.load(f)

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    translated = None
    if request.method == 'POST' and request.form.get("initial_text") != "":
        text = request.form.get("initial_text")
        source = request.form.get("source_lang")
        target = request.form.get("target_lang")
            
        url = f"https://api.mymemory.translated.net/get?q={text}&langpair={source}|{target}"
        
        response = requests.get(url).json()
        matchValue = response['responseData']['match']
        translatedText = response['responseData']['translatedText']
        
        
        apiKey = os.getenv("AUDIO_APIKEY")
        voice = os.getenv("VOICE_ID")
        tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"
        
        headers = {
            "xi-api-key": apiKey,
            "Content-Type": "application/json"
        }
        
        data = {
            "text" : translatedText,
            "match" : matchValue,
            "model_id" : "eleven_multilingual_v2", # v2 supports Italian
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
        }
        
        audio_response = requests.post(tts_url, json=data, headers=headers)
        if audio_response.status_code == 200:
            # Save the audio file to your static folder
            with open("static/output.mp3", "wb") as f:
                f.write(audio_response.content)
            
            translated = {
                "text": translatedText,
                "match" : matchValue,
                "audio": True
            }
        else:
            translated = {
                "text": translatedText,
                "match" : matchValue
            }  
    else:
        translated = None
    
    return render_template('index.html',  translate = translated, languages=SUPPORTED_LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
        