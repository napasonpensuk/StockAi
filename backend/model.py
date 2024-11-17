import yfinance as yf
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# โหลดโมเดลที่ฝึกมาแล้ว
model = load_model('models/stock_model.h5')
print(model.summary())  # ตรวจสอบโครงสร้างของโมเดลที่โหลด

# สร้าง scaler ภายนอกฟังก์ชัน
scaler = MinMaxScaler(feature_range=(0, 1))

def predict_stock(symbol):
    try:
        # ดึงข้อมูลหุ้นย้อนหลัง 3 เดือน
        stock_data = yf.download(symbol, period='3mo', interval='1d')
        print(stock_data)  # ตรวจสอบข้อมูลที่ได้รับ
        
        # ตรวจสอบว่ามีข้อมูลเพียงพอหรือไม่
        if stock_data.empty or len(stock_data) < 60:
            raise ValueError("Not enough data to make prediction")
        
        close_prices = stock_data['Close'].values.reshape(-1, 1)
        
        # ใช้ scaler.fit_transform บนข้อมูลราคาปิดทั้งหมดเพื่อฝึก scaler
        scaled_data = scaler.fit_transform(close_prices)
        last_60_days = scaled_data[-60:]

        # สร้าง X_test
        X_test = np.array([last_60_days])
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        print(f"X_test shape: {X_test.shape}")  # พิมพ์ขนาดของ X_test
        
        # ทำการทำนาย
        predicted_price = model.predict(X_test)
        predicted_price = scaler.inverse_transform(predicted_price)
        
        return predicted_price[0][0]
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        print(f"Error during stock prediction: {e}")
        return None
    

# ตัวอย่างการเรียกใช้ฟังก์ชัน
symbol = "AAPL"  # เปลี่ยนเป็นสัญลักษณ์ที่ต้องการทำนาย
predicted_price = predict_stock(symbol)
if predicted_price is not None:
    print(f"Predicted price for {symbol}: ${predicted_price:.2f}")  # แสดงผลในรูปแบบเงิน
else:
    print("Failed to predict price.")
