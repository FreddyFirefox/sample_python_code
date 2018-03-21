import qrcode
from qrcode.image.pil import PilImage
from PIL import Image

# 实例化QRCode
qr = qrcode.QRCode(
    version=2,  # version影响尺寸　[1,40]数字越大尺寸越大
    error_correction=qrcode.constants.ERROR_CORRECT_H,# 纠错级别　从低到高为L M Q H
    box_size=10,  # 每个格子的像素大小
    border=1 # 格子边框厚度　默认４
)

#   Add data to this QR Code.
qr.add_data("https://www.baidu.com/s?wd=心")

# Compile the data into a QR Code array.
qr.make(fit=True)

# Make an image from the QR Code data.
img = qr.make_image()
print(type(img))
# img = img.convert("RGBA")   Returns a converted copy of this image
img = img.convert("RGB")

# 二维码图片的width  height
img_w, img_h = img.size

factor = 3

# 预留二维码中心图片的尺寸　为二维码的四分之一
size_w = int(img_w / factor)
size_h = int(img_h / factor)

# 加载图片
icon = Image.open("jt.png")

# 获取图片的尺寸
icon_w, icon_h = icon.size

# 如果图片width 大于预留尺寸　则设为预留尺寸
if icon_w > size_w:
    icon_w = size_w

# 如果图片height大于预留尺寸　则设置为预留尺寸
if icon_h > size_h:
    icon_h = size_h

# 改变图片的尺寸
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

# 计算将图片贴到二维码中心的坐标
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)

# 将图片贴到二维码上
img.paste(icon, (w, h), None)

# 保存二维码
img.save("test_qrcode.png")


