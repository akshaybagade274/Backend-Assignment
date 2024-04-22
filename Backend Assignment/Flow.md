# Automated Sales Report Download Using Selenium WebDriver
- This repository contains a Python script using Selenium WebDriver to automate the download of sales reports from e-commerce websites. The script utilizes Chrome WebDriver and is configured to manage file downloads.
- #### Prerequisites
- Ensure you have the following installed:

- Python 3.x
- Selenium (pip install selenium)
- ChromeDriver (compatible with your Chrome browser version)
- #### Installation
- Clone this repository to your local machine
- Install required Python packages
- #### Usage
- Set the desired download directory in the download_path variable within the script (Backend.py)
- Customize the script by replacing the URL ("https://example.com/sales-reports") with the target e-commerce website where you want to download the sales report.
- Execute --> python Backend.py
- #### Notes
- Replace the URL in the script with the actual e-commerce website URL.
- Update the locator strategy (find_element_by_link_text(), find_element_by_xpath(), etc.) based on the target website's HTML structure.
- Use explicit waits (WebDriverWait) for better synchronization and error handling.
