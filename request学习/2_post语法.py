import requests
""" 语法
requests.post(
        url, # 请求的URL地址,必选参数
        data=None, # 用于指定请求体数据可以为一个字典、字节序列或文件对象,可选参数
        json=None, # 用于指定JSON格式的请求体数据,可选参数
        **kwargs) # 用于传递其他参数，如请求头、超时设置等，可选参数
**kwargs参数说明：
    headers: 用于指定请求头信息，如User-Agent、Content-Type等。
    cookies: 用于指定请求的Cookie信息。
    timeout: 用于设置请求的超时时间，单位为秒。
    auth: 用于指定HTTP身份验证信息。如果需要进行身份验证，可以传递一个包含用户名和密码的元组。
"""

# 发送POST请求
url = 'https://www.baidu.com/'
data = {'key': 'value'}  # 请求体数据
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.post(url, data=data, headers=headers, timeout=5)  # 设置超时时间为5秒

print(response.status_code)  # 打印响应状态码
print(response.text)  # 打印响应的内容