from PIL import Image, ImageOps

img_path = r"C:\Users\tanuj\OneDrive\Desktop\portfolio\avatar.jpg"
img = Image.open(img_path)
width, height = img.size

# We want a 1:1 square crop focusing on the head, tie, and shoulders
# Crop top from ~5% height to ~65% height
crop_top = int(height * 0.05)
crop_bottom = int(height * 0.65)
crop_height = crop_bottom - crop_top

# Center horizontally
crop_left = max(0, int((width - crop_height) / 2))
crop_right = min(width, crop_left + crop_height)

# Crop square
cropped_img = img.crop((crop_left, crop_top, crop_right, crop_bottom))

# Resize to crisp 600x600 square
final_img = cropped_img.resize((600, 600), Image.Resampling.LANCZOS)
final_img.save(img_path, quality=95)

print("Avatar cropped and square framed successfully!")
