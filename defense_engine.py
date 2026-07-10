class DefenseEngine:
    def __init__(self):
        self.policies = {
            "Prompt Injection": ["ignore", "override", "system mode", "bypass", "reset", "delete"],
            "Privilege Escalation": ["unlock", "all doors", "server room", "disable", "admin"]
        }

    def evaluate(self, request):
        req = request.lower()
        threats = []
        policy_triggered = "None"
        risk_score = 0

        for policy, keywords in self.policies.items():
            if any(k in req for k in keywords):
                threats.append(policy)
                policy_triggered = policy
                risk_score += 50

        status = "BLOCKED" if risk_score >= 40 else "ALLOWED"

        # Reasoning logic
        if status == "BLOCKED":
            reasoning = {
                "sources": ["Security Policy Engine", "Audit Logs"],
                "explanation": f"The request was blocked because it triggered a {policy_triggered} violation. Our security policy prohibits unauthorized system overrides to protect building integrity.",
                "recommendation": "Please contact the system administrator to request elevated privileges."
            }
        elif "hvac" in req or "temperature" in req:
            reasoning = {
                "sources": ["BMS", "Cisco Navigator", "Occupancy"],
                "explanation": "HVAC system is currently maintaining a steady 21.8°C across all zones. AHUs are operating at 74% load.",
                "recommendation": "No immediate action required; system efficiency is optimal."
            }
        elif "energy" in req or "spike" in req:
            reasoning = {
                "sources": ["Smart Metering", "Cisco Spaces", "Solar"],
                "explanation": "The 40% energy spike was caused by an unscheduled event in the North wing at 2:15 PM.",
                "recommendation": "Integrate event booking with BMS to pre-condition spaces."
            }
        else:
            reasoning = {
                "sources": ["General System Logs"],
                "explanation": "System status is nominal. All services are currently reporting normal telemetry.",
                "recommendation": "Continue monitoring."
            }

        return {
            "status": status,
            "risk_score": min(risk_score, 100),
            "threats": threats,
            "policy": policy_triggered,
            "reasoning": reasoning
        }