import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient

# Random User-Agents to avoid bot detection
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
]

# MongoDB Configuration
MONGO_URI = "mongodb+srv://user_idname:password@cluster0.oqox0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "job_scraper"
COLLECTION_NAME = "jobs"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
print("✅ Connected to MongoDB.")

# Setup Chrome options
options = Options()
options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_jobs(search_keyword="Python Developer", location="Lucknow"):
    url = f"https://in.indeed.com/jobs?q={search_keyword}&l={location}"
    driver.get(url)
    time.sleep(random.randint(3, 7))  # Random delay

    # Scroll down to load more jobs
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(random.uniform(2, 4))

    try:
        job_listings = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'job_seen_beacon')]")
        ))
        print(f"✅ Found {len(job_listings)} job listings!")
    except Exception as e:
        print(f"❌ Error finding job listings: {e}")
        driver.quit()
        return

    # Extract job details
    jobs_data = []
    for job in job_listings[:10]:
        try:
            company_element = job.find_elements(By.XPATH, ".//span[@data-testid='company-name']")
            company = company_element[0].text.strip() if company_element else "Company not found"

            location_element = job.find_elements(By.XPATH, ".//div[@data-testid='text-location']")
            location = location_element[0].text.strip() if location_element else "Location not found"

            salary_element = job.find_elements(By.XPATH, ".//div[contains(@class, 'salary-snippet-container')]")
            salary = salary_element[0].text.strip() if salary_element else "Not specified"

            job_data = {"company": company, "location": location, "salary": salary}
            jobs_data.append(job_data)

            print(f"🏢 {company} | 📍 {location} | 💰 {salary}")
        except Exception as e:
            print("⚠ Error extracting job details:", e)

    driver.quit()

    # Store job data in MongoDB
    if jobs_data:
        collection.insert_many(jobs_data)
        print(f"✅ Stored {len(jobs_data)} job listings in MongoDB.")

# Run the scraper
scrape_jobs()

client.close()
