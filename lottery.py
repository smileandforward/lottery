#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Create by H
# Create on 2022/9/8

import random
import time
import datetime
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
先判断今天是星期几，然后决定输出福彩还是体彩的随机数
"""

t = time.localtime()
week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
#得到今天的日期
jintian = datetime.date(t.tm_year,t.tm_mon,t.tm_mday)
# print(jintian)
#计算出今天是星期几,由于weekday使用0-6表示星期一到星期日，所以用一个列表把每一天转换出来
xingqi = week_list[jintian.weekday()]
# print(xingqi)

def fc_number():
    """
    福彩双色球投注区分为红球号码区和蓝球号码区，红球号码范围为01～33，蓝球号码范围为01～16。
    双色球每期从33个红球中开出6个号码，从16个蓝球中开出1个号码作为中奖号码，
    双色球玩法即是竞猜开奖号码的6个红球号码和1个蓝球号码，顺序不限。
    6个红球+1个蓝球=1注（2元）
    每周二、四、日21：15开奖；每周三期，开奖号码通过摇奖方式产生。
    """
    fc_red = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']
    fc_blue = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']
    fc_red_ball = random.sample(fc_red, 6)
    fc_blue_ball = random.sample(fc_blue, 1)
    return "福彩双色球前区号码红球"+str(fc_red_ball)+"后区号码蓝球"+str(fc_blue_ball)

def tc_number():
    """
    体彩大乐透投注区分为前区号码和后区号码，前区号码范围为01～35，后区号码范围为01～12。
    大乐透每期从35个前区号码中开出5个号码，从12个后区号码中开出2个号码作为中奖号码，
    大乐透玩法即是竟猜开奖号码的5个前区号码和2个后区号码，顺序不限。
    5个红球+2个蓝球=1注（2元），追加投注：1元（最多可中1800万）
    追加投注仅参与一、二等奖的奖金分配，一、二等奖追加投注奖金为当期基本投注对应单注奖金的80%。
    每周一、三、六20:25开奖；每周三期，开奖号码通过摇奖方式产生。
    """
    tc_red = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
    tc_blue = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    tc_red_ball = random.sample(tc_red, 5)
    tc_blue_ball = random.sample(tc_blue, 2)
    return "体彩大乐透前区号码红球" + str(tc_red_ball) + "后区号码蓝球" + str(tc_blue_ball)

if __name__=='__main__':
    # 体彩一，三，六开奖
    # 福彩二，四，日开奖
    # 周一买福彩双色球，周二开奖，
    # 周二买体彩大乐透，周三开奖，
    # 周三买福彩双色球，周四开奖，
    # 周四买体彩大乐透，周六开奖
    # 周四买福彩双色球，周日开奖
    if xingqi == '星期一':
        zhuyishixiang = "今天是星期一，买福彩双色球，明天周二开奖"
        print("今天是星期一，买福彩双色球，明天周二开奖")
        luck_number = fc_number()
        print(luck_number)
        lucky_number = ''
    if xingqi =='星期二':
        zhuyishixiang ="今天是星期二,今天是福彩双色球开奖日，记得查看开奖号码。另外今天买体彩大乐透，明天周三开奖。"
        print("今天是星期二,今天是福彩双色球开奖日，记得查看开奖号码。另外今天买体彩大乐透，明天周三开奖。")
        luck_number = tc_number()
        print(luck_number)
        lucky_number = ''
    if xingqi == '星期三':
        zhuyishixiang ="今天是星期三,今天是体彩大乐透开奖日，记得查看开奖号码。另外今天买福彩双色球，明天周四开奖。"
        print("今天是星期三,今天是体彩大乐透开奖日，记得查看开奖号码。另外今天买福彩双色球，明天周四开奖。")
        luck_number = fc_number()
        print(luck_number)
        lucky_number = ''
    if xingqi == '星期四':
        zhuyishixiang ="今天是星期四,今天是福彩双色球开奖日，记得查看开奖号码。另外周四或者周五买体彩大乐透，周六开奖。"
        print("今天是星期四,今天是福彩双色球开奖日，记得查看开奖号码。另外周四或者周五买体彩大乐透，周六开奖。")
        luck_number = tc_number()
        print(luck_number)
        lucky_number = ''
    if xingqi == '星期五':
        zhuyishixiang ="今天是星期五,周五买体彩大乐透，周六开奖；周五买福彩双色球，周日开奖。"
        print("今天是星期五,周五买体彩大乐透，周六开奖；周五买福彩双色球，周日开奖。")
        luck_number = fc_number()
        print(luck_number)
        lucky_number = tc_number()
        print(lucky_number)
    if xingqi == '星期六':
        zhuyishixiang ="今天是星期六,记得核对体彩大乐透开奖号码。另外如果没有买福彩双色球，可以参考下边号码"
        print("今天是星期六,记得核对体彩大乐透开奖号码。另外如果没有买福彩双色球，可以参考下边号码")
        luck_number = fc_number()
        print(luck_number)
        lucky_number = ''
    if xingqi == '星期日':
        zhuyishixiang ="今天是星期日,记得核对福彩双色球开奖号码。另外今天买体彩大乐透，周一开奖"
        print("今天是星期日,记得核对福彩双色球开奖号码。另外今天买体彩大乐透，周一开奖")
        luck_number = tc_number()
        print(luck_number)
        lucky_number = ''


    #发送邮件
    #发件人信息
    user = 'hezihui_forward@163.com'
    #邮箱授权码
    password = 'ZNRDROYZYILTMACW'
    #收件人地址，可以是多个，用列表显示
    toaddress = ['874590081@qq.com']

    content = "{},\n{},\n{}".format(zhuyishixiang,luck_number,lucky_number)
    text_content = MIMEText('<font color=red,size=20>{}<br><br><br>{}<br><br><br>{}<br><br><br></font>'.format(zhuyishixiang,luck_number,lucky_number))

    #封装邮件
    msg = MIMEMultipart()
    msg.attach(text_content)

    #邮箱头部显示的发件人信息
    msg['From'] = user
    #邮箱头部显示的收件人信息
    msg['To'] = toaddress[0]
    #主题
    msg['Subject'] = Header('今日自选彩票号码')

    #发送邮件
    try:
        #第一步，连接到smtp服务器，注意163邮箱的smtp端口是25，qq用的是465端口
        s = smtplib.SMTP('smtp.163.com')
        #第二步，登录到服务器
        s.login(user=user,password=password)
        #第三步，发送邮件
        s.sendmail(user,toaddress,msg.as_string())
        print('success')
        s.quit()
    except smtplib.SMTPException as e:
        print('登录邮箱出现问题',e)










