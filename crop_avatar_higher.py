from PIL import Image

raw_img_path = r"C:\Users\tanuj\.gemini\antigravity\brain\1174cb66-dd6c-48a8-9e9e-f51e4afa476a\.user_uploaded\media_1787812749595.jpg"
out_img_path = r"C:\Users\tanuj\OneDrive\Desktop\portfolio\avatar.jpg"

img = Image.open(raw_img_path)
width, height = img.size

# To shift the image UP inside the frame, we start the crop slightly higher up (near 0% height)
crop_top = int(height * 0.01) # Start near very top
crop_bottom = int(height * 0.58) # Take 58% of height
crop_height = crop_bottom - crop_top

crop_left = max(0, int((width - crop_height) / 2))
crop_right = min(width, crop_left + crop_height)

cropped_img = img.crop((crop_left, crop_top, crop_right, crop_bottom))
final_img = cropped_img.resize((600, 600), Image.Resampling.LANCZOS)
final_img.save(out_img_path, quality=95)

print("Image shifted up and cropped successfully!")
