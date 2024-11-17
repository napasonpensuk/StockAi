import numpy as np
from sklearn.preprocessing import MinMaxScaler

# สมมติว่า close_prices เป็น list ของราคาปิด
close_prices = [100, 102, 98, 105, 110] * 20  # ตัวอย่างข้อมูลที่ยาวขึ้น

# แปลง close_prices เป็น array แบบ 2 มิติ
close_prices = np.array(close_prices).reshape(-1, 1)

# สร้าง scaler และทำการ scale ข้อมูล
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(close_prices)

# ตรวจสอบขนาดของ scaled_data
print(f"Number of rows in scaled_data: {len(scaled_data)}")

# จำนวนวันที่ใช้ทำนาย (60 วัน)
look_back = 60
X_train, y_train = [], []

if len(scaled_data) > look_back:
    for i in range(look_back, len(scaled_data)):
        X_train.append(scaled_data[i-look_back:i, 0])
        y_train.append(scaled_data[i, 0])

    X_train, y_train = np.array(X_train), np.array(y_train)

    # Reshape เพื่อให้เข้ากับรูปแบบที่ LSTM ต้องการ (samples, timesteps, features)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    print("Reshape completed successfully")
else:
    print("Not enough data for the specified look_back period.")
