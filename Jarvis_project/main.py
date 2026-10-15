# import speech_recognition as sr
# import webbrowser
# import musiclibrary
# import pyttsx3

# recognizer = sr.Recognizer()
# ttsx = pyttsx3.init()


# def speak(text):
#     ttsx.say(text)
#     ttsx.runAndWait()


# if __name__ == "__main__":

#     speak("Initializing Jarvis")

#     while True:
#         try:
#             # Keep the microphone open while listening
#             with sr.Microphone() as source:
#                 print("Listening for wake word...")

#                 # Optional: reduce background noise
#                 recognizer.adjust_for_ambient_noise(source, duration=0.5)

#                 print("Recognizing...")
#                 audio = recognizer.listen(
#                     source,
#                     timeout=5,
#                     phrase_time_limit=5
#                 )

#             # Convert speech to text
#             command = recognizer.recognize_google(audio)
#             command = command.lower()

#             print("You said:", command)

#             if "open google" in command:
#                 speak("Opening Google")
#                 webbrowser.open("https://www.google.com")

#             elif "open youtube" in command:
#                 speak("Opening YouTube")
#                 webbrowser.open("https://www.youtube.com")

#             elif command.startswith("play music"):
#                 # Example: "play music shape of you"
#                 song = command.replace("play music", "").strip()[2]

#                 if song in musiclibrary.music:
#                     speak(f"Playing {song}")
#                     webbrowser.open(musiclibrary.music[song])
#                 else:
#                     speak("Sorry, I could not find that song.")
            # elif command.startswith("play music"):
            #     song = command.replace("play music", "").strip()

            #     print("Song detected:", song)
            #     print("Available songs:", musiclibrary.music.keys())

            #     if song in musiclibrary.music:
            #         speak(f"Playing {song}")
            #         webbrowser.open(musiclibrary.music[song])
            #     else:
            #         speak(f"Sorry, {song} is not in your music library.")

        #     elif "exit" in command:
        #         speak("Goodbye!")
        #         break

        #     else:
        #         speak("Sorry, I didn't understand that command.")

        # except sr.WaitTimeoutError:
        #     print("No speech detected.")

        # except sr.UnknownValueError:
        #     print("Could not understand the audio.")

        # except sr.RequestError as e:
        #     print(f"Could not connect to Google Speech Recognition: {e}")

        # except Exception as e:
        #     print(f"Error: {e}")


import speech_recognition as sr
import webbrowser
import musiclibrary
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()


def speak(text):
    print("Jarvis:", text)
    ttsx.say(text)
    ttsx.runAndWait()


if __name__ == "__main__":

    speak("Initializing Jarvis")
    speak("Jarvis is ready")

    while True:
        try:
            # Listen from microphone
            with sr.Microphone() as source:
                print("\nListening for wake word...")
                
                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            print("Recognizing...")

            command = recognizer.recognize_google(audio)
            command = command.lower()

            print("You said:", command)

            # ---------------- OPEN GOOGLE ----------------
            if "open google" in command:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")

            # ---------------- OPEN YOUTUBE ----------------
            elif "open youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")

            # ---------------- PLAY MUSIC ----------------
            elif "play music" in command:

                speak("What song would you like to listen to?")

                with sr.Microphone() as source:
                    print("Listening for song name...")

                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=5
                    )

                song = recognizer.recognize_google(audio).lower()
                song = song.lower().split(" ")[1]  # Normalize the song name

                print("Song requested:", song)

                if song in musiclibrary.music:
                    speak(f"Playing {song}")
                    webbrowser.open(musiclibrary.music[song])
                else:
                    speak(
                        "Sorry, I don't have that song in my music library."
                    )
            elif command.lower().startswith("play music"):
                song = command.lower().split(" ")[1]
                link = musiclibrary.music[song]
                webbrowser.open(link)

            # ---------------- EXIT ----------------
            elif (
                "exit" in command
                or "quit" in command
                or "bye" in command
            ):
                speak("Goodbye. Have a nice day.")
                break

            # ---------------- UNKNOWN ----------------
            # else:
            #     speak("Sorry, I didn't understand that command.")

        # If no speech is detected
        except sr.WaitTimeoutError:
            print("No speech detected.")

        # If speech cannot be understood
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")

        # Internet/API error
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech "
                f"Recognition service: {e}"
            )

        # Other errors
        except Exception as e:
            print("Error:", e)