import requests
import time
import datetime

url = 'http://cbseresults.nic.in/'
source_code_original = requests.get(url)
plain_text_original = source_code_original.text


def check_results(count=0):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    source_code = requests.get(url, headers=header)
    plain_text = source_code.text

    while plain_text == plain_text_original:
        source_code = requests.get(url)
        plain_text = source_code.text
        count += 1
        print('Number of times website checked: ' + str(count) + ' at ' + str(datetime.datetime.now().time()))
        time.sleep(10000.0 / 1000.0) # 10 seconds

    print('Results are out!')

check_results()
