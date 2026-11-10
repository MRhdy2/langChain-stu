"""
response.encoding ## 获取响应内容的字符编码
response.cookies ## 获取响应的Cookie信息
"""
import requests

response = requests.get('http://www.baidu.com')
print(response.encoding)  # 获取响应内容的字符编码
print(response.cookies)  # 获取响应的Cookie信息
html = response.text
print(html) 