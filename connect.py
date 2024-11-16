# 引入必要套件
import pymysql
# 設定資料庫連線資訊
host = 'localhost'
port = 3306
user = 'root'
passwd = 'password'
db = 'admin'
charset = 'utf8mb4'
# 建立連線
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
print('Successfully connected!')
# Successfully connected!
# 建立游標
cursor = conn.cursor()
# 關閉游標及連線
cursor.close()
conn.close()