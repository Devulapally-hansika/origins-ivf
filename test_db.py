import mysql.connector

try:
    connection = mysql.connector.connect(
        host='origins-ivf-db.chmaic0ym2vl.ap-south-1.rds.amazonaws.com',
        user='admin',
        password='OriginsIVF123.', 
        port=3306
    )
    if connection.is_connected():
        print("SUCCESS! Connected to AWS RDS MySQL database!")
        connection.close()
except Exception as e:
    print(f"Error: {e}")
