import qrcode

def generate_blue_on_white_qr_code(data, filename="blue_on_white_qr.png"):
    """
    Generates a QR code with blue modules and a white background.

    Args:
        data (str): The data (e.g., a link) to encode in the QR code.
        filename (str): The name of the output image file.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data) # The 'data' variable *must* be a string here
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="white")
    img.save(filename)

# --- HOW TO USE IT CORRECTLY WITH A LINK ---

# Define your link as a string
my_link = "https://shrimpomenu.github.io/" # <--- This is your data (the link)

# Call the function, passing the string variable
generate_blue_on_white_qr_code(my_link, "shrimpoqr.png")


print("QR codes generated!")