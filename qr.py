import os
import qrcode

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

barcode_data = input("Değer Giriniz: ")
print("Oluşturuluyor...")
img = generate_qr_code(barcode_data)

directory = os.path.join(os.path.expanduser("~"), "Desktop", "QR")
if not os.path.exists(directory):
    os.makedirs(directory)
img.save("{}/{}.png".format(directory, barcode_data.replace("/", "_")))
print("Oluşturuldu. ({})".format(barcode_data))
