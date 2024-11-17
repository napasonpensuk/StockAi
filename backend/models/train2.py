import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf  # หรืออ่านจาก CSV ตามที่คุณใช้

# ดึงข้อมูลหุ้นจาก yfinance
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
close_prices = stock_data['Close'].values.reshape(-1, 1)

# สเกลข้อมูล
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(close_prices)

# สร้าง X_train และ y_train
look_back = 60
X_train, y_train = [], []

for i in range(look_back, len(scaled_data)):
    X_train.append(scaled_data[i-look_back:i, 0])
    y_train.append(scaled_data[i, 0])

# แปลง X_train และ y_train เป็น NumPy array
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshape X_train ให้เป็น 3 มิติ (samples, timesteps, features)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# สร้างโมเดล LSTM
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

# ฝึกโมเดล
model.fit(X_train, y_train, batch_size=64, epochs=10)
