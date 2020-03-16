from URLManage import URLManage
import time
import datetime
import requests
from HTMLDownload import HTMLDownload
from DataOutput import write_header
from DataOutput import writeTableFromList
from DataOutput import readTableFromCsv
import os



def getPath(filePath):
    # filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    if not os.path.exists(filePath):
        os.mkdir(filePath)
    os.chdir(filePath)



# 行业中心连接数据
# http://quote.eastmoney.com/center/boardlist.html?st=ChangePercent&sortRule=0#industry_board
# 默认是4页
def industryBoardContent():
    #存盘路径
    filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    dateTime = datetime.datetime.now().strftime('%Y%m')
   
    getPath(filePath)
    url = 'http://quote.eastmoney.com/center/boardlist.html?st=ChangePercent&sortRule=0#industry_board'
    headers = ['行业名称', 'url', '没用', 'url']
    

    fileName = 'industryBoard' + str(dateTime)
    write_header(headers, fileName)

    a = HTMLDownload(url)
    writeTableFromList(a.href('#table_wrapper-table', 1), 1, fileName)
    writeTableFromList(a.href('#table_wrapper-table', 2), 2, fileName)
    writeTableFromList(a.href('#table_wrapper-table', 1), 3, fileName)
    writeTableFromList(a.href('#table_wrapper-table', 1), 4, fileName)

    return filePath + fileName + '.csv'

# url连接如下格式 http://data.eastmoney.com/bkzj/BK0738.html
def companysItemImpl(fromUrl, foreignKey):
    #存盘路径
    a = HTMLDownload(fromUrl)
    return a.companysItem('#dt_1', 16, foreignKey)

def companysHrefImpl(fromUrl, foreignKey):
    a = HTMLDownload(fromUrl)
    return a.companysHref('#dt_1', 40, foreignKey)




def companyTotal():
    #读取csv文件进行解析获取fromUrl
      
    headers = ['所属行业', '序号', 'url连接', '名称', '相关', '最新价格', 
        '今日涨跌幅','今日主力净流入_净额','今日主力净流入_净占比', '今日超大单净流入_净额',
        '今日超大单净流入_净占比','今日中单净流入_净额','今日中单净流入_净占比', '今日小单净流入_净额', '今日小单净流入_净占比']

    filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    dateTime = datetime.datetime.now().strftime('%Y%m')
    
    getPath(filePath)

    companyListFileName = "companyList" + str(dateTime)
    companyUrlFileName = "companyUrl" + str(dateTime)
    industryBoardFileName = 'industryBoard' + str(dateTime) + '.csv'
    #读取当天的industryBoard文件获取url
    industryList = readTableFromCsv(industryBoardFileName)

    companyList = [] #保存公司列表
    companyUrl = [] #保存公司Url

    print("*******industryBoard***********")
    print(industryList)
    i = 0
    for lst in industryList:
        try:
            writeTableFromList(companysItemImpl(lst[1], lst[0]), 1, companyListFileName)
            writeTableFromList(companysHrefImpl(lst[1], lst[0]), 1, companyUrlFileName)
            i += 1
            print("开始下载第" + str(i) + "个行业")
        except:
            print('执行出错继续***********')

# 公司概况清单
def companySurveyImpl():
    headers = [['公司名称','英文名称','曾用名','A股代码', 'A股简称','B股代码','B股简称',
        'H股代码','H股简称','证券类别','所属东财行业','上市交易所','所属证监会行业','总经理','法人代表','董秘','董事长','证券事务代表', '独立董事','联系电话',
        '电子信箱','传真','公司网址','办公地址','注册地址','区域','邮政编码','注册资本(元)','工商登记','雇员人数','管理人员人数','律师事务所','会计师事务所',
        '公司简介','经营范围','所属行业公司代码'
    ]]
    filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    dateTime = datetime.datetime.now().strftime('%Y%m')
    getPath(filePath)
    #公司财务清单列表
    companySurveyFileName = 'companySurvey' + str(dateTime)

    companySurveyList = [] 
    companyUrlFileName = "companyUrl" + str(dateTime) + '.csv'
    companySurveyUrlList =  readTableFromCsv(companyUrlFileName)
    print("*********公司概况分析*******************")
    #print(companySurveyUrlList)
    #写入表头
    writeTableFromList(headers, 0, companySurveyFileName)
    i = 0
    for lst in companySurveyUrlList:
        try:
            a = HTMLDownload(lst[3])
            result = a.companySurvey('#Table0', 40, lst[40] + lst[0])
            i += 1
            writeTableFromList(result, i, companySurveyFileName)
        except:
            print('执行出错继续***********')

