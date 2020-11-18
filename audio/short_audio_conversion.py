from typing import List, Any, Union

import speech_recognition as sr

filename = "audio.ogg"

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text: Union[List[Any], Any] = r.recognize_google(audio_data)
    print(text)
