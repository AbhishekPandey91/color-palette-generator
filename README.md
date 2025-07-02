# color-palette-generator
A Streamlit app that extracts dominant colors from an uploaded image using KMeans clustering and displays them as a color palette.

# 🎨 Color Palette Generator from Image

This is a simple Streamlit web app that lets you upload an image and automatically extracts a color palette using KMeans clustering.

---

## 🚀 Demo

Upload an image and get its dominant colors visualized in a beautiful palette!

## 🧠 How It Works

1. You upload an image (JPEG/PNG).
2. The app resizes and flattens it for faster processing.
3. KMeans clustering is applied to group similar colors.
4. The cluster centers are shown as the final color palette.

---

## 📦 Features

- Upload any image (`.jpg`, `.jpeg`, `.png`)
- Choose number of dominant colors
- Visualize color palette directly
- Built using Python, Streamlit, scikit-learn, and matplotlib

---

## 🛠️ Installation

### 1. Clone the repository

git clone https://github.com/your-username/color-palette-generator.git
cd color-palette-generator

### 2. Install dependencies
It’s recommended to use a virtual environment:

pip install -r requirements.txt

### 3. Run the app

streamlit run app.py

## 📄 `requirements.txt` (Add this too)

```txt
streamlit
scikit-learn
matplotlib
Pillow

