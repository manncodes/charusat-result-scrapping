import math
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import pandas as pd


driver = webdriver.Chrome()
resultlist = []

for i in range(1, 165):
    try:
        driver.get("http://117.239.83.200:2020/frmUniversityResult.aspx")
        e1 = Select(driver.find_element_by_id("ddlInst"))
        e1.select_by_value('21')
        e2 = Select(driver.find_element_by_id("ddlDegree"))
        e2.select_by_value('134')
        e3 = Select(driver.find_element_by_id("ddlSem"))
        e3.select_by_value('5')
        e4 = Select(driver.find_element_by_id("ddlScheduleExam"))
        e4.select_by_value('4917')
        ID = 'D19DCS' if i > 135 else '18DCS'
        for j in range(2-int(math.log10(i))):
            ID = ID + '0'
        ID = ID + str(i)
        element = driver.find_element_by_id("txtEnrNo")
        element.send_keys(ID)
        try:
            driver.find_element_by_id("btnSearch").click()
            doc = BeautifulSoup(driver.page_source, "html.parser")
            Name = doc.find('span', id='uclGrd1_lblStudentName')
            SGPA = doc.find('span', id='uclGrd1_lblSGPA')
            result = {}
            result['ID'] = ID
            result['name'] = Name.text
            result['SGPA'] = SGPA.text
            resultlist.append(result)
            print(result)
        except:
            pass
    except:
        pass


df = pd.DataFrame(resultlist)
df.to_csv('results.csv', index=False)
