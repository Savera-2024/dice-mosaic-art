import streamlit as st
from PIL import Image
import numpy as np
import io
# Page setting
st.set_page_config(page_title="🎲 Dice Mosaic Generator", layout="wide")


st.title("🎲Dice Mosaic Generator \n")

# Sidebar settings
st.sidebar.title("⚙ Settings")

dice_size_value = st.sidebar.slider("🎲 Dice Size (px)",min_value=5, max_value=30, value=15)
dice_size = (dice_size_value, dice_size_value)

# Mosaic color mode
color_mode = st.sidebar.radio("🎨 Mosaic Style", ["Color", "Black & White"])
# st.write(f"Selected Mosaic Style: {color_mode}")

# Upload image
uploaded_file = st.file_uploader("📤 Upload your image (JPG or PNG) \n", type=["jpg", "jpeg", "png"])


# Load dice images
@st.cache_data
def load_dice_images(size):
    dice_imgs = {}
    for i in range(1, 7):
        try:
            dice_img = Image.open(f"dice {i}.png").convert("RGBA").resize(size, Image.Resampling.LANCZOS) #resampling image
            dice_imgs[i] = dice_img
        except Exception as e:
            st.error(f"Couldn't load 'dice {i}.png': {e}")
    return dice_imgs

# Map brightness to dice face
def intensity_to_dice_face(intensity):
         face = int(( 1-intensity / 255) * 6) + 1
         return min(face, 6)

# #Generate dice mosaic
def create_dice_mosaic(image, dice_size, dice_images, color_mode):
    image = image.convert("RGB") #convert image in RGB format
    width, height = image.size   # if width=100 and height=70 then image.size = (100,70)

    # Pad image
    remainder_w = width % dice_size[0]
    remainder_h = height % dice_size[1]

    pad_w = dice_size[0] - remainder_w if remainder_w else 0 #calculate extra width
    pad_h = dice_size[1] - remainder_h if remainder_h else 0

    new_w = width + pad_w
    new_h = height + pad_h

    padded_img = Image.new("RGB", (new_w, new_h))#create new padded image
    padded_img.paste(image, (0, 0))#paste original image on new created padded image


    img_array = np.array(padded_img)     ##converts image into numpy array
    mosaic_img = Image.new('RGB', (new_w, new_h)) #it creates a blank image of black colour default(0,0,0)


    weights = [0.299, 0.587, 0.114]# weights for RGB to greyscale Conversion
    for y in range(0, new_h, dice_size[1]):  # move top to bottom with size of each block of dice size[1]
        for x in range(0, new_w, dice_size[0]): #move left to write with size of each block of dice size[0]
            block = img_array[y:y + dice_size[1], x:x + dice_size[0]] #slicing of image
            avg_color = np.mean(block, axis=(0, 1)) # mean of RGB and representing in a column
            brightness = np.dot(avg_color, weights)
            face = intensity_to_dice_face(brightness)#get dice face acc to intensity

            dice_img = dice_images.get(face)
            if dice_img:
                if color_mode == "Color":
                    tinted = Image.new('RGB', dice_size, tuple(map(int,avg_color))) #create tinted dice face
                    mask = dice_img.convert('L')
                    tinted.paste(dice_img, (0, 0), mask)
                    mosaic_img.paste(tinted, (x, y))
                else:
                   mosaic_img.paste(dice_img.convert("RGB"), (x, y))

    return mosaic_img

# Main app logic
if uploaded_file is not None:
    try:
        original_img = Image.open(uploaded_file)
        col1, col2 = st.columns([1, 1])

        with col1:
         st.subheader("📷 Original Image")
         st.image(original_img,use_container_width=True)

        dice_images = load_dice_images(dice_size)
        mosaic = create_dice_mosaic(original_img, dice_size, dice_images, color_mode)

        with col2:
         st.subheader("🎨 Dice Mosaic")
         st.image(mosaic, caption="Generated Mosaic", use_container_width=True)

        # Mosaic Summary
        st.write("## 🧾Mosaic Summary ")
        st.write(f"- Selected Mosaic Style: {color_mode}")
        st.write(f"- Dice Size: {dice_size_value}px x {dice_size_value}px")
        st.write(f"- Mosaic Dimensions: {mosaic.width} x {mosaic.height} px")
        st.write(f"- Total Dice: {(mosaic.width // dice_size_value) * (mosaic.height // dice_size_value)}")

        # Download button
        buf = io.BytesIO()
        mosaic.save(buf, format="PNG")
        byte_img = buf.getvalue()

        st.download_button(" **⬇ Download Your Mosaic** ",data=byte_img,file_name="dice_mosaic.png",mime="image/png")

    except Exception as e:
        st.error(f"❌ Error processing the image: {e}")
else:
    st.info("Upload an image from the uploader above to begin.")



