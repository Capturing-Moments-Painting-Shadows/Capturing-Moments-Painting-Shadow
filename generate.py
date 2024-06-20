import time
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO
import os

def generate_image(prompt, api_key, image_name='generated_image.png', output_dir='output'):
    client = OpenAI(api_key=api_key)
    response = client.images.generate(
        model="dall-e-3",
        prompt="按照要求画一幅水墨风格的画，要求是：" + prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, image_name)
    image.save(file_path)
    image.show()
    print(f"DALLE prompt Image saved to {file_path}")
    return file_path

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
    
    # If the image is larger than max_size_mb, reduce quality
    quality = 95
    while buffer.tell() >= max_size_mb * 1024 * 1024 and quality > 10:
        buffer = BytesIO()
        image.save(buffer, format='PNG', quality=quality)
        quality -= 5
    
    output_path = image_path.replace(".jpg", "_processed.png")
    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())
    
    return output_path

from PIL import ImageDraw
def create_partial_mask(image_size):
    # Create a partially transparent mask with the same size as the input image
    mask = Image.new("RGBA", image_size, (255, 255, 255, 255))  # Start with white (opaque)
    draw = ImageDraw.Draw(mask)
    draw.rectangle([(0, 0), image_size], fill=(0, 0, 0, 0))  # Make the whole image transparent
    # Modify specific parts of the image to be edited
    draw.rectangle([(150, 150), (200, 200)], fill=(255, 255, 255, 255))  # Example: edit a specific part
    mask_path = "partial_mask.png"
    mask.save(mask_path)
    return mask_path

def images_edit(prompt, image_path, api_key, image_name='generated_image.png', output_dir='output'):
    # Preprocess the image to ensure it meets the criteria
    processed_image_path = preprocess_image(image_path)
    
    # Create a full white mask
    image = Image.open(processed_image_path)
    mask_path = create_partial_mask(image.size)
    
    client = OpenAI(api_key=api_key)

    response = client.images.edit(
        model="dall-e-2",
        image=open(processed_image_path, "rb"),
        mask=open(mask_path, "rb"),
        prompt="在原有图像的基础上修改图像，要求是：" + prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response.data[0].url
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, image_name)
    image.save(file_path)
    image.show()
    print(f"DALLE prompt Image saved to {file_path}")
    return file_path

def create_variation(prompt, image_path, api_key, image_name='generated_image.png', output_dir='output'):
    # Preprocess the image to ensure it meets the criteria
    processed_image_path = preprocess_image(image_path)
    
    client = OpenAI(api_key=api_key)
    response = client.images.create_variation(
        model="dall-e-2",
        image=open(processed_image_path, "rb"),
        n=1,
        size="1024x1024"
    )

    image_url = response.data[0].url
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, image_name)
    image.save(file_path)
    image.show()
    print(f"DALLE prompt Image saved to {file_path}")
    return file_path




if __name__ == '__main__':
    api_key = 'sk-proj-933kUO1jCoiWF6Ecll6hT3BlbkFJPHWOp1d80wtf3G14iJ1V'
    prompt = '漫画风格'
    image_path = "D:\\腊八同学\\1大三（下）\\3软件工程\\实验\\lab2\\凝时绘影\\图片素材\\宠物\\小兔.jpg"
    time1=time.time()
    # generate_image(prompt, api_key)
    create_variation(prompt, image_path, api_key)
    # images_edit(prompt, image_path, api_key)
    time2=time.time()
    print('Time cost:',time2-time1)
