import streamlit as st

# ----------------------------------------------------
# PAGE SETUP
# ----------------------------------------------------

st.set_page_config(
    page_title="Cisco AI Defense Demo",
    page_icon="🛡",
    layout="wide"
)

st.title("🏢 AI Smart Building Assistant")
st.caption("Protected by Cisco AI Defense")

st.divider()

# ----------------------------------------------------
# CREATE TWO COLUMNS
# ----------------------------------------------------

left, right = st.columns([2,1])

# These variables will be updated after the user submits
risk_score = 0
status = ""
threats = []
building_action = ""

# ====================================================
# LEFT SIDE - SMART BUILDING ASSISTANT
# ====================================================

with left:

    st.header("💬 Smart Building Assistant")

    user_request = st.text_area(
        "Enter your request:",
        placeholder="Example: Turn on lights in Conference Room A",
        height=150
    )

    submit = st.button("Submit Request")

# ====================================================
# PROCESS THE REQUEST
# ====================================================

if submit:

    request = user_request.lower()

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

    # Safe Actions

    if status == "ALLOWED":

        if "light" in request:
            building_action = "💡 Lights turned ON in Conference Room A"

        elif "temperature" in request:
            building_action = "🌡 Temperature set to 22°C"

        elif "unlock" in request:
            building_action = "🚪 West Entrance unlocked"

        else:
            building_action = "No building action matched."

# ====================================================
# DISPLAY CHAT
# ====================================================

with left:

    if submit:

        st.divider()

        st.subheader("Conversation")

        st.chat_message("user").write(user_request)

        if status == "ALLOWED":

            st.chat_message("assistant").write(
                "Your request has been approved and executed."
            )

            st.success(building_action)

        else:

            st.chat_message("assistant").write(
                "I cannot complete that request because it violates security policy."
            )

# ====================================================
# RIGHT SIDE - AI DEFENSE DASHBOARD
# ====================================================

with right:

    st.header("🛡 Cisco AI Defense")

    st.metric(
        "Risk Score",
        risk_score
    )

    st.progress(risk_score / 100)

    st.divider()

    if status == "ALLOWED":

        st.success("✅ Request Allowed")

    elif status == "BLOCKED":

        st.error("🚫 Request Blocked")

    else:

        st.info("Waiting for request...")

    st.divider()

    st.subheader("Threats")

    if len(threats) == 0:

        st.write("No threats detected.")

    else:

        for threat in threats:

            st.warning(threat)

    st.divider()

    st.subheader("Building Systems")

    st.write("💡 Lighting")
    st.write("🟢 Online")

    st.write("")

    st.write("🌡 HVAC")
    st.write("🟢 Online")

    st.write("")

    st.write("🚪 Doors")
    st.write("🟢 Online")

    st.write("")

    st.write("📹 Cameras")
    st.write("🟢 Online")