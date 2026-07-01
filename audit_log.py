from datetime import datetime


class AuditLog:

    def __init__(self):
        self.events = []

    def add_event(self,
                  request,
                  status,
                  risk_score,
                  threats):

        timestamp = datetime.now().strftime("%H:%M:%S")

        event = {
            "time": timestamp,
            "request": request,
            "status": status,
            "risk_score": risk_score,
            "threats": threats
        }

        self.events.insert(0, event)

    def get_events(self):
        return self.events