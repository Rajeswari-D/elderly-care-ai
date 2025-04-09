import json
from utils.db_helper import get_today_reminders
from utils.voice_alerts import speak_alert

class ReminderAgent:
    def send_reminders(self):
        print("ReminderAgent: Fetching reminders...")
        reminders = get_today_reminders()
        for reminder in reminders:
            print(f"Reminder: {reminder}")
            speak_alert(f"Reminder: {reminder}")
