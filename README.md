# Job Scraper with Django and MongoDB

## 📌 Project Overview

This project is a web-based **Job Scraper** built using **Django** and **MongoDB**. It scrapes job listings from **Indeed.com** for "Python Developer" roles, stores the data in MongoDB, and provides an admin panel to manage and search jobs.

## 🚀 Features

- **Scrape Job Listings**: Extracts job details from Indeed.com.
- **MongoDB Storage**: Stores scraped job data efficiently.
- **Django Admin Panel**: Manage job listings via an easy-to-use UI.
- **Search & Filter Jobs**: Find jobs based on keywords.
- **Salary Insights**: Calculates the average salary using NumPy.
- **Deployment Ready**: Can be hosted on **Render** or any cloud provider.

## 🛠️ Tech Stack

- **Backend**: Django
- **Database**: MongoDB (using Djongo)
- **Scraping**: BeautifulSoup / Requests
- **Data Processing**: NumPy
- **Deployment**: Render

## 📂 Project Structure

```
job_scraper/
│── jobs/               # Django app for job management
│── staticfiles/        # Static assets
│── templates/         # HTML templates
│── job_scraper.py      # Scraper script
│── manage.py          # Django management script
│── requirements.txt    # Dependencies
│── README.md          # Project documentation
```

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/job_scraper.git
cd job_scraper
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up MongoDB

Ensure MongoDB is running locally or provide a **MongoDB Atlas URI** in `settings.py`:

```python
D00ATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'job_scraper_db',
        'CLIENT': {
            'host': 'your_mongodb_uri_here'
        }
    }
}
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Scraper

```bash
python job_scraper.py
```

### 6️⃣ Start the Django Server

```bash
python manage.py runserver
```

Access the app at: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

## 🚀 Deploying on Render

1. **Push your code to GitHub**.
2. **Create a new Render web service**.
3. **Set Python as the environment and MongoDB as the database**.
4. **Render will automatically install dependencies** from `requirements.txt`.
5. **Check logs if errors occur**.

## 🔗 Contributions & Issues

Feel free to fork this project, submit PRs, or open issues if you find bugs.


