# -*- coding: utf-8 -*-
# @Time    : 2018/1/25
# @Author  : whoiszxl
# @Site    : 
# @File    : import_taobaoCategory_to_ecmCategory.py
# @Software: PyCharm

import pymysql

# 需要填充的表名
table_name = 'ecm_gcategory'


# 0.创建连接，指定数据库的ip地址，账号、密码、端口号、要操作的数据库、字符集

# 本地测试环境
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='lamezhi_test', charset='utf8')

# 线上测试环境  测试库分类数据一共562条      线上正式环境一共561条
conn = pymysql.connect(host='118.89.23.125', port=3306, user='tenpercent', passwd='LaMeZhi@)17#EsCNgy&', db='tenpercent_test', charset='utf8')

# 创建游标
cursor = conn.cursor()

# 1.查询出表中的所有数据
cursor.execute("select sid,0,name,parent_sid,level,1,0,0 from y_category;")

# 2.获取所有数据
tb_categorys = cursor.fetchall()

# 将所有数据填充到ecm_gcategory中
effect_row = cursor.executemany(
    "insert into "+table_name+" (cate_id,store_id,cate_name,parent_id,sort_order,if_show,cate_logo,erp_sort) values (%s,%s,%s,%s,%s,%s,%s,%s); ",
    tb_categorys)

print(effect_row)

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
