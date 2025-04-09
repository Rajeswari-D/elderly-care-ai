from flask import Flask, render_template_string, request
from agents.health_agent import check_health
from agents.safety_agent import check_safety
from agents.reminder_agent import send_reminder
from utils.voice_alerts import simulate_voice_alert
from models.ollama_embedding_model import process_with_ollama

app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elderly Care AI Dashboard</title>
    <style>
        body {
            background: linear-gradient(to right, #e0eafc, #cfdef3);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #2c3e50;
        }
        form {
            background: white;
            padding: 30px;
            border-radius: 12px;
            display: inline-block;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        input[type="text"] {
            padding: 10px;
            width: 300px;
            border-radius: 6px;
            border: 1px solid #ccc;
            margin-bottom: 20px;
        }
        button {
            padding: 10px 20px;
            margin: 10px;
            border: none;
            border-radius: 6px;
            background-color: #3498db;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        p {
            margin-top: 30px;
            font-size: 18px;
            color: #34495e;
        }
    </style>
</head>
<body>
    <h1>Elderly Care AI Dashboard</h1>
    <form method="POST">
        <input type="text" name="bp" placeholder="Enter BP Level" required />
        <br>
        <button name="action" value="health">Check Health</button>
        <button name="action" value="safety">Check Safety</button>
        <button name="action" value="reminder">Send Reminders</button>
        <button name="action" value="voice">Simulate Voice Alert</button>
    </form>
    {% if result %}<p><strong>Result:</strong> {{ result }}</p>{% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        bp_level = request.form.get('bp')
        action = request.form.get('action')

        # Process input using ollama embedding model
        embedding_result = process_with_ollama(bp_level)

        if action == 'health':
            result = check_health(bp_level, embedding_result)
        elif action == 'safety':
            result = check_safety(bp_level, embedding_result)
        elif action == 'reminder':
            result = send_reminder(bp_level, embedding_result)
        elif action == 'voice':
            result = simulate_voice_alert(bp_level, embedding_result)

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)