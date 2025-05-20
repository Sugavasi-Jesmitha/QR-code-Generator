import qrcode

def generate_qr_code(data, filename):
    """Generates a QR code for the given data and saves it to a file.

    Args:
        data (str): The information to encode in the QR code.
        filename (str): The file name for the generated QR code image.
    """
    # Create a QR Code instance with default settings
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is 21x21, 2 is 25x25, etc.)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Width of the border (minimum is 4)
    )

    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image of the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the specified file
    img.save(filename)
    print(f"QR code saved to {filename}")

# Example usage
data = "https://www.example.com"
filename = "example_qr.png"
generate_qr_code(data, filename)