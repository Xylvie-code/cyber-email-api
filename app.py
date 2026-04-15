from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app) 

@app.route('/send-report', methods=['POST'])
def send_report():
    data = request.json
    email = data['email']
    report = data['report']

    msg = MIMEText(report)
    msg['Subject'] = "Cybersecurity Report"
    msg['From'] = "xpxria7@gmail.com"
    msg['To'] = email

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("xpxria7@gmail.com", "owomnqjyydjjfbab")
    server.send_message(msg)
    server.quit()

    return jsonify({"status": "sent"})

app.run(host='0.0.0.0', port=5000)