#base64加密
import base64
url = "Email                   :   cszhk0310@163.com\
    \nBlog site               :   https://www.zhukang.tech\
    \nWechat official account :   CarpeDiem-zhukang\
    \nlogan                  :   正心，诚意，进德，修身，养气，为学，笃行，慎独。"
bytes_url = url.encode("utf-8")
str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
print(str_url)

#base64解密
url = "RW1haWwgICAgICAgICAgICAgICAgICAgOiAgIGNzemhrMDMxMEAxNjMuY29tICAgIApCbG9nIHNpdGUgICAgICAgICAgICAgICA6ICAgaHR0cHM6Ly93d3cuemh1a2FuZy50ZWNoICAgIApXZWNoYXQgb2ZmaWNpYWwgYWNjb3VudCA6ICAgQ2FycGVEaWVtLXpodWthbmcgICAgCmxvZ2FuICAgICAgICAgICAgICAgICAgOiAgIOato+W/g++8jOivmuaEj++8jOi/m+W+t++8jOS/rui6q++8jOWFu+awlO+8jOS4uuWtpu+8jOesg+ihjO+8jOaFjueLrOOAgg=="
str_url = base64.b64decode(url).decode("utf-8")
print(str_url)
