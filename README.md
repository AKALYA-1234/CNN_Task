🦋 CNN Butterfly Classification

This project uses a Convolutional Neural Network (CNN) to classify butterfly species from images.
The model is built with TensorFlow/Keras and trained on a butterfly dataset.


App link:

https://huggingface.co/spaces/AKALYAS/CNN_Task



📂 Project Structure

📜 app.py → Flask app to serve model predictions

📜 trained_model.py → Script to train the CNN model

🧠 butterfly_model.h5 → Trained CNN model weights

🗂 class_indices.json → Mapping of class labels

📓 code.ipynb → Jupyter notebook with experiments

📁 DATASET/ → Training dataset (images)

📄 requirements.txt → Python dependencies

Label Distribution:


<img width="1160" height="747" alt="image" src="https://github.com/user-attachments/assets/c4664638-1f63-4866-b286-a536397b53a9" />



⚙️ Installation

1)Clone the repository:

git clone https://github.com/AKALYA-1234/CNN_Task.git
cd CNN_Task


2)Install dependencies:

pip install -r requirements.txt



🚀 Training

Run the training script to train the CNN model:

python trained_model.py


🖥️ Deployment

Run the Flask app to serve predictions:

python app.py

You can then send an image to the API and get predictions for butterfly species.



📊 Results

✅ Final Training Accuracy: ~73%

✅ Final Validation Accuracy: ~58%

📉 Loss values available in training logs



Demo App:


<img width="1857" height="662" alt="image" src="https://github.com/user-attachments/assets/cddb82dd-924c-4297-ba7a-1501d6f0342e" />






