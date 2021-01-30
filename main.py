import time
import pyautogui
import requests
import os
 
def getBeijinTime():
     print("\t正在查询许可信息...")
     try:
          # 设置头信息，没有访问会错误400！！！
          hea = {'User-Agent': 'Mozilla/5.0'}
          # 设置访问地址，我们分析到的；
          url = r'http://time1909.beijing-time.org/time.asp'
          # 用requests get这个地址，带头信息的；
          r = requests.get(url=url,headers=hea)
          # 检查返回的通讯代码，200是正确返回；
          if r.status_code == 200: 
               # 定义result变量存放返回的信息源码；
               result = r.text
               # 通过;分割文本；
               data = result.split(";")
               # ======================================================
               # 以下是数据文本处理：切割、取长度，最最基础的东西就不描述了；
               year = data[1][len("nyear") + 3: len(data[1])]
               month = data[2][len("nmonth") + 3: len(data[2])]
               day = data[3][len("nday") + 3: len(data[3])]
               # wday = data[4][len("nwday")+1 : len(data[4])-1]
               hrs = data[5][len("nhrs") + 3: len(data[5]) - 1]
               minute = data[6][len("nmin") + 3: len(data[6])]
               sec = data[7][len("nsec") + 3: len(data[7])]
               # ======================================================
               #beijinTimeStr = "%s/%s/%s %s:%s:%s" % (year, month, day, hrs, minute, sec)
               #print(beijinTimeStr)
               return year,month,day
               

               '''
            # 这个也简单把切割好的变量拼到beijinTimeStr变量里；
               beijinTimeStr = "%s/%s/%s %s:%s:%s" % (year, month, day, hrs, minute, sec)
            # 把时间打印出来看看；
               print(beijinTimeStr)
            # 将beijinTimeStr转为时间戳格式；
            beijinTime = time.mktime(time.strptime(beijinTimeStr, "%Y/%m/%d %X"))
            #返回时间戳；
            return (beijinTime)
            '''
     except:
          return (-1)
 
#
#
#
#
#时间在这
#
#
#
#
def youXiaoQi():
    year,month,day=getBeijinTime()
     
    panDuanY='2021'
    panDuanM='1'
    panDuanD='30'

    if int(panDuanY)>=int(year) and int(panDuanM)>=int(month) and int(panDuanD)>=int(day):
        print("\t此版本(V1.4.1.30)有效期到：",end='')
        print(panDuanY,end='')
        print("年",end='')
        print(panDuanM,end='')
        print("月",end='')
        print(panDuanD,end='')
        print("日23:59\n\t超出有效期请联系管理员\n")
        return 1
    else:
        return 0
     




#获取任务量
def jiChuHuoQv():
    print("提示：请满足以下几个基本条件\n\t显示设置窗口缩放放大为：100%\n\t电脑端微信版本为3.1.0.41\n\t其他问题请联系管理员\n")
    print("输入今日任务量:")
    ceShiNum=int(input("\t测试："))
    tingLiNum=int(input("\t听力："))
    #yueDuNum=int(input("阅读："))
    yueDuNum=0
    danCiNum=int(input("\t单词："))
    danCiNumPanDuan=0
    if danCiNum!=0:
        danCiNumPanDuan=int(input("\t是否有拼写？  1有  0没有："))
    danCiNumO=int(input("\t从第几个单词包开始（不知道填什么就填1）"))
    print("\n\t按任意键后有三秒时间把鼠标放置到基本点")
    print("\t按任意键开始",end='')
    aaaaaaa=input()
    return ceShiNum,tingLiNum,yueDuNum,danCiNum,danCiNumPanDuan,danCiNumO

#引导获取基础位置
def jiChuWeiZhi():
    print("3秒后获取基础位置并开始做单词，开始后软件接管鼠标，请不要影响它操作哦！")
    time.sleep(3)
    x,y = pyautogui.position() #返回鼠标的坐标
    posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
    x=int(str(x).rjust(4))
    y=int(str(y).rjust(4))
    return x,y

