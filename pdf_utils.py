from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(name, stress, blinks, screen_time, mouse, keys):
    file_path = "report.pdf"

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(file_path)

    content = []

    # =========================
    # 🧾 HEADER
    # =========================
    content.append(Paragraph("AI  Monitoring Report", styles["Title"]))
    content.append(Spacer(1, 10))

    # =========================
    # 👤 USER DATA
    # =========================
    content.append(Paragraph(f"<b>User:</b> {name}", styles["Normal"]))
    content.append(Paragraph(f"<b>Stress Score:</b> {stress}", styles["Normal"]))
    content.append(Paragraph(f"<b>Blinks:</b> {blinks}", styles["Normal"]))
    content.append(Paragraph(f"<b>Screen Time:</b> {screen_time} sec", styles["Normal"]))
    content.append(Paragraph(f"<b>Mouse Clicks:</b> {mouse}", styles["Normal"]))
    content.append(Paragraph(f"<b>Keystrokes:</b> {keys}", styles["Normal"]))
    content.append(Spacer(1, 15))

    # =========================
    # 📊 STRESS LEVEL
    # =========================
    if stress <= 50:
        level = "Low"
    elif stress <= 70:
        level = "Moderate"
    else:
        level = "High"

    content.append(Paragraph(f"<b>Stress Level:</b> {level}", styles["Heading2"]))
    content.append(Spacer(1, 10))

    # =========================
    # 🧠 INSIGHTS
    # =========================
    insights = []

    if screen_time > 3600:
        insights.append("You have been working for a long time without sufficient breaks.")

    if blinks < 10:
        insights.append("Low blink rate detected — possible eye strain.")

    if mouse + keys > 500:
        insights.append("High activity detected — you may be overworking.")

    if stress > 70:
        insights.append("Your stress level is significantly high and needs attention.")

    if not insights:
        insights.append("Your activity looks balanced and healthy.")

    content.append(Paragraph("<b>Insights:</b>", styles["Heading2"]))
    for ins in insights:
        content.append(Paragraph(f"- {ins}", styles["Normal"]))

    content.append(Spacer(1, 15))

    # =========================
    # 💡 RECOMMENDATIONS
    # =========================
    recommendations = []

    if stress > 70:
        recommendations.append("Take a 10–15 minute break immediately.")
        recommendations.append("Practice deep breathing or short meditation.")

    if screen_time > 3600:
        recommendations.append("Follow the 20-20-20 rule for eye care.")

    if blinks < 10:
        recommendations.append("Blink more often or look away from screen.")

    if mouse + keys > 500:
        recommendations.append("Slow down your work pace to avoid burnout.")

    if not recommendations:
        recommendations.append("Keep maintaining this healthy routine!")

    content.append(Paragraph("<b>Recommendations:</b>", styles["Heading2"]))
    for rec in recommendations:
        content.append(Paragraph(f"- {rec}", styles["Normal"]))

    content.append(Spacer(1, 20))

    # =========================
    # 🧠 SUMMARY
    # =========================
    summary = f"This session indicates a {level.lower()} stress level."

    if stress > 70:
        summary += " Immediate relaxation is recommended."
    elif stress > 50:
        summary += " Consider taking short breaks regularly."
    else:
        summary += " You are doing well. Keep it up!"

    content.append(Paragraph("<b>Summary:</b>", styles["Heading2"]))
    content.append(Paragraph(summary, styles["Normal"]))

    # BUILD PDF
    doc.build(content)

    return file_path