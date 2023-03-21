import os
import re
import urllib.request
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', type=str, help='the path of your blog fold')
parser.add_argument('--output_path', type=str, help='the output path of your download images')
arg = parser.parse_args()

folder_path = arg.folder_path
output_path = arg.output_path

# 遍历文件夹下的所有md文件
for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
            content = file.read()
            # 使用正则表达式提取图片链接
            img_urls = re.findall("!\[.*?\]\((.*?)\)", content)
            # 下载图片
            for url in img_urls:
                try:
                    img_name = os.path.basename(url)
                    img_path = os.path.join(output_path, img_name)
                    urllib.request.urlretrieve(url, img_path)
                    print(f"Downloaded {img_name} from {url}")
                except:
                    print(f"Error: Downloaded {url} failed !!!")




