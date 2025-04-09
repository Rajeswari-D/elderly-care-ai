from agents.health_agent import HealthAgent
from agents.safety_agent import SafetyAgent
from agents.reminder_agent import ReminderAgent

class CoordinatorAgent:
    def __init__(self):
        self.health_agent = HealthAgent()
        self.safety_agent = SafetyAgent()
        self.reminder_agent = ReminderAgent()

    def run(self):
        print("Coordinator running checks...")
        self.health_agent.check_health()
        self.safety_agent.check_safety()
        self.reminder_agent.send_reminders()
