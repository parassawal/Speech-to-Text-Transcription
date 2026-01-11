import speech_recognition as sr
import sys
import os

def transcribe_audio(file_path):
    if not os.path.exists(file_path):
        return f"Error: The file '{file_path}' does not exist."

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Error: Could not understand audio"
    except sr.RequestError as e:
        return f"Error: Request failed; {e}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <path_to_audio_file>")
        sys.exit(1)
    
    print(transcribe_audio(sys.argv[1]))
