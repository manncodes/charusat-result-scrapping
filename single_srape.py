import re
import math
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
resultlist = []

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
    ID = '18DCS074'
    # for j in range(2-int(math.log10(i))):
    #     ID = ID + '0'
    # ID = ID + str(i)
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
        table = doc.find('table',id = 'uclGrd1_grdResult')
        body_rows = table.find_all('tr')
        courseResult = []
        for row_num in range(1,len(body_rows)):
            course = []
            for row_item in body_rows[row_num].find_all("td"): 
                aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
                course.append(aa)
            courseResult.append(course)
        
        practicalFlag = 0
        courseList = []
        course={}
        for i in courseResult:
            if len(i) == 6 and practicalFlag == 0:
                course['CourseName'] = i[2]
                course['CourseID'] = i[1]
                course['TheoryGrade'] = i[-1]
                practicalFlag = 1
            if len(i) == 6 and practicalFlag == 1:
                course['PracticalGrade'] = i[-1]
                courseList.append(course)
                course = {}
                practicalFlag = 0
        result['Course Result'] = courseList
        resultlist.append(result)
    except:
        pass
except:
    pass

driver.quit()

df = pd.DataFrame(resultlist)
df.to_csv('results/results_single.csv', index=False)