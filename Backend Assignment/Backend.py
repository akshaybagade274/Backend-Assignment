from selenium import webdriver
import time

download_path = "C:/Downloads"  # Set your desired download directory path here

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option(
    "prefs", {"download.default_directory": download_path}
)

driver = webdriver.Chrome(
    executable_path="../Drivers/chromedriver.exe", options=chromeOptions
)
driver.maximize_window()

try:
    driver.get("https://example.com/sales-reports")

    # Locate and click the download link/button
    driver.find_element_by_link_text("Download Sales Report").click()

    time.sleep(5)  # Wait for the download to complete (adjust as needed)

    print("Sales report downloaded successfully.")

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    driver.quit()
