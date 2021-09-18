from flask import Flask, request, jsonify
from utils import connect_client, get_connected_clients, remove_connected_client

app = Flask(__name__)

app.config['SECRET_KEY']="some-secret"
app.config['DEFAULT_PARSERS'] = [
    'flask.ext.api.parsers.JSONParser'
]

@app.route("/add", methods=['POST'])
def add():
	device_ip = request.form.get("ip", None)
	device_name = request.form.get("platform", None)
	new_client = {"platform": device_name, "ip": device_ip}
	if device_name and device_ip:
		connect_client(new_client)
		print(get_connected_clients())
		return jsonify(new_client)
	else:	
		return {error: "Could not connect client, no valid platform"}

@app.route("/remove_client", methods=['POST'])
def remove_client():
	device_name = request.form.get("platform", None)
	if device_name:
		remove_connected_client(device_name)
		print(get_connected_clients())
		return jsonify({"platform": device_name})
	else:
		return {error: "Client does not exist"}

@app.route("/get")
def get_clients():
	clients = get_connected_clients()
	print(clients)
	return jsonify(clients)

if __name__ == "__main__":
	app.run(debug=True, host="192.168.43.14", port=4000)