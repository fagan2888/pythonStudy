from PIL import Image, ImageFilter
from PIL import ImageFont, ImageDraw
import random


# 使用PIL库，实现获取缩略图功能
def thumb_image():
    im = Image.open('../../res/mvp.png')
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    # 缩放到50%
    n_w = w / 2
    n_h = h / 2
    im.thumbnail((n_w, n_h))
    print('Resize image size: %sx%s' % (n_w, n_h))
    im.save('../../res/mvp-thumb.jpg', 'jpeg')


# 模糊效果
def blur_image():
    im = Image.open('../../res/mvp.png')
    im_blur = im.filter(ImageFilter.BLUR)
    im_blur.save('../../res/mvp-blur.jpg', 'jpeg')


# 随机字母
def rnd_char():
    return chr(random.randint(65, 90))


# 随机颜色
def rnd_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色
def rnd_color2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


# 获取验证码图片
def get_checkcode_image():
    number = 4
    width = 60 * number
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建font对象
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
    # 创建draw对象
    draw = ImageDraw.Draw(image)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rnd_color())
    # 绘制验证码
    for t in range(number):
        draw.text((60 * t + 10, 10), text=rnd_char(), font=font, fill=rnd_color2())
    # 雾化处理
    image = image.filter(ImageFilter.BLUR)
    image.save('../../res/check_code_image.jpg', 'jpeg')


# thumb_image()

# blur_image()

get_checkcode_image()
