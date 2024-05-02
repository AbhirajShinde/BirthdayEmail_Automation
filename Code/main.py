from datetime import date, datetime
import pandas as pd
from send__email import send_email
from pygoogle_image import image as pi
import os
import random
import delete_images

SHEET_ID = "1FO_L0n6zFwIj_WM9vR3kOcZChR14tbp1eYbPN5uw3A4"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_df(url):
    df = pd.read_csv(url)
    df['Name'] = df['FirstName'] + ' ' + df['LastName']
    return df


def find_birthday_people(df):
    today = date.today()
    birthday_people = []
    for _, row in df.iterrows():
        # Assuming "Birthday" column contains the date of birth in MM/DD format
        birthdate = datetime.strptime(row["Birthdate"], '%Y-%m-%d').replace(year=today.year).date()  # Set the current year
        if birthdate == today:
            birthday_people.append(row["Name"])
    return birthday_people

def download_image(output_directory):
    os.chdir(output_directory)
    pi.download("Birthday hd", limit=5)

def send_email_query(df, birthday_people, selected_image_path):
    for _, row in df.iterrows():
        # Check if the email address is valid (not NaN or empty)
        if pd.notnull(row["EmailID"]) and isinstance(row["EmailID"], str):
            send_email(
                subject="Birthday Wishes..!!",
                receiver_email=row["EmailID"],
                name_list=birthday_people,
                selected_image_path=selected_image_path
            )
    return

def main():
    df = load_df(URL)
    birthday_people = find_birthday_people(df)

    # Check if there are any birthdays today
    if not birthday_people:
        print("No birthdays today.")
        return  # Exit the function if there are no birthdays

    # Download Images
    Curr_directory = os.getcwd()
    relative_path = "Birthday_Images"
    output_directory = os.path.join(Curr_directory, relative_path)
    download_image(output_directory)

    # Get a list of image files in the output directory
    image_subdirectory_path = os.path.join(output_directory, "images\\Birthday_hd")
    image_files = os.listdir(image_subdirectory_path)

    # Filter JPEG images
    jpeg_image_files = [file for file in image_files if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg')]

    # Select one image file path randomly
    selected_image = random.choice(jpeg_image_files)
    selected_image_path = os.path.join(image_subdirectory_path, selected_image)

    # Send emails
    send_email_query(df, birthday_people, selected_image_path)

    # Run delete_images.py after all execution is completed
    delete_images.main()

if __name__ == "__main__":
    main()