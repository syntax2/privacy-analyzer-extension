import os
from PIL import Image, ImageDraw, ImageFont

def create_icon(size, text, filename):
    # Create a new RGBA image with transparent background
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Define colors for the icon
    circle_color = (52, 152, 219, 255)  # A pleasing blue shade
    border_color = (41, 128, 185, 255)  # A slightly darker blue for the outline
    
    # Calculate margin and border width relative to the image size
    margin = size // 10
    border_width = max(1, size // 20)
    
    # Draw the circular background
    draw.ellipse(
        [(margin, margin), (size - margin, size - margin)],
        fill=circle_color,
        outline=border_color,
        width=border_width
    )
    
    # Try to use a nice TrueType font; fallback to default if not available
    try:
        # Adjust the font path as needed for your system. Arial is common on Windows.
        font = ImageFont.truetype("arial.ttf", size // 2)
    except Exception as e:
        print("TrueType font not found. Using default font. Error:", e)
        font = ImageFont.load_default()
    
    # Calculate the position to center the text using textbbox (Pillow 10.4.0+)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_position = ((size - text_width) / 2, (size - text_height) / 2)
    
    # Draw the text (initials) on the icon
    draw.text(text_position, text, fill="white", font=font)
    
    # Save the image to the provided filename
    image.save(filename)
    print(f"Icon saved as: {filename}")

# Ensure the icons directory exists
icons_dir = os.path.join(os.getcwd(), "icons")
os.makedirs(icons_dir, exist_ok=True)

# Generate the icons
create_icon(48, "PA", os.path.join(icons_dir, "icon48.png"))
create_icon(128, "PA", os.path.join(icons_dir, "icon128.png"))
