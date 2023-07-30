import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import request

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

@app.route('/customer/create', methods=['POST'])
def create_customer():
     try:
          name = request.form['name']
     except:
          respone = jsonify({"message":"name is missing!"})
          respone.status_code = 400
          return respone
     try:
          phone_number = request.form['phone_number']
     except:
          respone = jsonify({"message":"phone_number is missing!"})
          respone.status_code = 400
          return respone
     try:
          address = request.form['address']
     except:
          respone = jsonify({"message":"address is missing!"})
          respone.status_code = 400
          return respone
     try:        
          conn = mysql.connect()
          cursor = conn.cursor(pymysql.cursors.DictCursor)		
          sqlQuery = "INSERT INTO Customer(name, phone_number, address) VALUES(%s, %s, %s)"
          bindData = (name, phone_number, address)            
          cursor.execute(sqlQuery, bindData)
          conn.commit()
          respone = jsonify('Customer added successfully!')
          respone.status_code = 200
          cursor.close() 
          conn.close()  
          return respone
     except Exception as e:
          print(e)
          return showMessage('name, phone_number, address are required')
     

@app.route('/customer/update', methods=['PUT'])
def update_customer():
     try:
          id = request.form['id']
     except:
          respone = jsonify({"message":"id is missing!"})
          respone.status_code = 400
          return respone
     try:
          name = request.form['name']
     except:
          respone = jsonify({"message":"name is missing!"})
          respone.status_code = 400
          return respone
     try:
          phone_number = request.form['phone_number']
     except:
          respone = jsonify({"message":"phone_number is missing!"})
          respone.status_code = 400
          return respone
     try:
          address = request.form['address']
     except:
          respone = jsonify({"message":"address is missing!"})
          respone.status_code = 400
          return respone
     try:        
          conn = mysql.connect()
          cursor = conn.cursor(pymysql.cursors.DictCursor)		
          sqlQuery = "UPDATE Customer SET name=%s, phone_number=%s, address=%s WHERE id=%s"
          bindData = (name,  phone_number, address, id,)            
          cursor.execute(sqlQuery, bindData)
          conn.commit()
          respone = jsonify('Customer updated successfully!')
          respone.status_code = 200
          cursor.close() 
          conn.close()  
          return respone
     except Exception as e:
          print(e)
          return showMessage('name, phone_number, address are required')
                


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 400,
        'message': error,
    }
    respone = jsonify(message)
    respone.status_code = 400
    return respone

if __name__ == "__main__":
    app.run()