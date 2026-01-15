# StockAI
StockAI is a web-based AI stock analysis and prediction system. The backend fetches historical stock data, runs machine learning predictions using TensorFlow, and exposes results via API for use in a frontend interface.

# Main Functions
1. Retrieve historical stock price data (via yfinance)
2. Analyze stock price trends
3. Use AI/ML models (e.g., TensorFlow, which is imported in the code) to predict future stock price trends
4. Provide an endpoint/API for web UI to access prediction results
5. Display stock graphs or data via a web interface (e.g., index page)

# Key Features
1. Retrieves historical stock data using yfinance
2. Uses TensorFlow/ML models in model.py for predictions
3. Provides a `/predict` route for the frontend to send symbols and receive results
4. Provides a `/all-stocks` route for retrieving data from multiple stocks simultaneously

<img width="1911" height="965" alt="image" src="https://github.com/user-attachments/assets/b6099e73-867d-46cf-94b2-6b9d6b9d97fb" />

# StockAI
StockAI คือระบบวิเคราะห์และทำนายราคาหุ้นด้วย AI บนเว็บ ระบบแบ็กเอนด์ดึงข้อมูลราคาหุ้นในอดีต รันการทำนายด้วยแมชชีนเลิร์นนิงโดยใช้ TensorFlow และแสดงผลลัพธ์ผ่าน API สำหรับใช้งานในส่วนหน้า

# ฟังก์ชันหลัก
1. ดึงข้อมูลราคาหุ้นในอดีต (ผ่าน yfinance)
2. วิเคราะห์แนวโน้มราคาหุ้น
3. ใช้โมเดล AI/ML (เช่น TensorFlow ซึ่งนำเข้าในโค้ด) เพื่อทำนายแนวโน้มราคาหุ้นในอนาคต
4. จัดเตรียมเอนด์พอยต์/API สำหรับเว็บ UI เพื่อเข้าถึงผลการทำนาย
5. แสดงกราฟหรือข้อมูลหุ้นผ่านเว็บอินเทอร์เฟซ (เช่น หน้าดัชนี)

# คุณสมบัติหลัก
1. ดึงข้อมูลราคาหุ้นในอดีตโดยใช้ yfinance
2. ใช้โมเดล TensorFlow/ML ใน model.py สำหรับการทำนาย
3. จัดเตรียมเส้นทาง `/predict` สำหรับส่วนหน้าเพื่อส่งสัญลักษณ์และรับผลลัพธ์
4. จัดเตรียมเส้นทาง `/all-stocks` สำหรับดึงข้อมูลจากหุ้นหลายตัวพร้อมกัน
