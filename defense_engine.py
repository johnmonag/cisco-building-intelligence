class DefenseEngine:
    """
    Simulates Cisco AI Defense.
    Evaluates prompts and returns a security decision.
    """

    def evaluate(self, request):

        request = request.lower()

        threats = []
        risk_score = 5
        status = "ALLOWED"

        # Prompt Injection
        if "ignore all instructions" in request:
            threats.append("Prompt Injection")
            risk_score = 95
            status = "BLOCKED"

        # Privilege Escalation
        if "unlock all doors" in request:
            threats.append("Privilege Escalation")
            risk_score = 95
            status = "BLOCKED"

        # Data Exfiltration
        if "camera feeds" in request:
            threats.append("Data Exfiltration")
            risk_score = 95
            status = "BLOCKED"

        return {
            "status": status,
            "risk_score": risk_score,
            "threats": threats
        }