import requests
from bs4 import BeautifulSoup


with requests.Session() as s:
    req = s.get('http://localhost:5501/simple_web_crawler/part_1/index.html')


    html = req.text
    header = req.headers
    status = req.status_code
    is_ok = req.ok

    soup = BeautifulSoup(html, 'html.parser')
    result = soup.select("body > p")
    breakpoint()
    print("end")
    https://www.google.com/search?q=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&client=safari&rls=en&biw=1792&bih=893&tbm=nws&ei=BCiFYMKgEY29mAWUv4moDA&oq=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&gs_l=psy-ab.3...3672.4059.0.4718.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.o0g3lqn4npw