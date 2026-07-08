Description

This project is a Python script for automatically sending job application emails to companies from an Excel file.

The system reads a list of companies, gets the contact email, selects a random subject, sends an HTML email with a PDF resume attached, and logs the result.

It is intended for organized job applications related to QA, manual testing, automation, SQL, Jira/Xray, and similar technology roles.

Features
Reads companies from an Excel file.
Sends emails using Gmail SMTP.
Supports HTML email templates.
Attaches a PDF resume.
Uses random email subjects.
Uses random delay between emails.
Logs messages to console and logs/app.log.
Dynamic countdown between emails.
Configuration through .env.
Project structure
gmail-automation/
│
├── attachments/
│   └── CV_AndresRamirez.pdf
│
├── data/
│   └── empresas.xlsx
│
├── logs/
│   └── app.log
│
├── services/
│   ├── excel_service.py
│   ├── gmail_service.py
│   └── logger_service.py
│
├── templates/
│   └── correo.html
│
├── .env
├── .gitignore
├── config.py
├── main.py
├── readme.md
└── requirements.txt
Requirements
Python 3.10 or higher.
Gmail account.
Gmail app password.
Excel file with companies.
PDF resume.
Installation

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install dependencies:

python -m pip install -r requirements.txt
Configuration

Create a .env file in the project root:

EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
DELAY_MIN_SECONDS=30
DELAY_MAX_SECONDS=90
CV_PATH=attachments/CV_AndresRamirez.pdf

Do not upload the .env file to GitHub.

Expected Excel format

The file should be located at:

data/empresas.xlsx

It should include at least these columns:

empresa
correo

Example:

empresa              correo
Empresa QA S.A.S      rrhh@empresa.com
Tech Company          jobs@techcompany.com
Run
python main.py
Logs

The system prints information in the console and saves logs in:

logs/app.log

Logs include:

Processed company.
Sent subject.
Email result.
Configured waiting time.
Errors if they occur.
Good practices
Do not send too many emails per day.
Use random delays.
Personalize the email body when possible.
Avoid sending duplicate emails to the same company.
Validate that the resume file exists before running.
Keep .env out of the repository.