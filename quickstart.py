# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# <code>
import json
import azure.cognitiveservices.speech as speechsdk

# Load the configuration from the JSON file
with open('config.json') as config_file:
    config_data = json.load(config_file)

# Extract the subscription key + region
# Creates an instance of a speech config with specified subscription key and service region.
speech_key = config_data.get('subscription_key')
service_region = config_data.get('service_region')
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language="nl-NL")

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Zeg iets...")


# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task returns the recognition text as result. 
# Note: Since recognize_once() returns only a single utterance, it is suitable only for singlehal
# shot recognition like command or query. 
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
result_sTt = speech_recognizer.recognize_once()

# Checks result.
if result_sTt.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result_sTt.text))
elif result_sTt.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result_sTt.no_match_details))
elif result_sTt.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result_sTt.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
speech_config.speech_synthesis_voice_name = "nl-NL-MaartenNeural"

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Receives a text from console input.
print("Type iets wat je uitgesproken wilt hebben...")
text = input()

# Synthesizes the received text to speech.
# The synthesized speech is expected to be heard on the speaker with this line executed.
result_tTs = speech_synthesizer.speak_text_async(text).get()

# Checks result.
if result_tTs.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(text))
elif result_tTs.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result_tTs.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")
# </code>