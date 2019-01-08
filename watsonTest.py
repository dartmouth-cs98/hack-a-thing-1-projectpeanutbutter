import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource

# service = SpeechToTextV1(url="https://stream.watsonplatform.net/speech-to-text/api", iam_apikey="")

# models = service.list_models().get_result()
# # print(json.dumps(models, indent=2))

# model = service.get_model('en-US_BroadbandModel').get_result()
# # print(json.dumps(model, indent=2))

# with open('jfk.wav', 'rb') as audio_file:
#     recognition = service.recognize(audio=audio_file, content_type='audio/wav').get_result()

# transcripts = list(map(lambda x: x['alternatives'][0]['transcript'], recognition["results"]))
transcripts = ['good evening my fellow citizens this government as promised has maintains the closest surveillance of the Soviet military buildup on the island of Cuba within the past week unmistakable evidence has established the fact that I see reserve offensive missile sites is now in preparation on the imprisoned island the purpose of these bases can be none other than to provide a nuclear strike capability against the western hemisphere ', 'upon receiving the first preliminary hard information of this nature last Tuesday morning at nine AM I directed that our surveillance be stepped up ', 'ends having now confirmed and completed our evaluation of the evidence and our decision on a course of action this government feels obliged to report this new crisis you in the fullest detail ', 'the characteristics of these new missile sites indicate two distinct type of insulations several of them include medium range ballistic missiles capable of carrying a nuclear warhead for a distance of more than one thousand knocked tore all miles ']
text = ''.join(transcripts)
print(text)