#听力模块
def tingLi(tingLiNum,x,y):
    if tingLiNum==0:
        print("无听力")
        return
    print("听力开始\t",end='')
    #进入听力模块
    x=x+68
    y=y-301
    pyautogui.click(x,y,clicks=1,button='left')
    x=x-57
    y=y-163
    xx=x
    yy=y
    #在第一个上备份1位置
    for i in range(0,tingLiNum):
        x=xx+(i*100)
        y=yy
        time.sleep(1)
        pyautogui.click(x,y,clicks=1,button='left')
        #确认
        x=xx
        x=x+152
        y=y+252
        time.sleep(1)
        pyautogui.click(x,y,clicks=1,button='left')
        #循环
        x=x-97
        y=y+117
        time.sleep(1)
        for j in range(0,7):
            pyautogui.click(x,y,clicks=1,button='left')
            time.sleep(20)
            x=x+268
            y=y+115
            pyautogui.click(x,y,clicks=1,button='left')
            x=x-268
            y=y-115
            time.sleep(2)
        #点击完成
        x=xx+86
        y=yy+447
        time.sleep(1.5)
        pyautogui.click(x,y,clicks=1,button='left')
    #点击返回
    x=xx-38
    y=yy-148
    time.sleep(1.5)
    pyautogui.click(x,y,clicks=1,button='left')
    print("听力结束")

#阅读模块    
def yueDu(yueDuNum,x,y):
    if yueDuNum==0:
        print("无阅读")
        return
    print("阅读开始\t",end='')
    #进入阅读模块
    x=x+240
    y=y-303
    pyautogui.click(x,y,clicks=1,button='left')
    x=x-240+11
    y=y+303-464
    xx=x
    yy=y
    #在第一个上备份1位置
    for i in range(0,yueDuNum):
        x=xx+(i*100)
        y=yy
        time.sleep(1)
        pyautogui.click(x,y,clicks=1,button='left')
        #循环
        time.sleep(1)
        x=x+323
        y=y+472
        for j in range(0,6):
            pyautogui.click(x,y,clicks=1,button='left')
            time.sleep(1)
            #容错确定
            x=x-171
            y=y-258
            time.sleep(1)
            pyautogui.click(x,y,clicks=1,button='left')
            x=x+171
            y=y+258

            #容错选型
            x=x-300
            y=y-482
            time.sleep(1)
            pyautogui.click(x,y,clicks=1,button='left')
            x=x+300
            y=y+482
            
            #选项
            #可以写一个判断的东西正确率
            #选项
            x=x-300
            y=y-358
            time.sleep(1)
            pyautogui.click(x,y,clicks=1,button='left')
            x=x+300
            y=y+358
            x=x-300
            y=y-482
            x=x+300
            y=y+482
            time.sleep(1)
            pyautogui.click(x,y,clicks=1,button='left')
        #点击完成
        print(x,y)
        x=x-176
        y=y-73
        time.sleep(1)
        pyautogui.click(x,y,clicks=1,button='left')
    #点击返回
    x=xx-38
    y=yy-148
    time.sleep(1.5)
    pyautogui.click(x,y,clicks=1,button='left')
    print("阅读结束")

#测试题模块
def ceShi(ceShiNum,x,y):
    if ceShiNum==0:
        print("无测试题")
        return
    print("测试题开始\t",end='')
    xx=x
    yy=y
    #进入测试题模块
    x=x+60
    y=y-462
    pyautogui.click(x,y,clicks=1,button='left')
    #确认
    x=xx+161
    y=yy-236
    time.sleep(1)
    pyautogui.click(x,y,clicks=1,button='left')
    #开始
    x=xx+281
    y=yy-355
    time.sleep(1)
    pyautogui.click(x,y,clicks=1,button='left')
    x=xx+68
    y=yy-209
    for i in range(0,50):
        #判断对错
        time.sleep(2)
        pyautogui.click(x,y,clicks=1,button='left')
    #点击完成
    x=xx+62
    y=yy-136
    time.sleep(1.5)
    pyautogui.click(x,y,clicks=1,button='left')
    #点击返回
    x=xx-27
    y=yy-615
    time.sleep(1)
    pyautogui.click(x,y,clicks=1,button='left')
    print("测试题结束")

