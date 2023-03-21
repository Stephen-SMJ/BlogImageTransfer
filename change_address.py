import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', type=str, help='the path of your blog fold')
parser.add_argument('--server_address', type=str, help='the address of your server')
arg = parser.parse_args()

# 输入文件夹路径和输出路径
folder_path = arg.folder_path
server_url = arg.server_address   #指定图片的服务器URL

# 定义正则表达式匹配图片URL
pattern = re.compile(r"\!\[(.*?)\]\((.*?)\)")


# 使用正则表达式替换图片URL
def replace_url(match):
    title = match.group(1) #![图片的title]
    image_path = match.group(2) #(图片的url)
    image_name = os.path.basename(image_path)
    new_url = f"{server_url}{image_name}"
    return f"![{title}]({new_url})"

# 遍历指定文件夹下的所有md文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".md"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r+", encoding="utf-8") as file:
            content = file.read()
            try:
                new_content = re.sub(pattern, replace_url, content) #第二个参数可以是一个函数，这个函数的第一个参数就是当前匹配到的子字符串的对象（即MatchObject）
                file.seek(0) #使用seek可以一次读写，不用再打开一遍文件写入, seek(0)指针回到开头
                file.truncate() #清空文件内容
                file.write(new_content)
                print("fished transfer url in {}".format(file_name))
                file.close()
            except:
                print("{} occurs a error".format(file_name))


# !: 匹配以感叹号开头的字符串，即图片链接的标记符号。
# \[和\]: 匹配中括号中的任意字符，即图片的标题。这里使用\[和\]进行转义。
# .*?: 匹配中间的任意字符，即图片的描述信息。这里使用.*?表示非贪婪模式，避免匹配到多个图片链接。
# \(和\): 匹配括号中的任意字符，即图片的链接地址。这里同样使用\(和\)进行转义
# ()将链接地址提取出来作为一个group。 group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分