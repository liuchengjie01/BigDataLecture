#!/usr/bin/python2.7.15
# -*- coding: utf-8 -*-
import sys

sys.path.append('/usr/local/lib/python2.7/dist-packages')
reload(sys)
sys.setdefaultencoding('utf8')
import csv
import happybase
import json
from itertools import islice

data_path = ''
#  北京 北京大学  喜欢  外交  好  差  成都  爱  疫情  讨厌  软微
data_topics = ['北京', '北京大学', '喜欢', '外交', '好', '差', '爱', '疫情', '讨厌']
# ip = "118.190.199.189"
ip = "47.102.205.73"
data = {
    'cf1:id': '',
    'cf1:bid': '',
    'cf1:user_id': '',
    'cf1:user_name': '',
    'cf1:content': '',
    # 微博中头条文章的url,可能为空
    'cf1:headline_url': '',
    'cf1:publish_place': '',
    'cf1:aite_user': '',
    'cf1:topic': '',
    'cf1:forward_num': '',
    'cf1:comment_num': '',
    'cf1:like_nums': '',
    'cf1:publish_time': '',
    'cf1:publish_tool': '',
    'cf1:pic_urls': '[]',
    'cf1:video_urls': '[]',
    'cf1:retweet_id': ''
}


def get_csv_path():
    path = "/home/hduser/workspace/weibo-search/结果文件/不/不.csv"
    return path


def list_to_dict(line):
    # 使用hbase数据的时候，需要取出来，然后json.loads一下
    if line[0] != '':
        data['cf1:id'] = json.dumps(line[0])
    if line[1] != '':
        data['cf1:bid'] = json.dumps(line[1])
    if line[2] != '':
        data['cf1:user_id'] = json.dumps(line[2])
    if line[3] != '':
        data['cf1:user_name'] = json.dumps(line[3])
    if line[4] != '':
        data['cf1:content'] = json.dumps(line[4])
    if line[5] != '':
        data['cf1:headline_url'] = json.dumps(line[5])
    if line[6] != '':
        data['cf1:publish_place'] = json.dumps(line[6])
    if line[7] != '':
        data['cf1:aite_user'] = json.dumps(line[7])
    if line[8] != '':
        data['cf1:topic'] = json.dumps(line[8])
    if line[9] != '':
        data['cf1:forward_num'] = json.dumps(line[9])
    if line[10] != '':
        data['cf1:comment_num'] = json.dumps(line[10])
    if line[11] != '':
        data['cf1:like_nums'] = json.dumps(line[11])
    if line[12] != '':
        data['cf1:publish_time'] = json.dumps(line[12])
    if line[13] != '':
        data['cf1:publish_tool'] = json.dumps(line[13])
    if line[14] != '':
        data['cf1:pic_urls'] = json.dumps(line[14])
    if line[15] != '':
        data['cf1:video_urls'] = json.dumps(line[15])
    if line[16] != '':
        data['cf1:retweet_id'] = json.dumps(line[16])


if __name__ == '__main__':
    # 1. 创建连接
    # 参数2类似命名空间
    # connection = happybase.Connection(ip, table_prefix='weibo')
    connection = happybase.Connection(ip)
    connection.open()
    table_name_list = connection.tables()
    table = connection.table("content")
    # 这里是创建的hbase表的结构
    # families = {
    #     # 列族
    #     "cf1": dict()
    # }
    # table = connection.create_table('content', families)

    # 1. 拿取csv的数据
    f = csv.reader(open(get_csv_path(), 'r'))
    # 跳过表头
    for line in islice(f,1,None):
        # 2. 将拿到的list转换为dict形式
        list_to_dict(line)
        for (key,value) in data.items():
            print("key=%s value=%s" % (key,value))
        try:
            table.put("2", data)
        except Exception as e:
            print("error:%s" % e)
        else:
            print("successful wirte")
        break

    # 如果插入数据的rowkey一样会怎样？后面的更新前面的
    # 插入数据必须是字符串
    # 可以一次性插入多个列
    # try:
    #     table.put("2", {"cf1:id": "888", "cf1:name": "hahah","cf1:url":"sdasdsad"})
    # except Exception as e:
    #     print("error:%s" % e)
    # else:
    #     print("successful wirte")
    row = table.row("2")
    print(row)

    # 3. 把数据写入HBase表格，HBase存储的数据是原始的字节字符串
    # id bid	user_id	用户昵称	微博正文	头条文章url	发布位置	艾特用户	话题	转发数	评论数	点赞数	发布时间	发布工具	微博图片url	微博视频url	retweet_id
    # for item in line:
    # 这里可以正确输入中文了
    # if item == '':
    #     print("this item is NULL")
    # else:
    #     print(item).decode('utf-8')
