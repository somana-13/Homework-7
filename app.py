import qrcode
import os

# Get the URL from an environment variable (default is your GitHub homepage)
url = os.getenv('QR_DATA_URL', 'https://github.com/kaw393939')

# Set QR code colors
fill_color = os.getenv('FILL_COLOR', 'black')
back_color = os.getenv('BACK_COLOR', 'white')

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

# Create QR Code image
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Save the QR code to a file
output_dir = os.getenv('QR_CODE_DIR', 'qr_codes')
output_file = os.getenv('QR_CODE_FILENAME', 'my_qr.png')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Save image
img.save(f"{output_dir}/{output_file}")

print(f"QR code generated and saved as {output_dir}/{output_file}")
