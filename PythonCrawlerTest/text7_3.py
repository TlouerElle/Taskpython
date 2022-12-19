import requests
from bs4 import BeautifulSoup
import pymysql


def download_html(url):
    response = requests.get(url)
    state = response.status_code
    if state == 200:
        html = response.text
        return html
    else:
        return state


def parser_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def main_html(soup):
    data = soup.find_all('a')
    city = data[6].string.strip()
    temperature = data[10].string.strip()
    weather = data[11].string.strip()
    airquality = data[13].string.strip()
    TemperaturSection = data[15].string.strip()
    StravioletRays = data[17].string.strip()
    humidity = data[19].string.strip()
    print(city, temperature, weather, airquality, TemperaturSection, StravioletRays, humidity)


def crawler_message(soup):
    data = soup.find_all('a')
    urls = set()
    for i in data:
        try:
            if '1d' in i.get('href'):
                url = 'https://tianqi.2345.com/' + i.get('href')
                if url not in urls:
                    urls.add(url)
        except Exception:
            pass
    try:
        for url in urls:
            html = download_html(url)
            soup = parser_html(html)
            data = soup.find_all('span')
            city = data[4].string
            temperature = data[8].string
            airquality = data[9].string
            todaysituation = data[10].string
            yessituation = data[11].string
            wind = data[12].text
            humidity = data[13].text
            StravioletRays = data[14].text
            pressure = data[15].text
            print(city, temperature, airquality, todaysituation, yessituation, wind, humidity, StravioletRays, pressure)
            sql = "INSERT weather(city, temperature, airquality, todaysituation, yessituation, wind, humidity, " \
                  "StravioletRays, pressure) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            connect(sql,(city, temperature, airquality, todaysituation, yessituation, wind, humidity, StravioletRays, pressure))
    except Exception as er:
        print(er)

def connect(sql, data):
    conn = pymysql.connect(host='159.75.52.80', user='root', password='bigdata2019', database='db_WeiEnsong', port=3306)
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    url = 'https://tianqi.2345.com/'
    html = download_html(url)
    soup = parser_html(html)
    main_html(soup)
    crawler_message(soup)
