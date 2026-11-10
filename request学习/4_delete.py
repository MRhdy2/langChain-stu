import requests
"""语法
requests.delete(
        url, # 请求的URL地址,必选参数
        params=None, # 用于指定URL中的查询参数，可以是一个字典或字符串,可选参数
        **kwargs) # 用于传递其他参数，如请求头、超时设置等，可选参数
**kwargs参数说明：
    headers: 用于指定请求头信息，如User-Agent、Content-Type等。
    cookies: 用于指定请求的Cookie信息。
    timeout: 用于设置请求的超时时间，单位为秒。  
    auth: 用于指定HTTP身份验证信息。如果需要进行身份验证，可以传递一个包含用户名和密码的元组。
"""
url = 'http://www.baidu.com/'  # 请求的URL地址
response = requests.delete(url, timeout=5)  # 设置超时时间为5秒

print(response.status_code)  # 打印响应状态码
print(response.text)  # 打印响应的内容
