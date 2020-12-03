from datetime import datetime

import bs4
import pymysql
import requests


def get_conn():
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           database='python_study', charset='utf8',
                           user='root', password='xia4698083', autocommit=True)
    return conn


def write_to_db(url):
    # 获取数据库连接对象
    conn = get_conn()
    try:
        # 通过连接对象获取游标
        with conn.cursor() as cursor:
            # 通过游标执行sql并获取执行结果
            result = cursor.execute("insert into tb_explore (url, create_time) values (%s, %s)",
                                    (url, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            if result == 1:
                print('添加成功!')
            else:
                print('添加失败!')
            # 操作成功提交事务
            conn.commit()
    finally:
        conn.close()


def parse(base_url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/86.0.4240.198 Safari/537.36'
    response = requests.get(base_url, headers={'user-agent': user_agent})
    response.encoding = 'GBK'
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    tags = soup.select('#newhouse_loupai_list > ul > li')
    for item in tags:
        soup_li = bs4.BeautifulSoup(markup=str(item), features="lxml")
        details = soup_li.find_all('a')
        n = str.strip(details[1].text)
        print("楼盘:%s" % n)
        write_to_db(n)


def main():
    parse('https://wuhan.newhouse.fang.com/house/s/donghugaoxin1/b92')


if __name__ == '__main__':
    main()
