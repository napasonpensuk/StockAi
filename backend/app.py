from flask import Flask, request, jsonify, render_template
from model import predict_stock  # Import prediction function from model.py
import pandas as pd
import yfinance as yf  # ใช้ yfinance เพื่อดึงข้อมูลหุ้น
from datetime import datetime, timedelta  # สำหรับจัดการวันที่

app = Flask(__name__)

# Function to get stock data from yfinance for the past 2 months
def get_stock_data(symbol):
    # กำหนดช่วงเวลา 2 เดือนก่อนหน้า
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=60)
    
    # ดึงข้อมูลจาก yfinance
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # แสดงข้อมูลหุ้นที่ดึงมาจาก yfinance
    print(stock_data) 

    # ตรวจสอบว่ามีข้อมูลหรือไม่
    if stock_data.empty:
        raise ValueError(f"No data found for symbol: {symbol}")

    # แปลงวันที่จาก index ไปเป็นคอลัมน์ปกติ
    stock_data.reset_index(inplace=True)
    
    # เปลี่ยนชื่อคอลัมน์ให้เหมาะสม
    stock_data.rename(columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Adj Close': 'adjClose', 'Volume': 'volume'}, inplace=True)
    
    return stock_data

@app.route('/')
def index():
    stock_symbols = ["AAPL", "GOOGL", "MSFT"]  # เพิ่มหุ้นตัวอื่น ๆ ที่ต้องการ
    stock_data = {symbol: get_stock_data(symbol) for symbol in stock_symbols}
    data_json = {symbol: data.to_json(orient='records') for symbol, data in stock_data.items()}  # แปลงเป็นรูปแบบที่เหมาะสม
    
    return render_template('index.html', data=data_json)

# Route for predicting stock price
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # รับ JSON data จากการ request
    symbol = data.get('symbol')  # รับ stock symbol จาก request

    if not symbol:
        return jsonify({'error': 'No stock symbol provided'}), 400

    try:
        print(f"Received symbol: {symbol}")  # Debugging - log symbol

        # เรียกฟังก์ชันการพยากรณ์หุ้นจาก model.py
        prediction = predict_stock(symbol)

        # ตรวจสอบว่าการพยากรณ์มีค่าหรือไม่
        if prediction is None:
            raise ValueError("Prediction result is None")

        # ดึงข้อมูลหุ้นย้อนหลัง 2 เดือน
        stock_data = get_stock_data(symbol)

        # แปลงข้อมูลหุ้นให้เป็น list ของ dict เพื่อใช้งานกับ jsonify
        stock_data_list = stock_data.to_dict(orient='records')

        # ส่งข้อมูลหุ้นและผลการพยากรณ์กลับไปเป็น JSON
        return jsonify({
            'symbol': symbol,
            'prediction': round(float(prediction), 3),  # แสดงผลเป็นทศนิยม 3 หลัก
            'data': stock_data_list
        })

    except ValueError as ve:
        print(f"ValueError: {ve}")  # Debugging - log value errors
        return jsonify({'error': str(ve)}), 400  # ส่งข้อผิดพลาดที่เกี่ยวข้องกับข้อมูล
    except Exception as e:
        print(f"Error: {e}")  # Debugging - log error
        return jsonify({'error': 'Error in predicting stock price'}), 500

@app.route('/all-stocks', methods=['GET'])
def all_stocks():
    stock_symbols = ["AAPL", "GOOGL", "MSFT"]  # หุ้นที่คุณต้องการดึงข้อมูล
    stock_data = []

    for symbol in stock_symbols:
        try:
            data = get_stock_data(symbol)
            data['symbol'] = symbol
            print(data)  # ตรวจสอบข้อมูลเพื่อดูว่าค่าถูกต้องหรือไม่
            stock_data.extend(data.to_dict(orient='records'))  # แปลงข้อมูลเป็น JSON
            data = data.rename(columns={
                'Open': 'open',
                'High': 'high',
                'Low': 'low',
                'Close': 'close',
                'Adj Close': 'adjClose',
                'Volume': 'volume',
                'Date': 'date'
            })
            # Add symbol as a new column in the DataFrame
            #data['symbol'] = symbol
            print(data)  # Debug - ตรวจสอบข้อมูล
            stock_data.extend(data.to_dict(orient='records'))  # แปลงข้อมูลเป็น JSON
        except Exception as e:
            print(f"Could not fetch data for {symbol}: {e}")
    print(stock_data)  # Debug ดูข้อมูลที่ถูกส่งกลับไปยังฝั่งไคลเอนต์
    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(debug=True)  # เริ่มต้นแอปพลิเคชัน Flask