# 经营分析
def businessAnalysisImpl():
    headers = [[ '分类类别','主营构成','主营收入(元)','收入比例',
        '主营成本(元)','成本比例','主营利润(元)','利润比例','毛利率(%)','企业代码', '行业代码'
    ]]
    filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    dateTime = datetime.datetime.now().strftime('%Y%m')
    getPath(filePath)
    #公司财务清单列表
    businessAnalysisFileName = 'businessAnalysis' + str(dateTime)

    businessAnalysis = [] 
    companyUrlFileName = "companyUrl" + str(dateTime) + '.csv'
    businessAnalysisUrlList =  readTableFromCsv(companyUrlFileName)
    print("********公司经营分析********")
    #print(businessAnalysisUrlList)
    #写入表头
    writeTableFromList(headers, 0, businessAnalysisFileName)
    i = 0
    for lst in businessAnalysisUrlList:
        try:
            a = HTMLDownload(lst[5])
            result = a.businessAnalysis('tr > .tips-dataL, tr > .tips-fieldnameL', 9, lst[40] , lst[0])
            i += 1
            writeTableFromList(result, i, businessAnalysisFileName)
        except:
            print('执行出错继续***********')

# 公司财务分析(杜邦分析)
def financeAnalysisDubangImpl():
    headers = [[ '分类','时间','净资产收益率','总资产净利率','归属母公司股东的净利润占比','权益乘数',
        '营业净利润率','总资产周转率','资产负债率','净利润','营业总收入','营业总收入','资产总额',
        '负债总额','资产总额','收入总额','成本总额','流动资产','非流动资产','营业总收入','营业成本',
        '期间费用','货币资金','可供出售金融资产','无形资产','共允价值变动收益','营业税金及附加',
        '交易性金融资产','持有至到资产','持有至到期投资','营业外收入','所得税费用','财务费用','应收账款',
        '长期股权投资','商誉','投资收益','资产减值损失','销售费用','预付账款','投资性房地产','长期待摊费用',
        '营业外支出','管理费用','其他应收款','固定资产','递延所得税资产','存货','在建工程','其他非流动性资产',
        '其他流动性资产','所属行业企业代码' , '行业代码'
    ]]
   
    filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    dateTime = datetime.datetime.now().strftime('%Y%m')
    getPath(filePath)
    #公司财务清单列表
    financeAnalysisDubangFileName = 'financeAnalysisDubang' + str(dateTime)

    financeAnalysisDubangList = [] 
    companyUrlFileName = "companyUrl" + str(dateTime) + '.csv'
    financeAnalysisDubangUrlList =  readTableFromCsv(companyUrlFileName)
    print("********公司财务分析*******")
    print(financeAnalysisDubangUrlList)
    writeTableFromList(headers, 0, financeAnalysisDubangFileName)
    i = 0
    for lst in financeAnalysisDubangUrlList:
        try:
            a = HTMLDownload(lst[7])
            result = a.financeAnalysisDubang('.canvas_bgq_0 p', '#DBFX_Date_ul li:nth-child(1)',  '#DBFX_ul li:nth-child(1)',  52 , lst[40] , lst[0])
            result += a.financeAnalysisDubang('.canvas_bgq_1 p', '#DBFX_Date_ul li:nth-child(1)',  '#DBFX_ul li:nth-child(2)',  52 , lst[40] , lst[0])
            result += a.financeAnalysisDubang('.canvas_bgq_2 p', '#DBFX_Date_ul li:nth-child(1)',  '#DBFX_ul li:nth-child(3)',  52 , lst[40] , lst[0])
            result += a.financeAnalysisDubang('.canvas_bgq_3 p', '#DBFX_Date_ul li:nth-child(1)',  '#DBFX_ul li:nth-child(4)',  52 , lst[40] , lst[0])
            result += a.financeAnalysisDubang('.canvas_bgq_4 p', '#DBFX_Date_ul li:nth-child(1)',  '#DBFX_ul li:nth-child(5)',  52 , lst[40] , lst[0])
            result += a.financeAnalysisDubang('.canvas_nd_0 p', '#DBFX_Date_ul li:nth-child(2)',  '#DBFX_ul li:nth-child(10)',  52 , lst[40] , lst[0])
            result += a.financeAnalysisDubang('.canvas_nd_1 p', '#DBFX_Date_ul li:nth-child(2)',  '#DBFX_ul li:nth-child(11)',  52 , lst[40] , lst[0])
            result += a.financeAnalysisDubang('.canvas_nd_2 p', '#DBFX_Date_ul li:nth-child(2)',  '#DBFX_ul li:nth-child(12)',  52 , lst[40] , lst[0])
            result += a.financeAnalysisDubang('.canvas_nd_3 p', '#DBFX_Date_ul li:nth-child(2)',  '#DBFX_ul li:nth-child(13)',  52 , lst[40] , lst[0])
            result += a.financeAnalysisDubang('.canvas_nd_4 p', '#DBFX_Date_ul li:nth-child(2)',  '#DBFX_ul li:nth-child(14)',  52 , lst[40] , lst[0])
            i += 1
            writeTableFromList(result, i, financeAnalysisDubangFileName)
        except:
            print('执行出错继续***********')

