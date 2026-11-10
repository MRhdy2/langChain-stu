"""
response.history ## 获取重定向的历史记录，返回的是一个列表，列表中的每个元素都是一个Response对象
response.url ## 获取最终的URL
"""
import requests
response = requests.get('http://www.baidu.com')
print(response.history) # 获取重定向的历史记录，返回的是一个列表，列表中的每个元素都是一个Response对象
print(response.url) # 获取最终的URL