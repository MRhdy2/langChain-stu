"""
1.添加Cookie
2.获取Cookie
3.删除Cookie
4.添加Cookie会话
"""
import requests

#添加Cookie
url = 'https://httpbin.org/cookies'
cookies = {'key1': 'value1'}
response = requests.get(url, cookies=cookies)
print(response.text)

# 获取Cookie
response1 = requests.get('https://www.baidu.com')
print(response1.cookies)
for cookie in response1.cookies:
    print(cookie.name, cookie.value)

# 删除Cookie
response2 = requests.get('https://www.baidu.com')
response2.cookies.pop('BDORZ', None)
print(response2.cookies)
response2.cookies.clear()
print(response2.cookies)

# 添加Cookie会话
session = requests.Session()
cookies = {'key2': 'value2'}
session.cookies.update(cookies) #添加Cookie到对话
response3 = session.get('https://httpbin.org/cookies') # 使用包含cookie的会话发送请求
print(response3.text)
session.cookies.clear() #清除会话中的所有Cookie
