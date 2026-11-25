import os
import re
import shutil
import requests


def move_jpg_files():
    """Move all .jpg/.jpeg files from a source folder to a destination folder."""
    src_dir = input("Enter source folder path: ").strip()
    dest_dir = input("Enter destination folder path: ").strip()

    if not os.path.isdir(src_dir):
        print(f"Error: Source directory '{src_dir}' does not exist.")
        return

    os.makedirs(dest_dir, exist_ok=True)
    moved_count = 0

    for filename in os.listdir(src_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            src_path = os.path.join(src_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            if os.path.isfile(src_path):
                shutil.move(src_path, dest_path)
                print(f"Moved: {filename}")
                moved_count += 1

    print(f"\nDone! Moved {moved_count} JPG file(s) to '{dest_dir}'.")


def extract_emails():
    """Extract all unique email addresses from a .txt file and save them."""
    input_file = input("Enter input .txt file path: ").strip()
    output_file = input("Enter output .txt file path (e.g., emails.txt): ").strip()

    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()

        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = sorted(set(re.findall(email_pattern, content)))

        with open(output_file, "w", encoding="utf-8") as f:
            for email in emails:
                f.write(email + "\n")

        print(f"\nDone! Extracted {len(emails)} unique email(s) to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def scrape_webpage_title():
    """Fetch a webpage and save its <title> tag content to a text file."""
    url = input("Enter webpage URL (e.g., https://www.python.org): ").strip()
    output_file = input("Enter output .txt file path (e.g., title.txt): ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
        title = match.group(1).strip() if match else "No title found"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\nTitle: {title}\n")

        print(f"\nDone! Title: '{title}' saved to '{output_file}'.")
    except requests.RequestException as e:
        print(f"Network error: {e}")


def main():
    while True:
        print("\n=== Python Task Automation Suite ===")
        print("1. Move all .jpg files to a new folder")
        print("2. Extract email addresses from a .txt file")
        print("3. Scrape the title of a webpage")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_webpage_title()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()