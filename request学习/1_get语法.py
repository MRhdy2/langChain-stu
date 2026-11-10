import requests
""" 语法
requests.get(
        url, # 请求的URL地址,必选参数
        params=None, # 用于指定查询参数,可选参数
        **kwargs) # 用于传递其他参数，如请求头、超时设置等，可选参数
**kwargs参数说明：
    headers: 用于指定请求头信息，如User-Agent、Content-Type等。
    cookies: 用于指定请求的Cookie信息。
    timeout: 用于设置请求的超时时间，单位为秒。
"""
#发送GET请求
url = 'https://www.baidu.com/s'
params = {'wd': 'python'}  # 查询参数，表示搜索关键词为'python'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, params=params, headers=headers, timeout=5)  # 设置超时时间为5秒

print(response.status_code)  # 打印响应状态码

print(response.text)  # 打印响应的HTML内容