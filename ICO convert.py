from PIL import Image

def jpg_to_ico(input_path, output_path):
    # Open the JPG image
    image = Image.open(input_path)
    
    # Convert the image to RGBA (if not already in RGBA mode)
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    # Resize the image to 256x256 (required size for ICO format)
    image = image.resize((256, 256), Image.LANCZOS)
    
    # Save the image as ICO format
    image.save(output_path, format='ICO', quality=5)  # You can adjust the quality here if needed

# Usage
input_image_path = "C:\\Users\\hp\\Desktop\\...\\just.jpg" #path to the input JPG image
output_ico_path = "C:\\Users\\hp\\Desktop\\...\\output.ico" #Path to save the output ICO file
jpg_to_ico(input_image_path, output_ico_path)