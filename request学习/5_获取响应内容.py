"""
response.text ## 获取响应体的文本内容，返回的是字符串类型
response.content ## 获取响应体的二进制内容，返回的是字节类型
response.json() ## 获取响应体的json内容，返回的是字典类型
"""

import requests
response = requests.get('http://www.baidu.com/')
print(response.text) # 以字符串的形式输出响应体内容
print(response.content) # 以字节的形式输出响应体内容
print(response.json()) # 以字典的形式输出响应体内容