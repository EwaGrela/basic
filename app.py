from flask import Flask, request
from user_agents import parse 
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World"

@app.route("/now")
def now():
	return datetime.datetime.utcnow().strftime("%Y-%m-%d, %H:%M:%S.%f")

@app.route("/user-agent")
def user_agent():
	return str(parse(request.user_agent.string))

@app.route("/request")
def request_info():
	return f'Request method: {request.method} url: {request.url} Headers: {request.headers}'

@app.route("/counter")
def counter():
	with open("count.txt", "r") as f:
		count = f.read()
		count = int(count)
	with open("count.txt", "w") as g:
		g.write(str(count+1))
	return str(count)



#this line should always stay at the bottom of the code
if __name__ == '__main__':
	app.run(debug=True)