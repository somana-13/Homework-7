# Use an official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Install required Python packages
RUN pip install qrcode[pil]

# Set environment variables (optional)
ENV QR_CODE_DIR="qr_codes"
ENV QR_CODE_FILENAME="my_qr.png"

# Create the output directory inside the container
RUN mkdir -p $QR_CODE_DIR

# Set the default command to run the script
CMD ["python", "app.py"]
