import sys
import json
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
from google.protobuf.json_format import MessageToDict


# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
  prediction_client = automl_v1beta1.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

def make_prediction(file_path):
  project_id = '832778849297'
  model_id = 'ICN2474837946402865152'

  with open(file_path, 'rb') as ff:
    content = ff.read()

  
  dictionary = MessageToDict(get_prediction(content, project_id, model_id))
  if dictionary:
    response = dictionary['payload'][0]['displayName']
    if response == "iron":
      response = "Ironing is allowed"
    elif response == "donottumbledry":
      response = "Do not tumble dry"
    elif response == "machinewashcold":
      response = "Machine wash cold, at or below 30 °C"
    elif response == "donotwash":
      response = "Do not wash"
    elif response == "nonchlorinebleach":
      response = "Only use non-chlorinated bleach when needed"
    elif response == "machinewashwarm":
      response = "Machine wash warm, at or below 40 °C"
    elif response == "dryclean":
      response = "Dry cleaning is allowed"
    elif response == "machinewashhot":
      response = "Machine wash hot, at or below 50 °C"
    elif response == "donotbleach":
      response = "Do not bleach"
    elif response == "tumbledry":
      response = "Tumble drying is allowed"
    elif response == "donotiron":
      response = "Do not iron"
    elif response == "donotdryclean":
      response = "Do not dry clean"
  else:
    response = "Invalid input!"
  return response

# Test case
# make_prediction('static/simplecv.png')
file_paths = ['sample2/sample2-3.png', 'sample2/sample2-4.png']
for file in file_paths:
  print(make_prediction(file))