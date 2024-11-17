import numpy as np
import pandas as pd  # ถ้าคุณใช้ข้อมูลจาก CSV
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import yfinance as yf  # ถ้าคุณดึงข้อมูลจาก yfinance API

# 1. ดึงข้อมูลราคาหุ้น (เลือกวิธีดึงข้อมูลตามที่คุณมี)

# วิธีที่ 1: ใช้ข้อมูลจาก CSV
# df = pd.read_csv('path_to_your_file.csv')
# close_prices = df['Close'].values.reshape(-1, 1)  # สมมติคอลัมน์ชื่อ 'Close'

# วิธีที่ 2: ใช้ yfinance API เพื่อดึงข้อมูลหุ้น
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
close_prices = stock_data['Close'].values.reshape(-1, 1)

# 2. สเกลข้อมูลด้วย MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(close_prices)  # ทำการสเกลข้อมูล

# 3. สร้าง X_train และ y_train
look_back = 60
X_train, y_train = [], []

for i in range(look_back, len(scaled_data)):
    X_train.append(scaled_data[i-look_back:i, 0])
    y_train.append(scaled_data[i, 0])

# แปลง X_train และ y_train เป็น NumPy array
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshape X_train ให้เป็น 3 มิติ (samples, timesteps, features)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# 4. สร้างโมเดล LSTM
model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))  # ลด overfitting

# เพิ่ม LSTM อีกหนึ่งเลเยอร์
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))

# เพิ่ม Dense Layer
model.add(Dense(units=25))
model.add(Dense(units=1))  # เลเยอร์สุดท้ายสำหรับการทำนาย

# คอมไพล์โมเดล
model.compile(optimizer='adam', loss='mean_squared_error')

# แสดงรายละเอียดของโมเดล
model.summary()

# ฝึกโมเดล (ถ้าคุณพร้อมจะฝึกโมเดล)
# model.fit(X_train, y_train, epochs=10, batch_size=32)
