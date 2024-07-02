import numpy as np
from PIL import Image
import tensorflow as tf
import gradio as gr


model = tf.keras.models.load_model('best_model.keras')

# Function to preprocess image for inference
def preprocess_image(image):
    image = tf.image.resize(image, (160, 160))  # Resize to match model input shape
    image = tf.expand_dims(image, 0)  # Add batch dimension
    return image
# Function to load and preprocess an image from the given path
def load_and_predict_image(image_path):
    image = Image.open(image_path)  # Ensure image is in RGB format
    preprocessed_image = preprocess_image(image)
    predictions = model(preprocessed_image)
    prediction = np.where(predictions < 0.5, 0, 1).item()
    predict = "Perfect" if prediction == 1 else "Defected"
    return predict

demo = gr.Interface(fn=load_and_predict_image,
                    inputs=[gr.Image(label="Upload image", type="filepath")],
                    #outputs=[gr.Textbox(label="Caption")],
                    outputs =[gr.Textbox(label="Your Tyre/Tire Condition ")],
                    title="Tyres/Tires Health Checkup Demo",
                    description="Upload your tire image to check its Health or use any example below",
                    allow_flagging="never",
                    examples=["Defective-1.jpg", "Defective-2.jpg","Defective-3.jpg","perfect1.jpg","perfect2.jpg","perfect3.jpg"])

if __name__ == "__main__":
    demo.launch()