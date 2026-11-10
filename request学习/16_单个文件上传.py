"""
request.post(
    url # 上传文件的URL地址，必选参数
    files # 要上传的文件名，可选参数
)
"""
import requests


url = "http://httpbin.org/post"
file_path = "test.txt"
#读取文件
with open(file_path, "rb") as f:
    files = {"file": f}
    #通过字典传递文件参数
    response = requests.post(url, files=files)

print(response.text)

