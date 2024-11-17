document.getElementById('stock-form').addEventListener('submit', function(event) {
    event.preventDefault();  // ป้องกันไม่ให้ฟอร์มถูกส่ง

    const stockSymbol = document.getElementById('stock-symbol').value;  // รับค่าจาก input

    // ส่งข้อมูลไปยัง backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ symbol: stockSymbol }),  // แปลงข้อมูลเป็น JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();  // แปลงผลลัพธ์จาก JSON
    })
    .then(data => {
        // แสดงผลการทำนาย
        const predictionResultDiv = document.getElementById('prediction-result');
        predictionResultDiv.innerText = `Predicted Price: $${data.prediction.toFixed(2)}`;
    })
    .catch(error => {
        console.error('Error:', error);
        const predictionResultDiv = document.getElementById('prediction-result');
        predictionResultDiv.innerText = 'Error occurred while predicting price.';
    });
});
