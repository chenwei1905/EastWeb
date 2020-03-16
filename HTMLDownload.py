
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import re
import numpy as np
from selenium.webdriver.support.wait import WebDriverWait


class HTMLDownload(object):

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--headless')

    chrome_driver = r"C:\Python27\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
  # driver=webdriver.Chrome(executable_path=chrome_driver) ceshi11
    browser = webdriver.Chrome(
    executable_path=chrome_driver, chrome_options=chrome_options)

    def __init__(self, url):
        self.url = url

    def getPageDiv(self, div):
        self.browser.get(self.url)
        element = self.browser.find_element_by_css_selector(div)  # 定位表格
        td_content = element.find_elements_by_tag_name(
            'td')  # 进一步定位到表格内容所在的td节点
        lst = []
        for td in td_content:
            lst.append(td.text)
        return lst
    # 行业总汇数据
    def indexPage(self, div, index, column, inputText, checkBox):
        self.browser.get(self.url)
        # 输入框输入值然后跳转
        # input = self.browser.find_element_by_css_selector('.paginate_input')
        if (len(inputText) > 0):
            input = self.browser.find_element_by_css_selector(inputText)
            input.clear() #清除输入框
            input.send_keys(index)

            self.browser.find_element_by_css_selector(checkBox).click()

            #self.browser.find_element_by_css_selector('.paginte_go').click()

            wait = WebDriverWait(self.browser, 10)
        # wait.until(EC.presence_of_element_located((By.ID, div)))

        #self.browser.refresh()
            time.sleep(10)
        element = self.browser.find_element_by_css_selector(div)  # 定位表格

        td_content = element.find_elements_by_tag_name(
            'td')  # 进一步定位到表格内容所在的td节点
        lst = []
        for td in td_content:
            lst.append(td.text)
        
        lst  =  [lst[i:i + column] for i in range(0, len(lst), column)]
        return lst
    
    # 对应行业的数据
    def href(self, div, index):
        self.browser.get(self.url)
        # 输入框输入值然后跳转
        input = self.browser.find_element_by_css_selector('.paginate_input')
        input.clear() #清除输入框
        input.send_keys(index)

        self.browser.find_element_by_css_selector('.paginte_go').click()

        wait = WebDriverWait(self.browser, 10)
        # wait.until(EC.presence_of_element_located((By.ID, div)))

        #self.browser.refresh()
        time.sleep(10)
       
        element = self.browser.find_element_by_css_selector(div)  # 定位表格
         
        td_content = element.find_elements_by_css_selector(
            div + ' .mywidth3 a')
        # 进一步定位到表格内容所在的td节点td
        lst = []
        for td in td_content:
            url = td.get_attribute('href') # http://quote.eastmoney.com/unify/r/90.BK0447 转化为 http://data.eastmoney.com/bkzj/BK0447.html
            url = 'http://data.eastmoney.com/bkzj/' + url[-6:] + '.html'
            text = td.text 
            lst.append(text)
            lst.append(url)
        lst  =  [lst[i:i + 4] for i in range(0, len(lst), 4)]
        
        
        
        return lst

    # 对应公司列表 
    def companysItem(self, div, column, foreignKey):
        self.browser.get(self.url)
        pageLen = len(self.pageTran()) # 表格翻页长度
        lstContent = [] # 存储基本类容
        
        element = self.browser.find_element_by_css_selector(div)  # 定位表格

        td_content = element.find_elements_by_tag_name(
            'td')  # 进一步定位到表格内容所在的td节点
        
       
        for td in td_content:
            lstContent.append(td.text)
        if (pageLen > 0):
            pageTotalNum = self.pageTran()[-3]
            for i in range(2, int(pageTotalNum)+1):
                #获取输入框并且跳转
                input = self.browser.find_element_by_css_selector('#PageContgopage')
                input.clear() #清除输入框
                input.send_keys(i)
                self.browser.find_element_by_css_selector('.btn_link').click()
                wait = WebDriverWait(self.browser, 5)
                time.sleep(5)
                element = self.browser.find_element_by_css_selector(div)
                td_content = element.find_elements_by_tag_name('td')  # 
                for td in td_content:
                    lstContent.append(td.text)
        lstContent = [lstContent[i:i + column] for i in range(0, len(lstContent), column)]
        for i in range(0,len(lstContent)):
            lstContent[i].append(foreignKey)

        return lstContent
    
    # 对应公司连接url
    def companysHref(self, div,  column, foreignKey):
        self.browser.get(self.url)
        pageLen = len(self.pageTran()) # 表格翻页长度
        element = self.browser.find_element_by_css_selector(div)  # 定位表格
        lstContent = [] # 存储基本类容
        td_content = element.find_elements_by_tag_name(
            'td')  # 进一步定位到表格内容所在的td节点
        td_content = element.find_elements_by_css_selector(
            div + ' a')
        
        
        for td in td_content:
            url = td.get_attribute('href') 
            text = td.text
            lstContent.append(text)
            lstContent.append(url)
            # 匹配上海的股票 60 90 开头
            matchSh = r"^[60|90].*"
            matchSz = r"^[00|20|30].*"
            if re.findall(matchSh, text):
                code = 'sh'
            if re.findall(matchSz,text):
                code = 'sz'
            # 匹配深圳的股票 00 20 30 开头
            lstContent.append('公司概况')
            urlCompanySurvey = 'http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code=' + code + text
            lstContent.append(urlCompanySurvey)
            lstContent.append('经营分析')
            urlBusinessAnalysis = 'http://f10.eastmoney.com/f10_v2/BusinessAnalysis.aspx?code=' + code + text
            lstContent.append(urlBusinessAnalysis)
            lstContent.append('财务分析')
            urlFinanceAnalysis = 'http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=' + code + text
            lstContent.append(urlFinanceAnalysis)
        if (pageLen > 0):
            pageTotalNum = self.pageTran()[-3]
            for i in range(2, int(pageTotalNum)+1):
                input = self.browser.find_element_by_css_selector('#PageContgopage')
                input.clear() #清除输入框
                input.send_keys(i)
                self.browser.find_element_by_css_selector('.btn_link').click()
                wait = WebDriverWait(self.browser, 5)
                time.sleep(5)
                element = self.browser.find_element_by_css_selector(div)  # 定位表格
                td_content = element.find_elements_by_tag_name('td')  # 进一步定位到表格内容所在的td节点
                td_content = element.find_elements_by_css_selector(div + ' a')
                for td in td_content:
                    url = td.get_attribute('href') #
                    text = td.text
                    lstContent.append(text)
                    lstContent.append(url)
                    # 匹配上海的股票 60 90 开头
                    matchSh = r"^[60|90].*"
                    matchSz = r"^[00|20|30].*"
                    if re.findall(matchSh, text):
                        code = 'sh'
                    if re.findall(matchSz,text):
                        code = 'sz'
                    # 匹配深圳的股票 00 20 30 开头
                    lstContent.append('公司概况')
                    urlCompanySurvey = 'http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code=' + code + text
                    lstContent.append(urlCompanySurvey)
                    lstContent.append('经营分析')
                    urlBusinessAnalysis = 'http://f10.eastmoney.com/f10_v2/BusinessAnalysis.aspx?code=' + code + text
                    lstContent.append(urlBusinessAnalysis)
                    lstContent.append('财务分析')
                    urlFinanceAnalysis = 'http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=' + code + text
                    lstContent.append(urlFinanceAnalysis)
                

        
        lstContent = [lstContent[i:i + column] for i in range(0, len(lstContent), column)]
        for i in range(0,len(lstContent)):
            lstContent[i].append(foreignKey)

        return lstContent

    # 公司概况
    def companySurvey(self, div, column, foreignKey):
        self.browser.get(self.url)
        
        element = self.browser.find_element_by_css_selector(div)  # 定位表格

        td_content = element.find_elements_by_tag_name(
            'td')  # 进一步定位到表格内容所在的td节点
        #wait = WebDriverWait(self.browser, 2)
        # wait.until(EC.presence_of_element_located((By.ID, div)))

        #self.browser.refresh()
        #time.sleep(2)
        lstContent = [] # 存储基本类容
        for td in td_content:
            lstContent.append(td.text)
        
        lstContent = [lstContent[i:i + column] for i in range(0, len(lstContent), column)]
        for i in range(0,len(lstContent)):
            lstContent[i].append(foreignKey)
        return lstContent

    # 经营分析
    def businessAnalysis(self, div, column, foreignKey, foreignKey2): 
        self.browser.get(self.url)
        
        td_content = self.browser.find_elements_by_css_selector(div)  # 定位表格

        # td_content = element.find_elements_by_tag_name(
        #     'td')  # 进一步定位到表格内容所在的td节点
        
        lstContent = [] # 存储基本类容
        for td in td_content:
            lstContent.append(td.text)
        
        lstContent = [lstContent[i:i + column] for i in range(0, len(lstContent), column)]
        for i in range(0,len(lstContent)):
            lstContent[i].append(foreignKey)
            lstContent[i].append(foreignKey2)
        
        timeLable = ""
        fenleiLable = ""
        matchData = r"(\d{4}-\d{1,2}-\d{1,2})"
        moneyMatch =  r"(\d*.\d*亿)"
        # 提取日期到最后一列
        # 保存结果
        resultContent = []
        for i in range(0,len(lstContent)):
            # print("*******第%d ********" % i)
            # print(lstContent[i][0])
            if re.findall(matchData, lstContent[i][0]):
                timeLable = lstContent[i][0]
            elif lstContent[i][0] != '':              
                fenleiLable = lstContent[i][0]
                if re.findall(moneyMatch,lstContent[i][2]):
                    lstContent[i][2] = str(float(lstContent[i][2][:-1])*10000) + '万'
                if re.findall(moneyMatch,lstContent[i][4]):
                    lstContent[i][4] = str(float(lstContent[i][4][:-1])*10000) + '万'
                if re.findall(moneyMatch,lstContent[i][6]):
                    lstContent[i][6] = str(float(lstContent[i][6][:-1])*10000) + '万'
                lstContent[i].append(timeLable)
                resultContent.append(lstContent[i])
            else:               
                lstContent[i][0] = fenleiLable
                lstContent[i].append(timeLable)
                resultContent.append(lstContent[i])
        # 在进行字段处理(按行业分添加到下面和钱单位转化为万以及过滤掉表头)
    
        return resultContent

    # 公司财务分析(杜邦分析 按报告期)
    def financeAnalysisDubang(self, tableDiv, label, li, column, foreignKey, foreignKey2):
        element = self.browser.get(self.url)
        label0 = self.browser.find_element_by_css_selector(label) # '#DBFX_Date_ul li:nth-child(1)'
        # li0 = self.browser.find_element_by_css_selector('#DBFX_ul li:nth-child(1)')  # 定位表格
        # tb0 = self.browser.find_elements_by_css_selector('.canvas_bgq_0 p')  # 定位表格
        labelClick0 = self.browser.find_element_by_css_selector(label).click()
        # wait = WebDriverWait(self.browser, 10)
        # time.sleep(10)
        li1 = self.browser.find_element_by_css_selector(li) # '#DBFX_ul li:nth-child(2)'
        liClick1 = self.browser.find_element_by_css_selector(li).click() # '#DBFX_ul li:nth-child(2)'
        wait = WebDriverWait(self.browser, 2)
        time.sleep(2)
        tb1 = self.browser.find_elements_by_css_selector(tableDiv)  # 定位表格 '.canvas_bgq_1 p'


        # tb2 = self.browser.find_elements_by_css_selector('.canvas_bgq_2 p')
        # tb3 = self.browser.find_elements_by_css_selector('.canvas_bgq_3 p')
        # tb4 = self.browser.find_elements_by_css_selector('.canvas_bgq_4 p')

        #td_content = [header[0]] + tb0 +  [header[1]]  + tb1 +  [header[2]]  + tb2 +  [header[3]]  +  tb3  +  [header[4]] +  tb4
        #tb1 = self.browser.find
        td_content = [label0] + [li1] + tb1
        # td_content = element.find_elements_by_tag_name(
        #     'p')  # 进一步定位到表格内容所在的p节点
        
        lstContent = [] # 存储基本类容
        moneyMatch =  r"(\d*.\d*亿)"
        for td in td_content:
            tempText = ''
            if re.findall(moneyMatch, td.text):
                tempText = str(float(td.text[:-1])*10000) + '万'
                lstContent.append(tempText)
            else:
                lstContent.append(td.text)
        
        lstContent = [lstContent[i:i + column] for i in range(0, len(lstContent), column)]
        for i in range(0,len(lstContent)):
            lstContent[i].append(foreignKey)
            lstContent[i].append(foreignKey2)
        return lstContent
    # 利润表按报告期
    def lrbBybgq(self, div, column, foreignKey, foreignKey2):
        self.browser.get(self.url)
        td_content = self.browser.find_elements_by_css_selector(div)  # 定位表格

        # td_content = element.find_elements_by_tag_name(
        #     'p')  # 进一步定位到表格内容所在的p节点
        
        lstContent = [] # 存储基本类容
        moneyMatch =  r"(\d*.\d*亿)"
        for td in td_content:
            tempText = ''
            if re.findall(moneyMatch, td.text):
                tempText = str(float(td.text[:-1])*10000) + '万'
                lstContent.append(tempText)
            else:
                lstContent.append(td.text)
        
        lstContent = [lstContent[i:i + column] for i in range(0, len(lstContent), column)]

        resultContent = []
        # 转置
        for i in range(0,len(lstContent)):
            #lstContent[i].append(foreignKey)
            if lstContent[i][0] != '':
                resultContent.append(lstContent[i])
        resultContent = np.transpose(resultContent).tolist()
        # 过滤
        for i in range(0,len(resultContent)):
            resultContent[i].append(foreignKey)
            resultContent[i].append(foreignKey2)
        return resultContent[1:]
    def lrbBynd(self, div, column, foreignKey, foreignKey2):
        self.browser.get(self.url)
        # self.browser.find_element_by_css_selector(checkBox).click()
        self.browser.find_element_by_css_selector('#lrb_ul li:nth-child(2)').click()
        wait = WebDriverWait(self.browser, 2)
        time.sleep(2)
        td_content = self.browser.find_elements_by_css_selector(div)  # 定位表格

        # td_content = element.find_elements_by_tag_name(
        #     'p')  # 进一步定位到表格内容所在的p节点
        
        lstContent = [] # 存储基本类容
        moneyMatch =  r"(\d*.\d*亿)"
        for td in td_content:
            tempText = ''
            if re.findall(moneyMatch, td.text):
                tempText = str(float(td.text[:-1])*10000) + '万'
                lstContent.append(tempText)
            else:
                lstContent.append(td.text)
        
        lstContent = [lstContent[i:i + column] for i in range(0, len(lstContent), column)]

        resultContent = []
        # 转置
        for i in range(0,len(lstContent)):
            #lstContent[i].append(foreignKey)
            if lstContent[i][0] != '':
                resultContent.append(lstContent[i])
        resultContent = np.transpose(resultContent).tolist()
        # 过滤
        for i in range(0,len(resultContent)):
            resultContent[i].append(foreignKey)
            resultContent[i].append(foreignKey2)
        return resultContent[1:]
    
    # 资产负债表 按照报告期
    def zcfzbBybgq(self, div, column, foreignKey, foreignKey2):
        self.browser.get(self.url)
        td_content = self.browser.find_elements_by_css_selector(div)  # 定位表格

        # td_content = element.find_elements_by_tag_name(
        #     'p')  # 进一步定位到表格内容所在的p节点
        
        lstContent = [] # 存储基本类容
        moneyMatch =  r"(\d*.\d*亿)"
        for td in td_content:
            tempText = ''
            if re.findall(moneyMatch, td.text):
                tempText = str(float(td.text[:-1])*10000) + '万'
                lstContent.append(tempText)
            else:
                lstContent.append(td.text)
        
        lstContent = [lstContent[i:i + column] for i in range(0, len(lstContent), column)]
        resultContent = []
        # 转置
        for i in range(0,len(lstContent)):
            #lstContent[i].append(foreignKey)
            if lstContent[i][0] != '':
                resultContent.append(lstContent[i])
        resultContent = np.transpose(resultContent).tolist()
        # 过滤
        for i in range(0,len(resultContent)):
            resultContent[i].append(foreignKey)
            resultContent[i].append(foreignKey2)
        return resultContent[1:]
    
    # 资产负载表 年度
    def zcfzbByNd(self, div, column, foreignKey,foreignKey2 ):
        self.browser.get(self.url)
        # self.browser.find_element_by_css_selector(checkBox).click()
        self.browser.find_element_by_css_selector('#zcfzb_ul li:nth-child(2)').click()
        wait = WebDriverWait(self.browser, 2)
        time.sleep(2)
        td_content = self.browser.find_elements_by_css_selector(div)  # 定位表格

        # td_content = element.find_elements_by_tag_name(
        #     'p')  # 进一步定位到表格内容所在的p节点
        
        lstContent = [] # 存储基本类容
        moneyMatch =  r"(\d*.\d*亿)"
        for td in td_content:
            tempText = ''
            if re.findall(moneyMatch, td.text):
                tempText = str(float(td.text[:-1])*10000) + '万'
                lstContent.append(tempText)
            else:
                lstContent.append(td.text)
        
        lstContent = [lstContent[i:i + column] for i in range(0, len(lstContent), column)]
        resultContent = []
        # 转置
        for i in range(0,len(lstContent)):
            #lstContent[i].append(foreignKey)
            if lstContent[i][0] != '':
                resultContent.append(lstContent[i])
        resultContent = np.transpose(resultContent).tolist()
        # 过滤
        for i in range(0,len(resultContent)):
            resultContent[i].append(foreignKey)
            resultContent[i].append(foreignKey2)
        return resultContent[1:]
    


    # 翻页测试获取公司分类
    def pageTran(self):
        self.browser.get(self.url)
        element = self.browser.find_element_by_css_selector('#PageCont')  # 定位表格
        td_content = element.find_elements_by_css_selector('a') # 获取a标签
        lst = []
        
        for td in td_content:
             lst.append(td.text)
        print(lst)
        return lst

        
        
