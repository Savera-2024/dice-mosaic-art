# 🎲 Dice Mosaic Art

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-PIL-green?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

A Python project that transforms any image into a stunning dice-based mosaic! Built with **Python**, **Pillow**, **NumPy**, and **Streamlit**.

---

## ✨ Features

- 🎲 **Convert Any Image:** Turn standard photos into unique dice mosaic art.
- 📐 **Adjustable Dice Size:** Fine-tune the grid resolution from **5 to 30 pixels**.
- 🎨 **Dual Rendering Modes:** Choose between **Grayscale** or **Colorful** modes.
- ⚡ **Live Preview:** Interactive Streamlit web interface for real-time visualization.
- 💡 **User-Friendly:** Simple and intuitive UI for fast image transformation.

---

## 🖼️ How It Works

The app analyzes the brightness or color intensity of each pixel segment in the uploaded image and maps it to a corresponding dice face image (**1 to 6**). This creates an artistic visual made entirely out of dice!

> 🎯 **Mapping Logic:**
> - **Darker Area** ➔ Dice face 6
> - **Lighter Area** ➔ Dice face 1

---

## 📸 Snapshots

| App Interface | Grayscale Dice Mosaic | Colorful Dice Mosaic |
| :---: | :---: | :---: |
| *[Insert App Interface Image]* | *[Insert Grayscale Image]* | *[Insert Colorful Image]* |

---

## 🧑‍💻 How to Run Locally in PyCharm

### 🔧 Setup Instructions

1. Open the project in **PyCharm**.
2. Make sure the following files are in the same folder:
   - `Dice Mosaic Art.py`
   - Dice face images (`dice1.png`, `dice2.png`, ..., `dice6.png`)
3. Open the **Terminal** in PyCharm and install the required libraries:
   ```bash
   pip install streamlit pillow numpy

   Run the app:

Bash
streamlit run "Dice Mosaic Art.py"
The app will automatically open in your browser at: http://localhost:8501

👨‍💻 Developed By
Zumar Sayyam

Haleema Sadia

Ayesha Javed

Savera Zainab

"Blending code and creativity — one dice at a time." 🎲✨
