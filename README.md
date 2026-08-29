# fake-news-detection
fake-news-detection
# 📰 Fake News Detection using Machine Learning

A web-based **Fake News Detection System** built using **Django**, **Machine Learning**, **TF-IDF Vectorization**, and **Logistic Regression**.

Users can paste a news article into the application, and the trained machine learning model predicts whether the news is likely **Fake** or **Real**.

---

## 🚀 Features

* 📰 Paste any news article into the text area
* 🤖 Machine Learning-based prediction
* ❌ Detect Fake News
* ✅ Detect Real News
* 📊 Display model confidence
* 🧹 Clear text functionality
* 🧪 Interactive Fake and Real sample articles
* 🎨 Responsive and user-friendly interface

---

## 🛠️ Technologies Used

* Python
* Django
* Scikit-learn
* Pandas
* TF-IDF Vectorizer
* Logistic Regression
* HTML
* CSS
* JavaScript

---

## 🧠 Machine Learning Workflow

```text
News Article
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
Logistic Regression Model
      ↓
Fake News ❌ / Real News ✅
```

---

## 📊 Dataset

The model was trained using the **Fake and Real News Dataset**.

The dataset contains:

* Fake News articles
* Real News articles
* Title
* News text
* Subject
* Date

### Labels

| Label | Meaning     |
| ----- | ----------- |
| 0     | Fake News ❌ |
| 1     | Real News ✅ |

---

## 🤖 Model Training

The following steps were used to train the model:

1. Import Fake and Real News datasets
2. Add labels to both datasets
3. Combine the datasets
4. Shuffle the data
5. Combine title and text into a content column
6. Split the dataset into training and testing data
7. Apply TF-IDF Vectorization
8. Train Logistic Regression
9. Evaluate model performance

---

## 📈 Model Performance

The model achieved approximately:

**Accuracy: 98.56%**

> Note: The accuracy was measured using the test split from the dataset. Predictions on completely new real-world articles may vary.

---

## 📁 Project Structure

```text
fake_news_project/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── detector/
│   ├── templates/
│   │   └── home.html
│   │
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── apps.py
│
├── model/
│   ├── fake_news_model.pkl
│   └── vectorizer.pkl
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/fake-news-detection.git
```

### 2. Move into the Project Directory

```bash
cd fake-news-detection
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Run the Django server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 💻 How to Use

1. Open the website.
2. Paste a news article into the text area.
3. Click **Check News**.
4. The machine learning model analyzes the text.
5. The application displays:

```text
FAKE NEWS ❌
```

or

```text
REAL NEWS ✅
```

along with the model confidence score.

---

## ⚠️ Disclaimer

This project uses a machine learning model trained on a specific dataset.

The prediction is based on patterns learned from the training data and should **not be considered a professional fact-checking system**. A prediction of "Fake" or "Real" does not guarantee the factual accuracy of a real-world article.

---

## 🔮 Future Improvements

* Add BERT or DistilBERT for comparison
* Add prediction history
* Add user authentication
* Add news source verification
* Integrate fact-checking APIs
* Deploy the application online
* Improve the UI and user experience
* Support multiple languages

---

## 👨‍💻 Author

**Jabir Hussain**

MCA(AI&IOT) NIT PATNA

---

⭐ If you found this project useful, consider giving the repository a star!
