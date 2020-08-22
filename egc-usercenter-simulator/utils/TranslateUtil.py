import json
import requests


def translate(word):
    post_url = 'http://fanyi.youdao.com/translate'
    data = {'doctype': 'json', 'i': words}
    response = requests.post(url=post_url, data=data)
    html = response.content.decode('utf-8')
    return json.loads(html)['translateResult'][0][0]['tgt']


if __name__ == '__main__':
    words = input('请输入要翻译的文字:')
    translate(words)
