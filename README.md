🐦 Twitter Sentiment Analysis – CAS Hackathon Project
📌 Project Overview

This project is a Twitter Sentiment Analysis Web Application developed as part of a CAS Hackathon. The system analyzes tweets from a CSV dataset and classifies them into Positive, Negative, or Neutral sentiments using Natural Language Processing (NLP) techniques.

The application is built using Flask (Python) for the backend and HTML, CSS, JavaScript for the frontend. Users can upload a CSV file containing tweets, and the system processes the data to generate sentiment predictions along with graphical visualizations.

This project demonstrates the practical implementation of AI-based sentiment analysis for social media analytics and brand monitoring.

🎯 Objective

To classify tweets into sentiment categories.

To analyze large tweet datasets efficiently.

To visualize sentiment distribution using graphs.

To build a simple and interactive web application for sentiment analysis.

🧠 Working Process

User uploads a CSV file containing tweets.

The system reads the dataset using Pandas.

Text preprocessing is performed:

Removal of URLs, special characters

Lowercase conversion

Text cleaning

Sentiment analysis is performed using a pre-trained NLP sentiment model.

Tweets are classified as:

Positive

Negative

Neutral

Sentiment distribution percentages are calculated.

Graphical visualization is generated using Matplotlib/Plotly.

Results are displayed on the result page.

🛠️ Technologies Used
🔹 Backend

Python

Flask

🔹 Frontend

HTML

CSS

JavaScript

🔹 Libraries

Pandas

NumPy

Matplotlib

Plotly

NLP Sentiment Analyzer (VADER / Pre-trained model)

📁 Project Structure
twitter-sentiment-analysis/
│
├── static/            # CSS, JavaScript, and static assets
├── templates/         # HTML templates (index, result pages)
├── uploads/           # Uploaded CSV files storage
├── app.py             # Main Flask application
└── README.md          # Project documentation

🚀 Features

✅ Upload CSV dataset of tweets
✅ Automatic sentiment classification
✅ Positive / Negative / Neutral prediction
✅ Sentiment percentage calculation
✅ Graphical visualization of results
✅ Clean and interactive web interface

#🖥️ How to Run the Project
###1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/twitter-sentiment-analysis.git
```

###2️⃣ Navigate to the project folder
```bash
cd twitter-sentiment-analysis
```

###3️⃣ Install required dependencies
```bash
pip install flask pandas numpy matplotlib plotly vaderSentiment
```

###4️⃣ Run the Flask application
```bash
python app.py
```

###5️⃣ Open in browser
```bash
http://127.0.0.1:5000/
```

📊 Output

The system provides:

Total number of tweets analyzed

Count of Positive, Negative, Neutral tweets

Sentiment distribution percentage

Graphical representation using charts

🔬 Applications

Brand monitoring

Social media analytics

Customer feedback analysis

Market research

Academic research projects
