import pyttsx3

textToSpeech = pyttsx3.init()
textToSpeech.say("This is the second problem i have solved. I have made use of external package")

# This will processes the speech event and waits for the speech to finish before continuing

textToSpeech.runAndWait()