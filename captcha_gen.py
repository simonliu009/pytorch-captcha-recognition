# -*- coding: UTF-8 -*-
from captcha.image import ImageCaptcha  # pip install captcha
from PIL import Image
import random
import time
import captcha_setting
import os

# number = ['0','1','2','3','4','5','6','7','8','9']
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 验证码一般都无视大小写；验证码长度4个字符 这里为节省演示时间 将alphabet ALPHABET注释掉
# def random_captcha_text(char_set=number+alphabet+ALPHABET, captcha_size=5):
# # def random_captcha_text(char_set=number, captcha_size=4):
#     captcha_text = []
#     for i in range(captcha_size):
#         c = random.choice(char_set)
#         captcha_text.append(c)
#     return ''.join(captcha_text)

def random_captcha():
    captcha_text = []
    for i in range(captcha_setting.MAX_CAPTCHA):
        c = random.choice(captcha_setting.ALL_CHAR_SET)
        captcha_text.append(c)
    return ''.join(captcha_text)

# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha()
    captcha_text = random_captcha()
    # captcha_text = random_captcha_text()
    captcha_image = Image.open(image.generate(captcha_text))
    return captcha_text, captcha_image

if __name__ == '__main__':
    count = 1000
    path = captcha_setting.TRAIN_DATASET_PATH    #通过改变此处目录，以生成 训练、测试和预测用的验证码集
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(count):
        now = str(int(time.time()))
        text, image = gen_captcha_text_and_image()
        filename = text+'_'+now+'.png'
        image.save(path  + os.path.sep +  filename)
        print('saved %d : %s' % (i+1,filename))

