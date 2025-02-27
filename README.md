# DSRS_Applications_Email_Automation_Tableau
# 📩 Automating Email Sending from Tableau Using Python (Flask + Gmail)

## 📌 Introduction
This project automates email sending from **Tableau** using a **Python Flask web service**. When a user clicks a student's NetID in **Tableau**, an email is automatically sent via **Gmail SMTP**. 

### 🎯 Key Features:
- **Tableau URL Actions** trigger an email when a student is selected.
- **Python Flask Web Service** processes the request.
- **Emails are sent using Gmail SMTP** for seamless communication.
- **Interactive Tableau dashboard** for tracking responses.

---

## 🛠️ Technologies Used
- **Tableau Public** – Interactive dashboard.
- **Python (Flask)** – Backend API for email automation.
- **Gmail SMTP** – Secure email sending.
- **GitHub** – Version control & project hosting.

---

## 🏗️ How It Works
1. **User clicks a student’s NetID in Tableau.**
2. **Tableau sends a request** to the Flask web service.
3. **Flask processes the request** and sends an email.
4. **Email is delivered** via Gmail SMTP.

---

## 🖥️ Installation & Setup

### **1️⃣ Install Python & Required Libraries**
Ensure Python is installed:
```sh
python --version
```
Install Flask and email libraries:
```sh
pip install flask
```
2️⃣ Update the Email Configuration
Modify app.py with your Gmail SMTP credentials:
```sh
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Use an App Password if 2FA is enabled
```
## 🚨 Use App Passwords instead of your actual password if 2FA is enabled.
Follow this guide to generate an App Password.

3️⃣ Run the Flask Web Service
Start the Python web service:
If you are successful you should see:
```sh
Running on http://0.0.0.0:5000
```
## 📧 Python Script (app.py) for Sending Emails via Gmail (Uploaded above)
## 📝 Tableau Integration
1️⃣ Open Tableau
Connect your student dataset (Excel, CSV, or Database).
Create a table view with NetID, First Name, Email, Status.

2️⃣ Add a URL Action
Go to Dashboard > Actions > Add Action > URL
Action Name: Send Email on Selection
URL Configuration:
```sh
http://localhost:5000/send-email?email=<Email>&first_name=<First Name>&status=selected
```
Click OK and Test the Dashboard.
✅ Now, clicking on a student will send an email automatically!

## 📊 Project Screenshots
Tableau Dashboard
![Dashboard Overview](dashboard_overview.png)

##🚀 Testing the Email Service
To manually test the API:

Open your browser.
Enter the following URL:
```sh
http://localhost:5000/send-email?email=student@gmail.com&first_name=John&status=selected
```
Check the email inbox for confirmation.

## 🚀 How to Use This Project
### **1️⃣ Access the Dashboard**
🔗 **[View the Live Tableau Dashboard](https://public.tableau.com/your-dashboard-link)**

##🤝 Contributing
###Feel free to fork this repository and submit a pull request.







