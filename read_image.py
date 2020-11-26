#coding=utf-8
import pytesseract #pip install pytesseract 识别图片信息，引用库之前先安装；然后https://github.com/UB-Mannheim/tesseract/wiki下载对应Tesseract-OCR安装包，安装成功后，在path中增加tesseract.exe的路径
from ShowapiRequest import ShowapiRequest
# from PIL import Image

#第一种pytesseract
# image = Image.open('D:/selenium截图/123.png')
# text = pytesseract.image_to_string(image)
# print(text)

#第二种付钱 ShowapiRequest
r = ShowapiRequest("http://route.showapi.com/1274-2","160666","6c7249013e10412785d5bb98305832fe" )
# r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
# # r.addBodyPara("base64", "")
r.addFilePara("imgFile", "D:/selenium截图/imooc1.png")
res = r.post()
text = res.json()['showapi_res_body']['texts']
print(text) # 返回信息
# pip install ddt  安装数据驱动
