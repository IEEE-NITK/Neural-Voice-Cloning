from flask import Flask, jsonify
import speech_recognition as sr
import time
import sys

import logging
try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    print(sys.path)
    return "Hello"


@app.route('/test')
def compute():
    r = sr.Recognizer()
    with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            print("s")
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))

    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


@app.route('/recognize/<int:id>')
def hello_world(id):
    print(id)
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # get a random word from the list
    # word = random.choice(WORDS)
    s1 = 'apple banana orange grapes'
    s2 = 'apple banana orange grapes'
    s3 = 'apple banana orange grapes'
    s4 = 'apple banana orange grapes'
  
    print('say something')
    guess = recognize_speech_from_mic(recognizer, microphone,id)
    #print(guess)
    if guess["error"]:
        message = "ERROR"
    message = "You said: {}".format(guess["transcription"])
    string = format(guess["transcription"])

    #CALL FUNCTION
    #string_class = func(string)
    result = {'result':False}
    ans = guess["transcription"]


    if ans != None:
        if id == 1:
            if s1.lower() == ans.lower():
                print(ans)
                result = {'result':True}
            else:
                print("no")
                result = {'result':False}
        if id == 2:
            if s2.lower() == ans.lower():
                print(ans)
                result = {'result':True}
            else:
                print("no")
                result = {'result':False}

        if id == 3:
            if s3.lower() == ans.lower():
                print(ans)
                result = {'result':True}
            else:
                print("no")
                result = {'result':False}

        if id == 4:
            if s4.lower() == ans.lower():
                print(ans)
                result = {'result':True}
            else:
                print("no")
                result = {'result':False}

    else:
        print("None")
        result = {'result':False}

    
    print("You said: {}".format(guess["transcription"]))
    return jsonify(result)



def recognize_speech_from_mic(recognizer, microphone,id):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    if id == 1:
        with open("1.wav", "wb") as f:
            print("1")
            f.write(audio.get_wav_data())
    elif id == 2:
        with open("2.wav", "wb") as f:
            print("2")
            f.write(audio.get_wav_data())
    elif id == 3:
        with open("3.wav", "wb") as f:
            print("3")
            f.write(audio.get_wav_data())
    else:
        with open("4.wav", "wb") as f:
            print("4")
            f.write(audio.get_wav_data())
   

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    
    
    return response