#!/usr/bin/python2.7.15
# -*- coding: utf-8 -*-
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
reload(sys)
sys.setdefaultencoding('utf8')
import csv
import happybase
from typing import List

data_path = ''
#  北京 北京大学  喜欢  外交  好  差  成都  爱  疫情  讨厌  软微
data_topics = ['北京', '北京大学', '喜欢', '外交', '好', '差', '爱', '疫情', '讨厌']
data = {
        'cf1:id': '',
        'cf1:bid': '',
        'cf1:user_id': '',
        'cf1:user_name': '',
        'cf1:content': '',
        # 微博中头条文章的url,可能为空
        'cf1:article_url': '',
        'cf1:src_place': '',
        'cf1:aite_user': '',
        'cf1:topic': '',
        'cf1:forward_num': 0,
        'cf1:comment_num': 0,
        'cf1:like_nums': 0,
        'cf1:publish_time': '',
        'cf1:publish_tool': '',
        'cf1:pic_urls': [],
        'cf1:video_urls': [],
        'cf1:retweet_id': ''
    }

def get_csv_path():
    path = "/home/hduser/workspace/weibo-search/结果文件/北京大学/北京大学.csv"
    return path

def list_to_dict(line):
    if line[0] != '':
        data['cf1:id'] = line[0]
    if line[1] != '':
        data['cf1:id'] = line[1]
    if line[0] != '':
        data['cf1:id'] = line[0]
    if line[0] != '':
        data['cf1:id'] = line[0]
    if line[0] != '':
        data['cf1:id'] = line[0]
    if line[0] != '':
        data['cf1:id'] = line[0]
    if line[0] != '':
        data['cf1:id'] = line[0]
    if line[0] != '':
        data['cf1:id'] = line[0]


def create_table(name):
    # 1 创建连接
    # 参数2类似命名空间
    connection = happybase.Connection('ip', table_prefix='weibo')
    families = {
        # 列族
        "cf1": dict()
    }
    # name：表名
    # families：列族
    connection.create_table(name, families)


if __name__ == '__main__':

    # 1. 拿取csv的数据
    f = csv.reader(open(get_csv_path(), 'r'))
    for line in f:
        # 2. 将拿到的list转换为dict形式
        list_to_dict(line)
        # 3. 写入HBase
        # ['测试1', '软件测试工程师']
        # for item in line:
            # 这里可以正确输入中文了
            # if item == '':
            #     print("this item is NULL")
            # else:
            #     print(item).decode('utf-8')


    # 2. 创建表
    # create_table("weibo")

    # 3. 把数据写入HBase表格，HBase存储的数据是原始的字节字符串
    # id bid	user_id	用户昵称	微博正文	头条文章url	发布位置	艾特用户	话题	转发数	评论数	点赞数	发布时间	发布工具	微博图片url	微博视频url	retweet_id
    # 共17列
    data = {
        'cf1:id': '4577473620612120',
        'cf1:bid': 'Jwvrs2zeW',
        'cf1:user_id': '1547279851',
        'cf1:user_name': u'美丽大科普',
        'cf1:content': u'#深圳牙齿矫正#深圳牙齿矫正案例投稿：今天来复诊啦，之前爸爸妈妈也带我去看过牙，但那会儿还在上高中，我不想戴传统的牙套，又担心戴隐形牙套在学校护理上会不方便，就说等高考结束再去做正畸。我的医生是@深圳牙齿矫正蓝敬翔医生，毕业于北京大学口腔医学六年制本科和四川大学华西口腔医学院正畸硕士，这就是爸妈口中的别人家的孩子吧......我戴牙套有一个月啦，现在已经习惯了戴牙套，要说生活中的变化，那就是每天刷牙的次数变多了。初戴牙套的时候会有酸胀感，适应了就好了，每个人适应的时间不太一样。蓝医生很年轻帅气，就像个大哥哥，沟通起来很容易。知道我是个准大学生时还跟我聊了大学生活，让我好好学习多参加一些有用的活动，不要荒废了。面诊时他说他也戴着隐适美牙套，我都没看出来戴了牙套，当时就想着这样太好了，以后我戴牙套别人也看不出来~我做矫正是想改善牙齿不齐和嘴突的问题，蓝医生说这些问题都可以通过矫正解决，看了3D的演示动画，矫正后的效果挺让我期待的。蓝医生很砖业，因为自己也戴着隐适美牙套，平时有什么问题找他时他还会和我分享他戴牙套的经验和矫正的心得，灰常nice~#深圳隐适美#深圳矫正哪里做的好？深圳牙齿纠正技术？深圳龅牙牙齿纠正口腔医院？深圳那家地包天牙齿纠正医院好？深圳深覆合牙齿纠正大约价格？牙齿拥挤牙齿纠正深圳哪家好？都可以来问我，或者上爱优牙，找好牙医。联系@爱优牙隐适美牙齿矫正平台可以推荐全国的优秀正畸医生。',
        # 微博中头条文章的url,可能为空
        'cf1:article_url': '',
        'cf1:src_place': '',
        'cf1:aite_user': u'深圳牙齿矫正蓝敬翔医生,爱优牙隐适美牙齿矫正平台',
        'cf1:topic': u'深圳牙齿矫正,深圳隐适美',
        'cf1:forward_num': 0,
        'cf1:comment_num': 2,
        'cf1:like_nums': 1,
        'cf1:publish_time': '2020/12/1 23:56',
        'cf1:publish_tool': u'微博',
        'cf1:pic_urls': ['http://ww2.sinaimg.cn/large/5c399debgy1gl8soyv8ovj20j60ghmxx.jpg',
                         'http://ww4.sinaimg.cn/large/5c399debgy1gl8soyxpi0j20j60oj0vc.jpg',
                         'http://ww4.sinaimg.cn/large/5c399debgy1gl8soywnpgj20j60p0jsi.jpg',
                         'http://ww4.sinaimg.cn/large/5c399debgy1gl8soywz7vj20j60itjsq.jpg',
                         'http://ww3.sinaimg.cn/large/5c399debgy1gl8soywkz6j20j60cswfb.jpg',
                         'http://ww4.sinaimg.cn/large/5c399debgy1gl8soyy3nzj20j60e4js3.jpg',
                         'http://ww2.sinaimg.cn/large/5c399debgy1gl8soz0395j20j60cst98.jpg',
                         'http://ww4.sinaimg.cn/large/5c399debgy1gl8soz0ym2j20j60eeq41.jpg',
                         'http://ww4.sinaimg.cn/large/5c399debgy1gl8soz1vluj20j60pkmzd.jpg'],
        'cf1:video_urls': [],
        'cf1:retweet_id': ''
    }
