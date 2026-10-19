from PIL import Image

def create_image():
    image = Image.new("RGB", (200, 100), "white")
    image.save("example.png")
    print("Зображення створено: example.png")
