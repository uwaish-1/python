import speech_recognition as sr
import webbrowser
import musiclibrary
import pyttsx3

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

if __name__ == "__main__":
    while True:
        # listen for the wake word jarvis
        r = sr.Recognizer()

        try:
            # obtain audio from the microphone
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            print("Recognizing...")

            command = r.recognize_google(audio)
            print("You said: " + command)

            if "open google" in command.lower():
                webbrowser.open("https://www.google.com")
                speak("Opening Google")

            elif "open youtube" in command.lower():
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube")

            elif "play music" in command.lower():
                speak("What song would you like to listen to?")

                with sr.Microphone() as source:
                    audio = r.listen(source, timeout=2, phrase_time_limit=3)

                song = r.recognize_google(audio).lower()

                if song in musiclibrary.music:
                    webbrowser.open(musiclibrary.music[song])
                    speak(f"Playing {song}")
                else:
                    speak("Sorry, I don't have that song.")

            elif "exit" in command.lower():
                speak("Goodbye!")
                break

            else:
                speak("Sorry, I didn't understand that command.")

        except Exception as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}"
                .format(e)
            )