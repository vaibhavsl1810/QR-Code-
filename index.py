import qrcode 
# Data to encode
data = input("Our Text :- ")

# Create a QR Code object
qr = qrcode.QRCode(
    version=5,  # Version of the QR Code, controls the size (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size (minimum is 4 for QR codes)
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create and save the QR Code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
filename = "user_qrcode.png"
img.save(filename)

print(f"QR Code saved as {filename}")
