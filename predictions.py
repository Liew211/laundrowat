import sys

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
  prediction_client = automl_v1beta1.PredictionServiceClient()

  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

file_path = ['sample1-1.jpg', 'sample1-2.png','sample1-3.png', 'sample1-4.png', 'sample1-5.png']
project_id = '832778849297'
model_id = 'ICN2474837946402865152'

for file in file_path:
  with open(file, 'rb') as ff:
      content = ff.read()

  print(get_prediction(content, project_id, model_id))