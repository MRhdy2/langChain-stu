"""
发送多个相关请求时，可以使用会话对象来管理会话信息，以便在请求之间保持某些参数（如cookies、headers等）的状态。
使用会话对象可以提高请求的效率，并简化代码的管理。
"""
import requests
# 创建一个会话对象
session = requests.Session()
#设置会话级别的请求头
session.headers.update({'User-Agent': 'Mozilla/5.0'})
#第一个请求
response1 = session.get('https://httpbin.org/cookies/set/sessioncookie/123456789',data={'key1': 'value1'})
print(response1.text)
#第二个请求
response2 = session.get('https://httpbin.org/cookies')
print(response2.text)
#第三个请求
response3 = session.get('https://httpbin.org/get', params={'param1': 'value1'})
print(response3.text)
#关闭会话
session.close()
