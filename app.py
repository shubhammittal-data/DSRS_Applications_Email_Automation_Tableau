from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# 🔹 Gmail SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "shubhammittal1899@gmail.com"  
SENDER_PASSWORD = "cdyrhwasbriuhzvd"  # Gmail App Password

def send_email(student_email, student_name, status):
    """
    Sends an email to the given student using Gmail SMTP.
    """
    
    subject = "Application Status"
    body = f"""Dear {student_name},

We are pleased to inform you that you have been {status} for the position.

Best regards,
Admissions Team
"""

    # Create the email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = student_email

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, student_email, msg.as_string())
        
        return True, "Email sent successfully."
    except Exception as e:
        return False, str(e)

@app.route("/send-email", methods=["GET"])
def handle_send_email():
    """
    HTTP endpoint to receive email requests from Tableau.
    Example request: /send-email?email=student@gmail.com&first_name=John&status=selected
    """
    
    student_email = request.args.get("email")
    student_name = request.args.get("first_name")
    status = request.args.get("status", "selected")  # Default to "selected" if not provided

    if not student_email or not student_name:
        return jsonify({"success": False, "message": "Missing required parameters."}), 400

    success, message = send_email(student_email, student_name, status)
    
    if success:
        return jsonify({"success": True, "message": message})
    else:
        return jsonify({"success": False, "message": message}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
