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

        # Define reasoning dictionary
        if risk_score >= 40:
            reasoning = {
                "sources": ["Security Policy Engine"],
                "explanation": "Unauthorized command detected.",
                "causality": "Security policy violation.",
                "recommendation": "Contact administrator."
            }
        elif "hvac" in req or "temperature" in req:
            reasoning = {
                "sources": ["BMS", "Cisco Navigator"],
                "explanation": "HVAC system is maintaining 21.8°C.",
                "causality": "Normal operation.",
                "recommendation": "No action required."
            }
        else:
            reasoning = {
                "sources": ["System Logs"],
                "explanation": "System nominal.",
                "causality": "N/A",
                "recommendation": "Continue monitoring."
            }

        return {
            "status": "BLOCKED" if risk_score >= 40 else "ALLOWED",
            "risk_score": min(risk_score, 100),
            "threats": threats,
            "policy": policy_triggered,
            "reasoning": reasoning
        }