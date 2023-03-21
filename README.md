# 批量博客防盗链接图片站点转移脚本
最近CSDN开始对图片施加防盗链接了。<br>
我个人经常在CSDN上进行写作，前一段时间我选择自己建站，为了省事，我直接使用了CSDN上的图片地址，当你在CSDN上写作时你上传的图片会存储在CSDN的服务器中，
可以直接在网页上输入URL访问。但是最近CSDN对图片施加了防盗链接，我个人网站上的所有图片全都看不到了。
搜索了一些解决方案，大多都治标不治本。于是我选择将图片上传至自己的服务器，通过Nginx进行代理。这个脚本适合与和我情况类似的朋友们使用: <br>
1.个站图片被防盗链接限制 2.有云服务器
## 脚本使用方法
1. 克隆仓库并进入项目目录
   ```
    git clone https://github.com/Stephen-SMJ/BlogImageTransfer.git
    cd blog_img_script
    ```
2. 执行图片下载脚本（folder_path为你本地的md文件存储路径，如果本地没存要先去网站上下载到本地）
    ```
   python collection.py --folder_path "the output path of your download images" --output_path ./imgs/
   ```
   ![屏幕截图 2023-03-21 163156](https://user-images.githubusercontent.com/67999981/226603242-56024361-6c90-4b1d-81c3-eb4acb433f57.png)
3. 此时你博客文件夹中的所有图片都被下载到了--output_path 这个目录，你需要把这个文件夹上传至你的服务器，并配置Nginx映射
4. 修改所有md文件中的图片路径(只更域名，会自动保留原图片名称以及描述)
   ```
    python change_address.py --folder_path "the address of your md file in your blog project " --server_address "nginx中配置好的图片url"
   ```
    ![屏幕截图 2023-03-21 191719](https://user-images.githubusercontent.com/67999981/226602754-4a2a94c4-e018-4029-84ea-1e9b013df77a.png)
    
完成，此时再访问你自己的博客网站应该就可以正常显示图片了！<br>
**如果觉得好用麻烦高抬贵手点点star！**