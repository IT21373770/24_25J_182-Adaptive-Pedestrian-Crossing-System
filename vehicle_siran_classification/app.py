from flask import Flask, request, jsonify
import numpy as np
import librosa
import pickle
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

print("loading model")
model = load_model('Content/cnn_model.h5')

with open('Content/label_encoder.pkl', 'rb') as f:
   label_encoder = pickle.load(f)

def features_extractor(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=80)
    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)
    return mfccs_scaled_features

@app.route('/predict',methods=['POST'])
def predict():
	print("Request files:", request.files)
	file = request.files['file']
	print("work here 2")
	if not file.filename.endswith('.wav'):
		 return jsonify({'error': 'Unsupported file format. Please upload a .wav file'}), 400

	try:
		file_path ="Content/sound_205.wav"
		file.save(file_path)

		features = features_extractor(file_path)
		features = features.reshape(1, -1, 1)

		# Make prediction
		predictions = model.predict(features)
		predicted_class = np.argmax(predictions, axis=1)
		class_label = label_encoder.inverse_transform(predicted_class)
		print(class_label)
		return jsonify({'predicted_class': class_label[0]}), 200

	except Exception as e:
	  print(e)
	  return jsonify({'error': str(e)}), 500
	  
if __name__=='__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)