# 公司财务分析(资产分析表)
def zcfzbBybgqImpl():
    headers = [[ '时间','流动资产','货币资金','以公允价值计量且其变动计入当期损益的金融资产',
        '应收票据及应收账款','其中:应收账款','预付款项','其他应收款合计','其中:应收利息',
        '应收股利', '其他应收款', '一年内到期的非流动资产', '其他流动资产', '流动资产合计',
        '非流动资产','可供出售金融资产','长期应收款', '长期股权投资', '投资性房地产',
        '固定资产', '无形资产', '长期待摊费用', '递延所得税资产', '其他非流动资产',
        '非流动资产合计', '资产总计', '流动负债' , '短期借款', '应付票据及应付账款',
        '其中:应付账款', '预收款项', '应付职工薪酬', '应交税费', '其他应付款合计', '其中:应付利息',
        '应付股利', '其他应付款', '一年内到期的非流动负债', '流动负债合计', '非流动负债', '长期借款',
        '递延所得税负债', '非流动负债合计', '负债合计', '所有者权益(或股东权益)', '实收资本（或股本)',
        '资本公积', '盈余公积', '未分配利润', '归属于母公司股东权益合计', '少数股东权益', '股东权益合计',
        '负债和股东权益合计', '行业代码', '公司代码'
    ]]
    filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    dateTime = datetime.datetime.now().strftime('%Y%m')
    getPath(filePath)

    zcfzbBybgqFileName = 'zcfzbBybgq' + str(dateTime)
    zcfzbBybgqList = [] 
    companyUrlFileName = "companyUrl" + str(dateTime) + '.csv'
    zcfzbBybgqUrlList =  readTableFromCsv(companyUrlFileName)
    print("********zcfzb*******")
    print(zcfzbBybgqUrlList)
    writeTableFromList(headers, 0, zcfzbBybgqFileName)
    i = 0
    for lst in zcfzbBybgqUrlList:
        try:
            a = HTMLDownload(lst[7])
            result = a.zcfzbBybgq('#report_zcfzb th ,#report_zcfzb td',6 , lst[40] , lst[0])
            i += 1
            writeTableFromList(result, i, zcfzbBybgqFileName)
        except:
            print('执行出错继续***********')

    return

# 公司财务分析(按年度分析)
def zcfzbByNdImpl():
    headers = [[ '时间','流动资产','货币资金','以公允价值计量且其变动计入当期损益的金融资产',
        '应收票据及应收账款','其中:应收账款','预付款项','其他应收款合计','其中:应收利息',
        '应收股利', '其他应收款', '一年内到期的非流动资产', '其他流动资产', '流动资产合计',
        '非流动资产','可供出售金融资产','长期应收款', '长期股权投资', '投资性房地产',
        '固定资产', '无形资产', '长期待摊费用', '递延所得税资产', '其他非流动资产',
        '非流动资产合计', '资产总计', '流动负债' , '短期借款', '应付票据及应付账款',
        '其中:应付账款', '预收款项', '应付职工薪酬', '应交税费', '其他应付款合计', '其中:应付利息',
        '应付股利', '其他应付款', '一年内到期的非流动负债', '流动负债合计', '非流动负债', '长期借款',
        '递延所得税负债', '非流动负债合计', '负债合计', '所有者权益(或股东权益)', '实收资本（或股本)',
        '资本公积', '盈余公积', '未分配利润', '归属于母公司股东权益合计', '少数股东权益', '股东权益合计',
        '负债和股东权益合计', '行业代码', '公司代码'
    ]]
    filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    dateTime = datetime.datetime.now().strftime('%Y%m')
    getPath(filePath)

    zcfzbByNdFileName = 'zcfzbByNd' + str(dateTime)
    zcfzbByNdList = [] 
    companyUrlFileName = "companyUrl" + str(dateTime) + '.csv'
    zcfzbByNdUrlList =  readTableFromCsv(companyUrlFileName)
    print("********zcfzb*******")
    print(zcfzbByNdUrlList)
    writeTableFromList(headers, 0, zcfzbByNdFileName)
    i = 0
    for lst in zcfzbByNdUrlList:
        try:
            a = HTMLDownload(lst[7])
            result = a.zcfzbByNd('#report_zcfzb th ,#report_zcfzb td',6 , lst[40] , lst[0])
            i += 1
            writeTableFromList(result, i, zcfzbByNdFileName)
        except:
            print('执行出错继续***********')

    return

