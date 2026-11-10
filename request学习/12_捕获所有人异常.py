"""
RequestException是所有异常的基类，可以用于捕获所有异常。
当网络请求出现异常时，例如连接超时、DNS解析失败等，可以使用该异常捕获并处理。
"""
import requests
from requests.exceptions import RequestException

try:
    response = requests.get('https://www.example.com')
    print("响应正常，执行下一步")
except RequestException as e:
    print(f"请求异常: {e}")
