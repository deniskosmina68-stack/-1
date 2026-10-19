import qrcode

def create_qr():
    text = input("\nВведіть текст для QR-коду: ")
    image = qrcode.make(text)
    image.save("qr.png")
    print("QR-код збережено у файлі qr.png")
