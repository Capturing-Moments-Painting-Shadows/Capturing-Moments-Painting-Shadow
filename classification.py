import json
from pathlib import Path
import time
from matplotlib import pyplot as plt
from matplotlib.collections import PatchCollection
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import torch
from transformers import Owlv2Processor, Owlv2ForObjectDetection
from matplotlib.patches import Polygon
import deepl
import re

letter_pattern = re.compile(r'[a-zA-Z]')
def contains_letters(text, pattern=letter_pattern):
    return bool(pattern.search(text))

def translate_object_list(object_list):

    auth_key = "5fbbf5d5-edba-464f-bbbf-4a95dbd3b610:fx" # 更新api
    translator = deepl.Translator(auth_key)
    translation_mapping = {}

    if len(object_list) == 1: # 整句翻译
        translate_input = object_list
        translate_result = translator.translate_text(translate_input, source_lang="ZH", target_lang="EN-US")[0]
        translate_result_text = translate_result.text # string 类型
        if "lit. " in translate_result_text:
            translate_result_text = translate_result_text.split("lit. ")[1]
        if "fig. " in translate_result_text:
            translate_result_text = translate_result_text.split("fig. ")[0]
        translation_mapping[object_list[0]] = translate_result_text
        return translation_mapping
    elif len(object_list) > 1: # 关键要素列表翻译
        punctuation = ",.，。[]"
        # 诗句抽取的关键要素列表list转成string（整体翻译再分词效果更好）
        object_list_no_punc = [] # 去除列表中的标点符号
        for obj in object_list:
            if obj not in punctuation or obj != '':
                object_list_no_punc.append(obj)
        object_list_to_string = str(object_list_no_punc)

        translate_input = [object_list_to_string]
        translate_result = translator.translate_text(translate_input,source_lang="ZH", target_lang="EN-US")[0]
        translate_result_text = translate_result.text
        # 整体翻译后再分词成list
        res_list = re.split(",|'|[|]|\"",translate_result_text)
        res = []
        for obj in res_list:
            if contains_letters(obj):
                res.append(obj)
        # 创建原始类别到翻译类别的映射
        for i in range(len(object_list_no_punc)):
            translation_mapping[object_list_no_punc[i]] = res[i] if i < len(res) else object_list_no_punc[i]
        return translation_mapping
    else:
        return {}

def process_image_detection(image_path, translation_mapping, font_path="c:\\WINDOWS\\Fonts\\MSYHL.TTC", font_size=15, desired_size=(256, 256), threshold=0.15):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # 打开图像
    image = Image.open(image_path)
    
    # 如果图像不是RGB格式，转换为RGB格式
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # 将图像转换为NumPy数组
    image_np = np.array(image)
    
    # 检查图像的形状
    print(f"图像形状: {image_np.shape}")
    font = ImageFont.truetype(font_path, font_size)
    processor = Owlv2Processor.from_pretrained("google/owlv2-base-patch16-ensemble")
    model = Owlv2ForObjectDetection.from_pretrained("google/owlv2-base-patch16-ensemble").to(device)
    original_size = image.size  # Original image size (width, height)
    resized_image = image.resize(desired_size)

    translated_categories = list(translation_mapping.values())
    inputs = processor(text=[translated_categories], images=resized_image, return_tensors="pt").to(device)
    
    # 清理显存
    torch.cuda.empty_cache()
    
    # 设置分配策略
    import os
    os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'
    
    # 使用混合精度减少内存占用
    with torch.cuda.amp.autocast():
        outputs = model(**inputs)
        
    target_sizes = torch.Tensor([desired_size[::-1]]).to(device)
    results = processor.post_process_object_detection(outputs=outputs, target_sizes=target_sizes, threshold=threshold)
    
    best_match = None
    highest_score = 0
    for box, score, label in zip(results[0]["boxes"], results[0]["scores"], results[0]["labels"]):
        if score.item() > highest_score:
            highest_score = score.item()
            best_match = (box, score, label)
    
    if best_match:
        box, score, label = best_match
        original_box = [
            (box[0] * original_size[0] / desired_size[0]).item(),
            (box[1] * original_size[1] / desired_size[1]).item(),
            (box[2] * original_size[0] / desired_size[0]).item(),
            (box[3] * original_size[1] / desired_size[1]).item()
        ]
        best_category = list(translation_mapping.keys())[label]
        print(f"Best match: {best_category} with confidence {round(score.item(), 3)} at location {original_box}")
        return best_category, original_box, round(score.item(), 3)
    else:
        print(f"No match found for categories: {list(translation_mapping.keys())}")
        return None, None, None

if __name__ == "__main__":
    time1=time.time()
    image_path = "D:\\腊八同学\\1大三（下）\\3软件工程\\实验\\lab2\\凝时绘影\\图片素材\\风景照\\湖光晚霞.jpg"
    categories = ["风景照", "城市", "宠物", "美女", "美食", "人像"]
    translation_mapping = translate_object_list(categories)
    best_match = process_image_detection(image_path, translation_mapping)
    if best_match:
        category, box, score = best_match
        print(f"Best match: {category}, Box: {box}, Score: {score}")
    time2=time.time()
    print('Time cost:',time2-time1)
