import os
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_PATH = "./assets/banners/template.png"
FONT_PATH = "./assets/fonts"

def generate_banner(device_vendor: str, device_name: str, device_codename: str):
    template = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(template)
    
    font_vendor = ImageFont.truetype(f"{FONT_PATH}/GENERALSANS-MEDIUM.OTF", size=60)
    font_device = ImageFont.truetype(f"{FONT_PATH}/GENERALSANS-MEDIUM.OTF", size=140 if len(device_name) <= 12 else 100)
    font_codename = ImageFont.truetype(f"{FONT_PATH}/CONFIG-MEDIUM.OTF", size=40)
    
    draw.text((85, 590), device_vendor, font=font_vendor, fill=(255, 69, 0))
    draw.text((80, 680), device_name, font=font_device, fill=(238, 238, 238))
    draw.text((80, 1320), device_codename.upper(), font=font_codename, fill=(51, 51, 51))
    
    
    output_filename = f"./assets/{device_codename}_banner.png"
    template.save(output_filename)
    return os.path.abspath(output_filename)
