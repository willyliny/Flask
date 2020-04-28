from flask import Flask, request, abort , jsonify
from flask_cors import CORS
from flask import render_template
import random
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})  
import sqlite3
import datetime


conn = sqlite3.connect('date.db')
cursor = conn.cursor()
try:
	cursor.execute("create table data (time text, temp text, h text)")
except:
	#print("已存在");
	pass

def insert(time , temp , h):
	conn = sqlite3.connect('date.db')
	cursor = conn.cursor()
	insert_cmd = "insert into data values ('{}','{}','{}')".format(time , temp  , h )
	cursor.execute(insert_cmd)
	conn.commit()
	
	
def get_t():
	conn = sqlite3.connect('date.db')
	cursor = conn.cursor()
	cursor.execute("select time,temp,h from data")
	m = {}
	
	items = cursor.fetchall()
	number = 50
	long = number if (len(items) >= number) else len(items)
	for item in items[ len(items) - long : len(items) ]:
		time = item[0]
		temp = item[1]
		h = item[2]
		m[ time ] = temp
		'''
		
	for item in cursor.fetchall():
		time = item[0]
		temp = item[1]
		h = item[2]
		m[ time ] = temp
	print(m)
	'''
	return m

@app.route('/page/<page_name>', methods=['GET'])
def liff_index(page_name):
	#index = request.args.get('page')
	openindex = "{0}".format(page_name)
	return render_template(openindex)


@app.route("/api/<function>", methods=['POST'])
def post_hander(function):
	if function == "set_led":
		data = request.get_json()
		print(data['led'] )
		return "OK"
	if function == "set_temp":
		data = request.get_json()
		insert( data['time'] , str(data['temp']) , str(data['h']) )
		print( data )
		return "OK"
	else:
		return jsonify(eventjson),200
		
@app.route("/api/<function>", methods=['GET'])
def get_hander(function):
	if function == "data":
		
		return jsonify(get_t()),200
	else:
		return 'ok'

	
import os
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='192.168.50.122', port=port , debug=True)
	