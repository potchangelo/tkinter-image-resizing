from PIL import Image, ImageTk

def image_open(filename):
    image_original = Image.open(filename)
    width_original, height_original = image_original.size

    width, height = 500, 500
    if height_original > width_original:
        width = int(height * width_original / height_original)
    else:
        height = int(width * height_original / width_original)
    image_resized = image_original.resize((width, height))

    image_tk = ImageTk.PhotoImage(image_resized)

    return image_original, image_tk