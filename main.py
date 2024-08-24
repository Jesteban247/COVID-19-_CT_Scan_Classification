import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np

app = Flask(__name__)

# Configuration
MODEL_PATH = 'Model/covid19_ct_model.keras'
IMAGES_FOLDER = 'images'
CLASS_NAMES = ['1NonCOVID', '2COVID', '3CAP']

# Class descriptions
CLASS_DESCRIPTIONS = {
    '1NonCOVID': 'No evidence of COVID-19 or CAP.',
    '2COVID': 'Evidence of COVID-19 infection.',
    '3CAP': 'Evidence of Community-Acquired Pneumonia (CAP).'
}

# Load the trained model
model = load_model(MODEL_PATH)

def predict_label(img_path):
    """Predict the label and probabilities of the given image."""
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    prediction = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    probabilities = {CLASS_NAMES[i]: (float(prediction[0][i]), CLASS_DESCRIPTIONS[CLASS_NAMES[i]]) for i in range(len(CLASS_NAMES))}
    return predicted_class, probabilities

def get_image_folders():
    """Get a list of image folders and their contents."""
    folders = {}
    for folder in os.listdir(IMAGES_FOLDER):
        folder_path = os.path.join(IMAGES_FOLDER, folder)
        if os.path.isdir(folder_path):
            folders[folder] = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return folders

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        folder = request.form.get('folder')
        selected_image = request.form.get('selected_image')
        if folder and selected_image:
            img_path = os.path.join(IMAGES_FOLDER, folder, selected_image)
            predicted_class, probabilities = predict_label(img_path)
            return render_template('index.html', prediction=predicted_class, img_path=img_path, probabilities=probabilities, show_results=True, image_folders=get_image_folders(), selected_folder=folder)
    return render_template('index.html', prediction=None, show_results=False, image_folders=get_image_folders(), selected_folder=None)

@app.route('/images/<folder>/<filename>')
def image_file(folder, filename):
    return send_from_directory(os.path.join(IMAGES_FOLDER, folder), filename)

if __name__ == "__main__":
    app.run(debug=True)
