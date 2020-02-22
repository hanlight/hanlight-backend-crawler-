from django.core.management.base import BaseCommand, CommandError
import time, re, datetime, os
from selenium import webdriver
#import sys
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from crawler.models.calendar import CalenderModel

class Command(BaseCommand):

    def handle(self, *args, **options):

        # 현재년도
        year = datetime.datetime.now().year

        # 정규식
        pattern = re.compile('\d+')

        # User Agent 설정
        #options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

        options = webdriver.ChromeOptions() #브라우저가 열리지 않게 헤드리스로 작동하게끔 해주는 코드.
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        # driver 인스턴스 생성
        driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver'), options=options)

        #driver = webdriver.Chrome('./chromedriver.exe')
        #driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

        url = "https://stu.sen.go.kr/edusys.jsp?page=sts_m42220"

        # 나이스 접속
        driver.get(url)
        time.sleep(3)

        # 교육청 선택
        driver.find_element_by_xpath('''//*[@id="selContEducation"]/option[2]''').click()
        # 이동 버튼 클릭
        driver.find_element_by_xpath('''//*[@id="btnMove"]''').click()
        time.sleep(2)

        # 학교 검색하기
        driver.find_element_by_xpath('''//*[@id="btnSearchSchool"]''').click()
        # 학교 검색 창으로 포커스 전환
        driver.switch_to.window(driver.window_handles[1])
        # 한세사이버보안고등학교 입력
        driver.find_element_by_id("edInfoNam").send_keys("한세사이버보안고등학교")
        # 검색버튼 클릭
        driver.find_element_by_xpath('''//*[@id="btnSearch"]''').click()
        time.sleep(1)
        # 검색결과 클릭
        driver.find_element_by_xpath('''//*[@id="grdSchoolList_cell_0_0"]/nobr/a''').click()
        # 원래 창으로 포커스 전환
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

        #연도 테스트용
        #select_box2 = driver.find_element_by_id("selAy")
        #select_options2 = [options for options in select_box2.find_elements_by_tag_name('option')]
        #options1 = select_options2[0]
        #options1.click()
        #time.sleep(2)

        # select 박스 선택
        select_box = driver.find_element_by_id("selMm")

        # 월별 options 가져오기
        select_options = [options for options in select_box.find_elements_by_tag_name('option')]

        # 월별 조회
        for options in select_options:
            # 월 저장
            month = options.text
            month = pattern.findall(month)[0]
            month = int(month)
            if month == 1:
                year += 1
            # 각 월 선택
            options.click()
            # 조회
            driver.find_element_by_xpath('''//*[@id="btnSearch"]''').click()
            time.sleep(2)

            # 일정 모두 선택
            days = driver.find_elements_by_css_selector('tbody#genCalendarWeb > tr.w2group  > td.w2group.w2tb_td.verT.w2tb_noTH')

            for day in days:
                try:
                    # 날짜 가져오기
                    date = day.find_element_by_css_selector('div.textL').text
                    date = int(date)
                    # 일정 가져오기
                    detail = day.find_elements_by_css_selector('div > a.textL')
                    if detail:
                        detail = ','.join([x.text for x in detail])
                    else:
                        continue
                except:
                    continue

                # Calender 레코드 생성 및 저장
                CalenderModel(year = year, month = month, date = date, detail = detail).save()
                # Todo: db.session.flush를 사용하여 bulk_create 로직 구성

        driver.close()
