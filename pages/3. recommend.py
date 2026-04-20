import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

from tensorflow.keras.models import load_model, Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

# ---------------------------
# LOAD EVERYTHING (ONLY ONCE)
# ---------------------------
@st.cache_resource
def load_all():

    model = load_model("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\efficientnet_model.keras")

    feature_extractor = Model(
        inputs=model.input,
        outputs=model.layers[-2].output
    )

    features = pickle.load(open("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\features_embeddings.pkl", "rb"))
    paths = pickle.load(open("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\paths.pkl", "rb"))

    df = pd.read_csv("D:\\PROJECTS\\FASHION PRODUCT\\notebooks\\data\\image_dataset_for_modelling.csv")

    return model, feature_extractor, features, paths, df


model, feature_extractor, features, paths, df_images = load_all()


# ---------------------------
# FEATURE EXTRACTION FUNCTION
# ---------------------------
def extract_features(img):

    img = img.resize((224, 224))
    img = np.array(img)

    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    features = feature_extractor.predict(img, verbose=0)
    return features.flatten()


# ---------------------------
# RECOMMENDATION FUNCTION
# ---------------------------
def recommend(query_features, top_n=5):

    similarities = cosine_similarity([query_features], features)[0]
    indices = np.argsort(similarities)[::-1][1:top_n+1]

    results = []

    for i in indices:
        img_path = paths[i]
        filename = os.path.basename(img_path)

        metadata = df_images[df_images['filename'] == filename]

        results.append((img_path, similarities[i], metadata))

    return results


# ---------------------------
# CLASSIFICATION FUNCTION
# ---------------------------
def classify_image(img):
    
    img = img.resize((224, 224))
    img = np.array(img)

    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    preds = model.predict(img)
    class_index = np.argmax(preds)

    return class_index


# ---------------------------
# UI STARTS HERE
# ---------------------------

class_names = ["Bra", "Flats", "Handbags", "Heels", "Kurtas", 
               "Sarees", "Tops", "Tshirts", "Wallets", "Watches"]
st.title("🛍️ Fashion Image Recommendation System")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])


if uploaded_file is not None:

    # Show uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Extract features
    query_features = extract_features(img)

    # Classification
    class_index = classify_image(img)
    st.subheader(f"Predicted Class Index: {class_index}")
    st.subheader("Pedicted Class:")
    st.write(class_names[class_index])

    # Recommendations
    st.subheader("🔍 Similar Products")

    results = recommend(query_features, top_n=5)

    cols = st.columns(5)

    for i, (img_path, sim, metadata) in enumerate(results):

        with cols[i]:
            st.image(img_path)
            st.caption(f"Similarity: {sim:.2f}")

            if not metadata.empty:
                st.write(metadata.iloc[0])