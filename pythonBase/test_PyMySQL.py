import pymysql
 
# 打开数据库连接
conn = pymysql.connect("120.76.232.203","viewer","Lz123321!#@$","scmbase",3306)
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
#创建一条sql语句
sql =  "select id,PN from phone_service_parts"
sql_update = "update phone_service_parts set PN222 = '02.01.2125718' where id = 87"

try:
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    rs = cursor.fetchmany(3)
    #print(rs) 
    for row in rs:
        print("id = %s, PN = %s" % row)
    cursor.execute(sql_update)
    conn.commit()  #提交事务
except Exception as e:
    print(e)
    conn.rollback()  #提交事务发生异常，回滚事务

#关闭cursor
cursor.close()

# 关闭数据库连接
conn.close()