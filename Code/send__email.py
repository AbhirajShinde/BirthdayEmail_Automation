import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load the environment variable
current_dir = Path(__file__).resolve().parent.parent
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("Email_ID")
password_email = os.getenv("Email_Password")

def add_text_to_image(image_path, names, padding = 40):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("segoepr.ttf", 40)
    
    text_pos = (padding, padding)
    text_color = (0,0,0)

    names_str = "\n".join(names)

    draw.text(text_pos, names_str, fill=text_color, font=font)
    return image

# Mail Format
def send_email(subject, receiver_email, name_list, selected_image_path):

    # Create the base text message.
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Happy Birthday!!!", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    # HTML content with image
    html_content = f"""\
    <html>
      <body>
        <p>Dear Birthday Celebrants,</p>
        <p>
        Wishing you a day filled with laughter, love, and joy as you celebrate another wonderful year of your life. May this special day bring you all the happiness you deserve.
        </p>

        <p>Happy Birthday!</p>
        <img src="cid:image1">
        
        <p>Best wishes,</p>
        <p>[Organization Name]</p>
      </body>
    </html>
    """
    html_part = MIMEText(html_content, "html")
    msg.attach(html_part)

    # Add names to the image
    birthday_image = add_text_to_image(selected_image_path, name_list)

    # Convert the modified image to bytes
    with BytesIO() as image_buffer:
        birthday_image.save(image_buffer, format='JPEG')
        image_data = image_buffer.getvalue()

    # Attach the modified image
    image_part = MIMEImage(image_data)
    image_part.add_header("Content-ID", "<image1>")
    msg.attach(image_part)

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())
