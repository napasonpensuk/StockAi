import numpy as np
from sklearn.preprocessing import MinMaxScaler

# สมมติว่า close_prices เป็น list ของราคาปิด
close_prices = [100, 102, 98, 105, 110]

# แปลง close_prices เป็น array แบบ 2 มิติ
close_prices = np.array(close_prices).reshape(-1, 1)

# สร้าง scaler และทำการ scale ข้อมูล
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(close_prices)

# แสดงผลลัพธ์
print(scaled_data)
