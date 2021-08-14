import requests
from bs4 import BeautifulSoup


def check_standard():
    data = {}
    url = "https://www.kmu.ac.kr/uni/main/page.jsp?mnu_uid=143&"
    res = requests.get(url)
    xml = res.text
    n = 1

    soup = BeautifulSoup(xml, 'html.parser')
    datalist = soup.find('tbody').findAll('tr')
    for i in datalist:
        data[f"st_sub{n}"] = (i.find('td', class_='subject').text)
        data[f"st_href{n}"] = (i.find('td', class_='subject').find('a')["href"])
        data[f"st_wrt{n}"] = (i.find('td', class_='writer').text)
        data[f"st_date{n}"] = (i.find('td', class_='date').text)
        n = n+1
        if n is 10:
            break;
    return data

def check_academic():
    data = {}
    url = "https://www.kmu.ac.kr/uni/main/page.jsp?mnu_uid=144&"
    res = requests.get(url)
    xml = res.text
    n = 1

    soup = BeautifulSoup(xml, 'html.parser')
    datalist = soup.find('tbody').findAll('tr')
    for i in datalist:
        data[f"ac_sub{n}"] = (i.find('td', class_='subject').text)
        data[f"ac_href{n}"] = (i.find('td', class_='subject').find('a')["href"])
        data[f"ac_wrt{n}"] = (i.find('td', class_='writer').text)
        data[f"ac_date{n}"] = (i.find('td', class_='date').text)
        n = n+1
        if n is 10:
            break;
    return data

def check_award():
    data = {}
    url = "https://www.kmu.ac.kr/uni/main/page.jsp?mnu_uid=145&"
    res = requests.get(url)
    xml = res.text
    n = 1

    soup = BeautifulSoup(xml, 'html.parser')
    datalist = soup.find('tbody').findAll('tr')
    for i in datalist:
        data[f"aw_sub{n}"] = (i.find('td', class_='subject').text)
        data[f"aw_href{n}"] = (i.find('td', class_='subject').find('a')["href"])
        data[f"aw_wrt{n}"] = (i.find('td', class_='writer').text)
        data[f"aw_date{n}"] = (i.find('td', class_='date').text)
        n = n+1
        if n is 10:
            break;
    return data

def check_recruit():
    data = {}
    url = "https://www.kmu.ac.kr/uni/main/page.jsp?mnu_uid=147&"
    res = requests.get(url)
    xml = res.text
    n = 1

    soup = BeautifulSoup(xml, 'html.parser')
    datalist = soup.find('tbody').findAll('tr')
    for i in datalist:
        data[f"cr_sub{n}"] = (i.find('td', class_='subject').text)
        data[f"cr_href{n}"] = (i.find('td', class_='subject').find('a')["href"])
        data[f"cr_wrt{n}"] = (i.find('td', class_='writer').text)
        data[f"cr_date{n}"] = (i.find('td', class_='date').text)
        n = n+1
        if n is 10:
            break;
    return data

def check_job():
    data = {}
    url = "https://www.kmu.ac.kr/uni/main/page.jsp?mnu_uid=3445&"
    res = requests.get(url)
    xml = res.text
    n = 1

    soup = BeautifulSoup(xml, 'html.parser')
    datalist = soup.find('tbody').findAll('tr')
    for i in datalist:
        data[f"jo_sub{n}"] = (i.find('td', class_='subject').text)
        data[f"jo_href{n}"] = (i.find('td', class_='subject').find('a')["href"])
        data[f"jo_wrt{n}"] = (i.find('td', class_='writer').text)
        data[f"jo_date{n}"] = (i.find('td', class_='date').text)
        n = n+1
        if n is 10:
            break;
    return data

def check_nonsub():
    data = {}
    url = "https://story.kmu.ac.kr/user/Ep/EpMng010L.do?CURRENT_MENU_CODE=MENU0052&TOP_MENU_CODE=MENU0004&PRM_ORDER=2"
    res = requests.get(url)
    xml = res.text
    n = 1

    soup = BeautifulSoup(xml, 'html.parser')
    #datalist = soup.find('ul', class_="extra_card").findAll('li')
    # for i in datalist:
    #     data[f"non_title{n}"] = (i.find('div', class_="cardInfo").find('h4').text)
    #     data[f"non_date{n}"] = (i.find('div', class_="cardInfo").find('strong').text)
    #     data[f"non_mem{n}"] = (i.find('div', class_="cardInfo").find('em').text)
    #     n = n+1
    #     if n is 10:
    #         break;
    return data