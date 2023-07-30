import pymysql
from app import app
from config import mysql
from flask import jsonify


@app.route('/customer', methods=['GET'])
def list_customers():
     try:
          conn = mysql.connect()
          cursor = conn.cursor(pymysql.cursors.DictCursor)
          cursor.execute("SELECT id, name, phone_number, address FROM Customer")
          empRows = cursor.fetchall()
          respone = jsonify(empRows)
          respone.status_code = 200
          cursor.close() 
          conn.close()  
          return respone
     except Exception as e:
          respone = jsonify(str(e))
          respone.status_code = 400
          return respone
     
@app.route('/customer/get/<customer_id>' , methods=['GET'])
def get_customer(customer_id):
     try:
          conn = mysql.connect()
          cursor = conn.cursor(pymysql.cursors.DictCursor)
          cursor.execute("SELECT id, name, phone_number, address FROM Customer WHERE id =%s", customer_id)
          customer_obj = cursor.fetchone()
          if not customer_obj:
               return showMessage('Customer not found')
          respone = jsonify(customer_obj)
          respone.status_code = 200
          cursor.close() 
          conn.close() 
          return respone
     except Exception as e:
          print(e)