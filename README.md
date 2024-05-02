# Email Birthday Automation Project

This project automates the process of sending birthday emails to everyone on a list, with a personalized touch of including the recipient's name on a random image in the email template.

## Features

- Sends automated birthday emails to a list of recipients.
- Personalizes each email with the recipient's name on a random image.
- Easy setup and configuration.
- Error handling for robustness.
- Security measures for sensitive information.

## Getting Started

To get started with the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Set up your email service provider (SMTP server, credentials, etc.). Refer to the `.env.example` file for the required environment variables.
4. Replace the Google Sheets link with your own link for the recipients' data in `main.py` (line 13).
5. Customize the email template in `send_email.py` according to your organization's branding.
6. Run the script manually to test: `python main.py`.
7. To automate the script, deploy it on a server or use a scheduler like cron to run it at regular intervals. Ensure that the server has the necessary permissions and environment variables set.

## Configuration

- Replace the Google Sheets link with your own link for the recipients' data in `main.py` (line 13).
- Set up environment variables for your email credentials. Copy `.env.example` to `.env` and fill in the required details.

## Usage

To run the project manually:

```bash
python main.py
