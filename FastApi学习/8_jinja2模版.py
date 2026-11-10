"""
jinjia2模板存在三种语法：
1. 变量语法：{{ variable }}，用于输出变量的值。
2. 控制语法：{% statement %}，用于控制流程，如循环、条件
3. 注释语法：{# comment #}，用于添加注释，不会在输出中显示。
"""

"""
jinja2模板过滤器：
{{ 'abc'| captialize  }}  # Abc 把值的首字母大写，其他字母小写

{{ 'abc'| upper  }} # ABC  把值的所有字母大写  lower：把值的所有字母小写

{{ 'hello world'| title  }} # Hello World 把值的每个单词首字母大写

{{ "hello world"| replace('world','yuan') | upper }} # HELLO YUAN 替换并大写

{{ 18.18 | round | int }} # 18 向上取整

trim ：去掉值的前后空格
striptags ：去掉值的html标签
join ：把值的列表拼接成字符串
safe ：把值标记为安全的，防止被转义
"""

"""
jinja2模板控制语法：
1.分支控制
{% if condition %}  
  <p>条件为真时显示的内容</p>
{% else %}或者{% elif condition %}  
  <p>条件为假时显示的内容</p>
{% endif%}
2.循环控制
{% for item in list %}
  <p>{{ item }}</p>
{% endfor %}
"""
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()  # 实例化 FastAPI对象
templates = Jinja2Templates(directory="templates")  # 实例化Jinja2对象，并将文件夹路径设置为以templates命令的文件夹


@app.get('/')
def hello(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={
            'request': request,  # 注意，返回模板响应时，必须有request键值对，且值为Request请求对象
            'user': 'yuan',
            "books": ["金瓶梅", "聊斋", "剪灯新话", "国色天香"],
            "booksDict": {
                "金瓶梅": {"price": 100, "publish": "苹果出版社"},
                "聊斋": {"price": 200, "publish": "橘子出版社"},
            }
        }
    )
if __name__ == "__main__":
    uvicorn.run("8_jinja2模版:app", host="127.0.0.1", port=8000)
