# source venv/bin/activate
from urllib import request

from flask import Flask, send_file, render_template, jsonify
import base64
app = Flask(__name__)

@app.route('/img')
def sendNotification():
	p = "notification.txt"
	return send_file(p,as_attachment=True)

@app.route("/getimg", method=["POST"])
def getImageFromMobile():
	json1 = request.get_json()
	s = json1['content']

	fh = open("imageToSave.png", "wb")
	fh.write(s.decode('base64'))
	fh.close()

	return jsonify(message="Done")
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5050, debug=True, threaded=True)