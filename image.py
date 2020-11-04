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

def image_save(image, directory, width_list):
    image_name_ext = image.filename.split('/')[-1]
    image_name, image_format = image_name_ext.split('.')

    for width_str in width_list:
        if len(width_str) == 0:
            continue

        width = int(width_str)
        height = int(width * image.size[1] / image.size[0])
        image_output = image.resize((width, height))
        image_output.save('{}/{}-{}.{}'.format(directory, image_name, width_str, image_format))