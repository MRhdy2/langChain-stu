"""
response.status_code ## 获取响应的状态码，返回的是整数类型
response.ok ## 判断响应是否成功，返回的是布尔类型
response.raise_for_status() ## 如果响应的状态码是错误的，抛出HTTPError异常
"""
import requests

response = requests.get('http://www.baidu.com')
print(response.status_code)  # 打印响应的状态码
print(response.ok)  # 获取响应的布尔值
print(response.raise_for_status())  # 如果响应的状态码是错误的，抛出HTTPError异常