import streamlit as st
from building_controller import BuildingController
from defense_engine import DefenseEngine
from audit_log import AuditLog

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Cisco AI Defense Demo", page_icon="🛡", layout="wide")

st.title("🏢 AI Smart Building Assistant")
st.caption("Protected by Cisco AI Defense")
st.divider()

# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------
if "building" not in st.session_state:
    st.session_state.building = BuildingController()
if "engine" not in st.session_state:
    st.session_state.engine = DefenseEngine()
if "audit" not in st.session_state:
    st.session_state.audit = AuditLog()
if "messages" not in st.session_state:
    st.session_state.messages = []

# Accessing session objects
building = st.session_state.building
engine = st.session_state.engine
audit = st.session_state.audit

# --------------------------------------------------
# LAYOUT
# --------------------------------------------------
left, right = st.columns([2, 1])

# -----------------------------
# LEFT PANEL (Chat Interface)
# -----------------------------
with left:
    st.header("💬 Smart Building Assistant")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask me to control the building..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 1. Ask Cisco AI Defense
        decision = engine.evaluate(prompt)
        st.session_state.last_decision = decision
        
        # 2. Record the event
        audit.add_event(
            request=prompt,
            status=decision["status"],
            risk_score=decision["risk_score"],
            threats=decision["threats"]
        )

        # 3. Handle response
        with st.chat_message("assistant"):
            if decision["status"] == "ALLOWED":
                response = "✅ Request approved. I've updated the building systems."
                if "light" in prompt.lower(): building.turn_on_lights()
                elif "temperature" in prompt.lower(): building.set_temperature(22)
                elif "unlock" in prompt.lower(): building.unlock_doors()
            else:
                response = "🚫 Request blocked by Cisco AI Defense. Security risk detected."
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# -----------------------------
# RIGHT PANEL (Dashboard)
# -----------------------------
with right:
    st.header("🛡 Cisco AI Defense")
    
    if "last_decision" in st.session_state:
        decision = st.session_state.last_decision
        st.metric("Risk Score", decision["risk_score"])
        st.progress(decision["risk_score"] / 100)
        
        if decision["status"] == "ALLOWED":
            st.success("✅ ALLOWED")
        else:
            st.error("🚫 BLOCKED")

        st.subheader("Threats")
        if decision["threats"]:
            for threat in decision["threats"]:
                st.warning(threat)
        else:
            st.write("None")
            
        st.subheader("Policy Enforcement")
        if decision.get("policy") and decision["policy"] != "None":
            st.code(f"POLICY: {decision['policy']}", language="text")
        else:
            st.write("No policy violations.")
    else:
        st.metric("Risk Score", "--")
        st.progress(0)
        st.info("Waiting for request...")

    st.divider()
    st.subheader("🏢 Building Status")
    status = building.status()
    st.write(f"💡 Lights: **{status['lights']}**")
    st.write(f"🌡 HVAC: **{status['temperature']}°C**")
    st.write(f"🚪 Doors: **{status['doors']}**")
    st.write(f"📹 Cameras: **{status['cameras']}**")

# --------------------------------------------------
# AUDIT TIMELINE
# --------------------------------------------------
st.divider()
st.header("📜 Live Security Audit Log")
events = audit.get_events()
if events:
    st.table(events[-5:][::-1])
else:
    st.info("No security events recorded yet.")