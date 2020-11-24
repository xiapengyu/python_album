import requests
import json

# - `dump` - 将Python对象按照JSON格式序列化到文件中
# - `dumps` - 将Python对象处理成JSON格式的字符串
# - `load` - 将文件中的JSON数据反序列化成对象
# - `loads` - 将字符串的内容反序列化成Python对象


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    print(data_model)
    if 'newslist' in data_model.keys():
        for news in data_model['newslist']:
            print(news['title'])
    else:
        print('值不存在')


if __name__ == '__main__':
    main()