#单词模块
def danCi(danCiNum,x,y,danCiNumPanDuan,danCiNumO):
    #xx,yy是基准点
    xx=x
    yy=y
    #进入模块
    x=x+281
    y=y-442
    n=0
    time.sleep(1)
    pyautogui.click(x,y,clicks=1,button='left')
    if danCiNumPanDuan!=0:
        danCiNum=danCiNum-1
        #print("单词——拼写开始")
        '''
        x=xx+305
        y=yy-360
        time.sleep(1)
        pyautogui.click(x,y,clicks=1,button='left')
        #点击确定
        x=xx+161
        y=yy-212
        time.sleep(1)
        pyautogui.click(x,y,clicks=1,button='left')
        #挺难的模块
        #没了
        #下次试试
        '''
        #dxx,dyy第一个单词包的基本位置
        dxx=xx+7
        dyy=yy-202
        #pyautogui.moveTo(dxx,dyy,duration=0.25)
        #a=input()
    else:
        #print("123")
        dxx=xx+14
        dyy=yy-337
    danCiNumO=danCiNumO-1
    for i in range(danCiNumO,danCiNum):
        if i>=4:
            if n==0:
                dxx=dxx
                dyy=dyy+110
                n=1
        x=dxx+(i*100)
        y=dyy
        if n==1:
            x=x-400
        #进入卡包
        time.sleep(1)
        pyautogui.moveTo(x,y,duration=0.25)
        #a=input()
        print("单词包",end='')
        print(i+1,end='')
        print("开始",end='')
        pyautogui.click(x,y,clicks=1,button='left')
        for k in range(1,260):
            if k==50:
                time.sleep(1)
                x=xx+159
                y=yy-65
                pyautogui.click(x,y,clicks=1,button='left')
            if k==49:
                time.sleep(1)
                x=xx+159
                y=yy-65
                pyautogui.click(x,y,clicks=1,button='left')
            if k==51:
                time.sleep(1)
                x=xx+159
                y=yy-65
                pyautogui.click(x,y,clicks=1,button='left')
            if k==52:
                time.sleep(1)
                x=xx+159
                y=yy-65
                pyautogui.click(x,y,clicks=1,button='left')
            time.sleep(1)
            x=xx+70
            y=yy-211
            pyautogui.click(x,y,clicks=1,button='left')
            y=y-150
            time.sleep(0.5)
            pyautogui.dragTo(x,y,0.2,button='left')
            y=y+150
            pyautogui.moveTo(x,y,duration=0.25)
        x=xx-29
        y=yy-612
        time.sleep(1)
        pyautogui.click(x,y,clicks=1,button='left')
    print("单词包",end='')
    print(i+1,end='')
    print("结束")
        
def jiemian():
     os.system("color F0")
     os.system("mode con cols=62 lines=26")
    
    
#main()
jiemian()
yxq=youXiaoQi()
if yxq==0:
    print("已超出许可期，请联系管理员获取新版本")
    exit()
ceShiNum,tingLiNum,yueDuNum,danCiNum,danCiNumPanDuan,danCiNumO=jiChuHuoQv()
x,y=jiChuWeiZhi()
#听力
tingLi(tingLiNum,x,y)
#阅读
#yueDu(yueDuNum,x,y)
#测试
ceShi(ceShiNum,x,y)
#单词
danCi(danCiNum,x,y,danCiNumPanDuan,danCiNumO)


