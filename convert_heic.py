from PIL import Image
import os

food_dir = "Food/Food"
if os.path.exists(food_dir):
    for filename in os.listdir(food_dir):
        if filename.lower().endswith('.heic'):
            heic_path = os.path.join(food_dir, filename)
            jpg_filename = filename.rsplit('.', 1)[0] + '.jpg'
            jpg_path = os.path.join(food_dir, jpg_filename)
            
            try:
                img = Image.open(heic_path)
                img = img.convert('RGB')
                img.save(jpg_path, 'JPEG', quality=90)
                print(f"Converted {filename} to {jpg_filename}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")
