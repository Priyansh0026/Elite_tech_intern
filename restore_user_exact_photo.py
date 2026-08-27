from PIL import Image

raw_img_path = r"C:\Users\tanuj\.gemini\antigravity\brain\1174cb66-dd6c-48a8-9e9e-f51e4afa476a\.user_uploaded\media_1787812749595.jpg"
out_img_path = r"C:\Users\tanuj\OneDrive\Desktop\portfolio\avatar.jpg"

img = Image.open(raw_img_path)
width, height = img.size

# Frame: Top near top of head (3%), Bottom around mid-chest (62%)
crop_top = int(height * 0.03)
crop_bottom = int(height * 0.62)
crop_height = crop_bottom - crop_top

crop_left = max(0, int((width - crop_height) / 2))
crop_right = min(width, crop_left + crop_height)

cropped_img = img.crop((crop_left, crop_top, crop_right, crop_bottom))
final_img = cropped_img.resize((800, 800), Image.Resampling.LANCZOS)
final_img.save(out_img_path, quality=98)

print("Restored exact photo framing!")