if __name__ == "__main__":
   

    # a = HTMLDownload('http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=sh600423')
    # print(a.financeAnalysisDubang('.canvas_nd_0', 1, 2))

    # a = HTMLDownload('http://data.eastmoney.com/bkzj/BK0910.html')
    # print(a.companysHref('#dt_1', 40, "hh"))

    # a = HTMLDownload('http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code=sh600695')
    # print(a.companySurvey('#Table0', 40, 'test'))

    # a = HTMLDownload('http://f10.eastmoney.com/f10_v2/BusinessAnalysis.aspx?code=sh600695')
    # print(a.businessAnalysis('tr > .tips-dataL, tr > .tips-fieldnameL', 9, 'test'))

    # a = HTMLDownload('http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=sh600695')
    # print(a.financeAnalysisDubang('.canvas_bgq_0 p', 40 ,'Testing'))


    #利润表测试
    #  a = HTMLDownload('http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=sh600695')
    #  print(a.lrb('#report_lrb th, #report_lrb td',6, '测试'))

    # a = HTMLDownload('http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=sh600695')
    # #print(a.lrbBynd('#report_lrb td ,#report_lrb td',6, '测试'))

    # print(a.zcfzbByNd('#report_zcfzb th ,#report_zcfzb td',6, '测试'))

    #公司经营分析
    # a = HTMLDownload('http://f10.eastmoney.com/f10_v2/BusinessAnalysis.aspx?code=sh600695')
    # print(a.businessAnalysis('tr > .tips-dataL, tr > .tips-fieldnameL', 9, 'Test1' , 'Test1'))
    
    a = HTMLDownload('http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=sh600695')
    #print(a.financeAnalysisDubang('.canvas_bgq_0 p', '#DBFX_Date_ul li:nth-child(1)', '#DBFX_ul li:nth-child(1)',52, 'test', 'test'))
    #print(a.financeAnalysisDubang('.canvas_nd_0 p', '#DBFX_Date_ul li:nth-child(2)', '#DBFX_ul li:nth-child(10)',52, 'test', 'test'))
    print(a.lrbBynd('#report_lrb th ,#report_lrb td',6, '测试', 'tt'))










   




   