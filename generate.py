import time
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO
import os
from PIL import ImageDraw

def preprocess_image(image_path, max_size_mb=4):
    image = Image.open(image_path)
    
    # Convert to PNG if not already
    if image.format != 'PNG':
        image = image.convert('RGBA')
    
    # Resize to square
    width, height = image.size
    min_side = min(width, height)
    image = image.crop((0, 0, min_side, min_side))
    
    # Save to BytesIO to control file size
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    
    # If the image is larger than max_size_mb, reduce size
    size_mb = buffer.tell() / (1024 * 1024)
    if size_mb > max_size_mb:
        scale_factor = (max_size_mb / size_mb) ** 0.5
        new_size = (int(min_side * scale_factor), int(min_side * scale_factor))
        image = image.resize(new_size, Image.LANCZOS)
        buffer = BytesIO()
        image.save(buffer, format='PNG')
    
    # Ensure the image size is less than max_size_mb
    while buffer.tell() >= max_size_mb * 1024 * 1024:
        scale_factor = 0.9
        new_size = (int(image.width * scale_factor), int(image.height * scale_factor))
        image = image.resize(new_size, Image.LANCZOS)
        buffer = BytesIO()
        image.save(buffer, format='PNG')

    output_path = image_path.replace(".jpg", "_processed.png").replace(".jpeg", "_processed.png")
    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())
    
    return output_path

def create_variation( image_path, api_key = 'sk-proj-IhptTzpXcuBiqAFe0rFYT3BlbkFJvaonIxrkQjLCaKBG4u24', output_dir = ''):
    # Preprocess the image to ensure it meets the criteria
    processed_image_path = preprocess_image(image_path)
    
    time1=time.time()
    print('start time:',time1)
    client = OpenAI(api_key=api_key)
    response = client.images.create_variation(
        model="dall-e-2",
        image=open(processed_image_path, "rb"),
        n=1,
        size="1024x1024"
    )

    time2=time.time()
    print('end time:',time2)
    print('Time cost:',time2-time1)

    image_url = response.data[0].url
    # return image_url
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))

    # os.makedirs(output_dir, exist_ok=True)
    image.save(output_dir)
    print(f"DALLE prompt Image saved to {output_dir}")
    return output_dir




if __name__ == '__main__':
    api_key = 'sk-proj-IhptTzpXcuBiqAFe0rFYT3BlbkFJvaonIxrkQjLCaKBG4u24'
    prompt = '漫画风格'
    image_path = "D:\\腊八同学\\1大三（下）\\3软件工程\\实验\\lab2\\凝时绘影\\图片素材\\美食\\川菜.jpg"
    time1=time.time()
    # generate_image(prompt, api_key)
    create_variation(image_path, api_key)
    # images_edit(prompt, image_path, api_key)
    time2=time.time()
    print('Time cost:',time2-time1)
