
import qrcode

def convert_to_qr_code(text, output_file):
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_code.add_data(text)
    qr_code.make(fit=True)

    qr_img = qr_code.make_image(fill_color="black", back_color="white")
    qr_img.save(output_file)


print (__name__)
if __name__=="__main__":
    text = "Hello, Liam!"
    output_file = "qr_code.png"
    convert_to_qr_code(text, output_file)
    print(f"A QR code has been saved to {output_file}.")

