"""
response.headers ## 获取响应头部的信息，返回的是字典类型
response.headers['header_name'] ## 获取响应头部字段的信息
"""
import requests
response = requests.get('https://www.baidu.com')
print(response.headers)  # 获取响应头部的信息，返回的是字典类型
print(response.headers['Date'])  # 获取响应头部字段的信息