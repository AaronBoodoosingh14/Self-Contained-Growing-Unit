import os
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
FILE_NAME = "sensor_data.csv"

# 1. Updated Headers for Scaling
def initialize_file():
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            # Added Temp and Humidity columns
            f.write("Timestamp,Temp_C,Humidity_Pct,Raw_Duration_us,Distance_cm\n")
        print(f"Created new file: {FILE_NAME} with headers.")

@app.route('/update-sensor', methods=['POST'])
def update_sensor():
    # 2. Get JSON data from the request
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid JSON or Content-Type"}), 400

    try:
        # 3. Extract values using keys (matches your ESP32 code)
        # Using .get(key, default) prevents crashes if a sensor fails
        temp = data.get('temp', 0)
        hum = data.get('hum', 0)
        duration_us = float(data.get('dist', 0))
        
        # Calculate distance
        dist_cm = duration_us / 58.0
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 4. Append the expanded data to CSV
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{timestamp},{temp},{hum},{duration_us},{dist_cm:.2f}\n")
        
        print(f"[{timestamp}] Saved -> Temp: {temp}C | Hum: {hum}% | Dist: {dist_cm:.2f}cm")
        
        return jsonify({"status": "success", "received": data}), 200
        
    except Exception as e:
        print(f"Error processing data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    initialize_file()
    # Host 0.0.0.0 allows any device on your Wi-Fi to reach the server
    app.run(host='0.0.0.0', port=5000, debug=True)