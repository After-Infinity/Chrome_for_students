from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import messagebox

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = './/chrome-win64/chrome.exe'
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

text_to_look = ["keam", "neet", "jee", ""]

def webscraper(url, *target_texts):
    driver.get(url)
    driver.maximize_window()

    # Check if target_texts is not empty
    if not target_texts:
        print("No target texts provided.")
        return

    while True:
        try:
            title_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='title']/h1/yt-formatted-string")))
            current_title = title_element.text.strip()

            if not current_title:
                print("Title is blank. Printing None.")
            else:
                print("Video Title:", current_title)

                # Check if any of the target texts is present in the current title
                found_target = any(target_text.lower() in current_title.lower() for target_text in target_texts if target_text)

                if found_target:
                    print(f"Target text found in the title: {', '.join(target_texts)}")
                    # Add your code here for actions to take when the target text is found
                else:
                    print("None of the target texts found in the title. Going back.")
                    driver.back()

                    def show_yes_no_popup():
                        result = messagebox.askyesno("Question", "CONCENTRATE MAN")
                        if result:
                            # Add your code here for the action to be taken when "Yes" is clicked
                            print("User clicked Yes")
                        else:
                            # Add your code here for the action to be taken when "No" is clicked
                            print("User clicked No")
                            driver.get("file:///C:/Users/afterinfinity/Downloads/Snapinsta.app_video_119421664_875444510710180_2334015300641129347_n.mp4")


                    # Create the main window
                    root = tk.Tk()

                    # Set the main window to be always on top
                    root.attributes('-topmost', True)

                    # Create a button that, when clicked, shows the Yes/No popup
                    button = tk.Button(root, text="justclick MAN", command=show_yes_no_popup)
                    button.pack(pady=20)

                    # Run the main loop
                    root.mainloop()


            time.sleep(10)

        except NoSuchElementException:
            print("Title not found. Retrying in 10 seconds...")
            time.sleep(10)

# Example usage
webscraper("https://www.youtube.com", *text_to_look)
