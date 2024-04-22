import requests
from bs4 import BeautifulSoup

# Example URL for scraping
url = "https://example.com/reports"

# Send a GET request
response = requests.get(url)

if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract report links
    report_links = []
    for link in soup.find_all("a", href=True):
        if "report" in link["href"]:
            report_links.append(link["href"])

    # Download reports
    for report_url in report_links:
        report_response = requests.get(report_url)
        if report_response.status_code == 200:
            # Save report to a file
            with open("report.pdf", "wb") as f:
                f.write(report_response.content)
        else:
            print(f"Failed to download report: {report_url}")
else:
    print("Failed to fetch page")
