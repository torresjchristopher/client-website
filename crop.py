from PIL import Image

# Load Landingpage.png
img = Image.open('Landingpage.png')
print(f'Original: {img.size}')

# Target dimensions (from Landingpage3.png)
target_width = 891
target_height = 1117

# Calculate crop to center
width, height = img.size
left = (width - target_width) // 2
top = (height - target_height) // 2
right = left + target_width
bottom = top + target_height

# Crop and save
cropped = img.crop((left, top, right, bottom))
cropped.save('Landingpage.png')
print(f'Cropped to: {cropped.size}')
