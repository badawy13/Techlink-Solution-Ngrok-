from flask import Flask, jsonify
import time
import logging

app = Flask(__name__)

# منطق المحرك (مدمج داخل السيرفر)
def run_full_simulation():
    logging.info("بدء تنفيذ الأوامر على الأجهزة...")
    time.sleep(2)
    return "تم تطبيق الإعدادات بنجاح على جميع الراوترات."

@app.route('/run-simulation', methods=['POST'])
def handle_request():
    result = run_full_simulation()
    return jsonify({"status": "Success", "network_result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)