# 理论按报告期
def lrbBybgqImpl():
    headers = [[ '时间','营业总收入','营业收入','营业总成本',
        '营业成本','营业税金及附加','管理费用','财务费用','资产减值损失',
        '其他经营收益', '加:公允价值变动收益', '投资收益', '其中:对联营企业和合营企业的投资收益', '营业利润',
        '加:营业外收入', '减:营业外支出', '利润总额', '减:所得税费用' , '净利润' , '其中:归属于母公司股东的净利润',
        '少数股东损益', '扣除非经常性损益后的净利润', '每股收益', '基本每股收益', '稀释每股收益', '其他综合收益',
        '归属于母公司股东的其他综合收益', '归属于少数股东的其他综合收益', '综合收益总额', '归属于母公司所有者的综合收益总额',
        '归属于少数股东的综合收益总额', '所属行业', '企业代码'
    ]]
    filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    dateTime = datetime.datetime.now().strftime('%Y%m')
    getPath(filePath)

    lrbBybgqFileName = 'lrbBybgq' + str(dateTime)
    lrbBybgqList = [] 
    companyUrlFileName = "companyUrl" + str(dateTime) + '.csv'
    lrbBybgqUrlList =  readTableFromCsv(companyUrlFileName)
    print("********zcfzb*******")
    print(lrbBybgqUrlList)
    writeTableFromList(headers, 0, lrbBybgqFileName)
    i = 0
    for lst in lrbBybgqUrlList:
        try:
            a = HTMLDownload(lst[7])
            result = a.lrbBybgq('#report_lrb th ,#report_lrb td',6 , lst[40] , lst[0])
            i += 1
            writeTableFromList(result, i, lrbBybgqFileName)
        except:
            print('执行出错继续***********')

    return

# 理论按年度
def lrbByndImpl():
    headers = [[ '时间','营业总收入','营业收入','营业总成本',
        '营业成本','营业税金及附加','管理费用','财务费用','资产减值损失',
        '其他经营收益', '加:公允价值变动收益', '投资收益', '其中:对联营企业和合营企业的投资收益', '营业利润',
        '加:营业外收入', '减:营业外支出', '利润总额', '减:所得税费用' , '净利润' , '其中:归属于母公司股东的净利润',
        '少数股东损益', '扣除非经常性损益后的净利润', '每股收益', '基本每股收益', '稀释每股收益', '其他综合收益',
        '归属于母公司股东的其他综合收益', '归属于少数股东的其他综合收益', '综合收益总额', '归属于母公司所有者的综合收益总额',
        '归属于少数股东的综合收益总额', '所属行业', '企业代码'
    ]]
    filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
    dateTime = datetime.datetime.now().strftime('%Y%m')
    getPath(filePath)

    lrbByndFileName = 'lrbBynd' + str(dateTime)
    lrbByndList = [] 
    companyUrlFileName = "companyUrl" + str(dateTime) + '.csv'
    lrbByndUrlList =  readTableFromCsv(companyUrlFileName)
    print("********zcfzb*******")
    print(lrbByndUrlList)
    writeTableFromList(headers, 0, lrbByndFileName)
    i = 0
    for lst in lrbByndUrlList:
        try:
            a = HTMLDownload(lst[7])
            result = a.lrbBynd('#report_lrb th ,#report_lrb td',6 , lst[40] , lst[0])
            i += 1
            writeTableFromList(result, i, lrbByndFileName)
        except:
            print('执行出错继续***********')

    return





if __name__ == "__main__":
    #industryBoardContent()
    #companyTotal()
    #print(companysItemImpl('http://data.eastmoney.com/bkzj/BK0738.html'))
    #companySurveyImpl()


    # a = HTMLDownload('http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code=sh600695')
    # print(a.companySurvey('#Table0', 1, 40))

    #companySurveyImpl()


    # 公司概况
    #companySurveyImpl()
    #businessAnalysisImpl()
    #financeAnalysisDubangImpl()
    #zcfzbBybgqImpl()
    #zcfzbByNdImpl()
    #lrbBybgqImpl()
    lrbByndImpl()


    

   
