class DefenseEngine:
    def __init__(self):
        self.policies = {
            "Prompt Injection": ["ignore", "override", "system mode", "bypass", "reset", "delete"],
            "Privilege Escalation": ["unlock", "all doors", "server room", "disable", "admin"]
        }

    def evaluate(self, request):
        request_lower = request.lower()
        threats = []
        policy_triggered = "None"
        risk_score = 0

        for policy, keywords in self.policies.items():
            if any(k in request_lower for k in keywords):
                threats.append(policy)
                policy_triggered = policy
                risk_score += 50

        status = "BLOCKED" if risk_score >= 40 else "ALLOWED"
        
        return {
            "status": status,
            "risk_score": min(risk_score, 100),
            "threats": threats,
            "policy": policy_triggered
        }