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
