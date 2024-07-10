from PIL import Image

def encrypt_image(image_path, encrypted_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Convert image to RGB mode (if not already in RGB mode)
    img = img.convert("RGB")

    # Create a new image for encrypted pixels
    encrypted_img = Image.new('RGB', (width, height))

    # Encrypt each pixel by XORing with the key
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # Apply XOR encryption on each RGB channel
            encrypted_pixel = tuple(p ^ key for p in pixel)
            encrypted_img.putpixel((x, y), encrypted_pixel)

    # Save the encrypted image
    encrypted_img.save(encrypted_path)
    print(f"Image encrypted successfully and saved as {encrypted_path}")

def decrypt_image(encrypted_path, decrypted_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_path)
    width, height = encrypted_img.size

    # Create a new image for decrypted pixels
    decrypted_img = Image.new('RGB', (width, height))

    # Decrypt each pixel by XORing again with the key (XOR is its own inverse)
    for y in range(height):
        for x in range(width):
            encrypted_pixel = encrypted_img.getpixel((x, y))
            # Apply XOR decryption on each RGB channel
            decrypted_pixel = tuple(p ^ key for p in encrypted_pixel)
            decrypted_img.putpixel((x, y), decrypted_pixel)

    # Save the decrypted image
    decrypted_img.save(decrypted_path)
    print(f"Image decrypted successfully and saved as {decrypted_path}")

# Example usage:
image_path = "input_image.jpg"
encrypted_path = "encrypted_image.jpg"
decrypted_path = "decrypted_image.jpg"
encryption_key = 123  # Example encryption key (can be any integer)

# Encrypt the image
encrypt_image(image_path, encrypted_path, encryption_key)

# Decrypt the encrypted image
decrypt_image(encrypted_path, decrypted_path, encryption_key)
