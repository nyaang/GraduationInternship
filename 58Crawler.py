import requests
import time
import csv,json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from decode58 import decode58main
ua = UserAgent()
headers = {"User-Agent": ''}
urllist = []
linklist = json.load(open("./DATA/links.json", 'r'))
def getrequest(url):
    # 使用随机的user-agent
    headers["User-Agent"] = ua.random
    try:
        r = requests.get(url, headers=headers, timeout=8)
        print("requested from:" + url)
        return r
    except BaseException:
        print("error")
        time.sleep(3)
        r = getrequest(url)
        return r
def geturllist():
    for i in range(1, 70):
        url = "https://bj.58.com/haidian/zufang/pn" + str(i) + "/?PGTID=0d300008-0047-7032-5dce-5d45cf6aae27&ClickID=2"
        urllist.append(url)
    for url in urllist:
        r = getrequest(url)
        bsobj = BeautifulSoup(r.content, 'lxml')
        Linkinfos=bsobj.find_all("a",{"onclick":"clickLog('from=fcpc_zflist_gzcount');"})
        for Linkinfo in Linkinfos:
            linklist.append(Linkinfo.get('href'))
    links=list(set(linklist))
    linkfile = open('links.json', 'w')
    json.dump(
        links,
        linkfile,
        indent=4,
        sort_keys=False,
        ensure_ascii=False)
    linkfile.close()
#geturllist()

def run():
    with open("58.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 先写入columns_name
        writer.writerow(["租赁方式", "户型", "面积", "装修", "朝向", "高低", "楼层","小区名","区域","次级区域","详细地址","详情","亮点","描述","URL","价格","周期","押金"])
        for link in linklist:
            try:
                r = getrequest(link)
                content=decode58main(r.content)
                bsobj = BeautifulSoup(content, 'lxml')
                basicInfo=bsobj.find("ul",{"class":"f14"})
                HousePay=bsobj.find("div",{"class":"house-pay-way f16"})
                Price=HousePay.span.get_text().split()[0]  #价格
                YuanYue=HousePay.span.get_text().split()[1] #周期
                PayWay=HousePay.span.next_sibling.next_sibling.get_text()   #押几付几
                ZuLinFangShi=basicInfo.li
                LeiXing=ZuLinFangShi.span.next_sibling.get_text()   #租赁方式
                FangWuLeiXing = ZuLinFangShi.next_sibling.next_sibling
                Huxing=FangWuLeiXing.span.next_sibling.get_text().split()[0]  #户型
                MianJi=FangWuLeiXing.span.next_sibling.get_text().split()[1]  #面积
                try:
                    ZhuangXiu=FangWuLeiXing.span.next_sibling.get_text().split()[3] #装修
                except:
                    ZhuangXiu=" "
                ChaoXiang=FangWuLeiXing.next_sibling.next_sibling
                FangXiang=ChaoXiang.span.next_sibling.get_text().split()[0] #朝向，东南西北
                GaoDi=ChaoXiang.span.next_sibling.get_text().split()[1] #高低，高中低
                try:
                    LouCeng=ChaoXiang.span.next_sibling.get_text().split()[3]   #楼层
                except:
                    LouCeng=" "
                XiaoQu=ChaoXiang.next_sibling.next_sibling
                XiaoQuName=XiaoQu.a.get_text()  #小区名
                QuYu=XiaoQu.next_sibling.next_sibling
                QuYuName=QuYu.span.next_sibling.get_text().split()[0]   #区域
                CiJiQuYu=QuYu.span.next_sibling.get_text().split()[1]   #次级区域
                XiangXiDiZhi=QuYu.next_sibling.next_sibling.span.next_sibling.get_text()    #详细地址

                try:
                    XiangQing=bsobj.find("ul",{"class":"house-disposal"}).get_text().replace("\n", " ");    #详情
                except:
                    XiangQing=" "
                Detail=bsobj.find("ul",{"class":"introduce-item"})
                try:
                    LiangDian=Detail.li.span.next_sibling.next_sibling.get_text().replace("\n", " ")    #亮点
                except:
                    LiangDian=" "
                try:
                    MiaoShu=Detail.li.next_sibling.next_sibling.get_text()  #描述
                except:
                    MiaoShu=" "
                try:
                    writer.writerow([LeiXing,Huxing,MianJi,ZhuangXiu,FangXiang,GaoDi,LouCeng,XiaoQuName,QuYuName,CiJiQuYu,XiangXiDiZhi,XiangQing,LiangDian,MiaoShu,link,Price,YuanYue,PayWay])
                except UnicodeEncodeError:
                    MiaoShu=MiaoShu.replace(u'\xa0', u' ')
                    try:
                        writer.writerow(
                                [LeiXing, Huxing, MianJi, ZhuangXiu, FangXiang, GaoDi, LouCeng, XiaoQuName, QuYuName, CiJiQuYu,
                                 XiangXiDiZhi, XiangQing, LiangDian, MiaoShu,link,Price,YuanYue,PayWay])
                    except UnicodeEncodeError:
                        writer.writerow(
                            [LeiXing, Huxing, MianJi, ZhuangXiu, FangXiang, GaoDi, LouCeng, XiaoQuName, QuYuName, CiJiQuYu,
                             XiangXiDiZhi, XiangQing, LiangDian, " ",link,Price,YuanYue,PayWay])
            except:
                print("continue")
                continue
run()