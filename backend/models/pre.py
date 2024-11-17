import yfinance as yf

# ดึงข้อมูลหุ้นย้อนหลังของ Apple (AAPL)
data = yf.download('AAPL', start='2022-01-01', end='2023-01-01')

# ใช้เฉพาะราคาปิด
close_prices = data['Close'].values.reshape(-1, 1)
