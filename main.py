import pymysql
con = pymysql.connect(host='localhost',user='root',password='root',db='zuji',port=3306)    #连接建立好的数据库zuji
#参数分别是数据库的主机地址，用户名，密码，数据库名称，端口号
try:
    cursor = con.cursor()#游标
    print("demoColumn1", "demoColumn2")
    longitude = 4.4334
    dimension = 43.3434
    area_radius = 6.0
    sql = 'insert into gps_table(longitude,dimension,area_radius) values(%f,%f,%f)' % (longitude,dimension,area_radius)

    count = cursor.execute(sql)
    con.commit()

except Exception as e:
    raise e
