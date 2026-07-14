import random

class DefenseEngine:
    def __init__(self):
        self.policies = {
            "Prompt Injection": ["ignore", "override", "system mode", "bypass", "reset", "delete"],
            "Privilege Escalation": ["unlock", "all doors", "server room", "disable", "admin"]
        }

    def check_talos_reputation(self, request):
        """
        Simulates a lookup against Cisco Talos Intelligence.
        Context-aware: flags malicious intent consistently.
        """
        req = request.lower()
        malicious_keywords = ["unlock", "bypass", "override", "ignore", "delete", "admin"]

        if any(k in req for k in malicious_keywords):
            return {
                "reputation": "MALICIOUS",
                "threat_category": "Unauthorized Access Attempt"
            }

        # Small chance of random noise, otherwise CLEAN
        is_malicious = random.random() < 0.05
        return {
            "reputation": "MALICIOUS" if is_malicious else "CLEAN",
            "threat_category": "Botnet C2" if is_malicious else "None"
        }

    def evaluate(self, request):
        req = request.lower()
        threats = []
        policy_triggered = "None"
        risk_score = 0

        # 1. Run Policy Check
        for policy, keywords in self.policies.items():
            if any(k in req for k in keywords):
                threats.append(policy)
                policy_triggered = policy
                risk_score += 50

        # 2. Run Talos Check
        talos_data = self.check_talos_reputation(req)
        if talos_data["reputation"] == "MALICIOUS":
            threats.append(f"Talos Intelligence: {talos_data['threat_category']}")
            policy_triggered = "Talos Threat Intelligence"
            risk_score += 60

        status = "BLOCKED" if risk_score >= 40 else "ALLOWED"

        # 3. Context-Aware Reasoning Logic
        if status == "BLOCKED":
            reasoning = {
                "sources": ["Security Policy Engine", "Cisco Talos Intelligence"],
                "explanation": f"The request was blocked because it triggered a {policy_triggered} violation. Our security policy prohibits unauthorized system overrides to protect building integrity.",
                "causality": "Unauthorized intent detected by Talos threat feed or policy engine.",
                "recommendation": "Please contact the system administrator to request elevated privileges."
            }
        elif "hvac anomaly" in req or "sensor failure" in req:
            reasoning = {
                "sources": ["Splunk HVAC Index", "BMS Controller Logs", "Power Metering"],
                "explanation": "AI detected 206°C readings but confirmed a sensor glitch, not a boiling event. Cross-referencing power draw (35.4kW) and the lack of thermal lag confirms a data corruption issue.",
                "causality": "Electrical transient caused simultaneous multi-sensor circuit failure.",
                "recommendation": "1. Inspect sensor wiring for EMI. 2. Test power quality at sensor circuits. 3. Flag 30 mins of data as corrupted."
            }
        elif "hvac" in req or "temperature" in req:
            reasoning = {
                "sources": ["BMS", "Cisco Navigator", "Occupancy"],
                "explanation": "HVAC system is currently maintaining a steady 21.8°C across all zones. AHUs are operating at 74% load.",
                "causality": "Normal operation.",
                "recommendation": "No immediate action required; system efficiency is optimal."
            }
        elif "energy" in req or "spike" in req:
            reasoning = {
                "sources": ["Smart Metering", "Cisco Spaces", "Solar"],
                "explanation": "The 40% energy spike was caused by an unscheduled event in the North wing at 2:15 PM.",
                "causality": "High occupancy triggered HVAC ramping during low solar output.",
                "recommendation": "Integrate event booking with BMS to pre-condition spaces."
            }
        else:
            reasoning = {
                "sources": ["General System Logs"],
                "explanation": "System status is nominal. All services are currently reporting normal telemetry.",
                "causality": "N/A",
                "recommendation": "Continue monitoring."
            }

        return {
            "status": status,
            "risk_score": min(risk_score, 100),
            "threats": threats,
            "policy": policy_triggered,
            "reasoning": reasoning
        }