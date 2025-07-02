import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Function to create and show color palette
def create_color_palette(colors):
    n = len(colors)
    fig, ax = plt.subplots(1, figsize=(n, 1))
    for idx, color in enumerate(colors):
        ax.add_patch(plt.Rectangle((idx, 0), 1, 1, color=np.array(color)/255))
    ax.set_xlim(0, n)
    ax.set_ylim(0, 1)
    ax.axis('off')
    st.pyplot(fig)

# Streamlit UI
st.title("Color Palette Generator from Image")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image",  use_container_width=True)

    # Resize image for faster processing
    image = image.resize((150, 150))
    image_np = np.array(image)
    image_flat = image_np.reshape((-1, 3))  # Reshape for clustering

    # KMeans clustering
    k = st.slider("Select number of colors", min_value=2, max_value=10, value=5)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(image_flat)

    # Show color palette
    st.subheader("Extracted Color Palette")
    create_color_palette(kmeans.cluster_centers_.astype(int))
