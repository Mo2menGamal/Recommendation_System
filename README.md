# 💍 Wedding Venue Recommender System

This project is a machine learning–based recommendation system built for _Wedding Planner_, a wedding event management platform.  
The system recommends similar venues based on one or more previously viewed venues — for both single venue views and personalized homepage feeds.

---

## 🚀 Features

- Recommends similar venues using TF-IDF + cosine similarity
- Supports Arabic venue names, tags, and descriptions
- Fast and lightweight — no database required
- RESTful API using Flask
- JSON output ready for frontend use
- Personalized results with support for multiple venue IDs
- Weighted scoring: most recently viewed venues have more influence

---

## 🎯 Supported Use Cases

### 1. 📺 YouTube-Style Recommendations (Single Venue)

When a user views a specific venue, the system recommends similar venues based only on that one.  
**API Call:**

```bash
GET /recommend?id=7
```

Use this on the **Venue Details Page** — just like YouTube suggests related videos while watching.

---

### 2. 🏠 Home Page Recommendations (Multiple Venues)

When a user lands on the homepage, the system suggests venues based on the **last 2–3 venues** they viewed.  
The most recent venue has the most weight, making results feel personalized and relevant.<br>
**API Call:**

```bash
GET /recommend?ids=7,10,14
```

---

## 📁 Folder Structure

wedding_recommender/
\
│
\
├── venues.csv # Original dataset
\
├── build_recommender.py # Builds similarity matrix +
features
\
├── processed_venues.csv # Cleaned data with extracted
features
\
├── similarity_matrix.pkl # Precomputed similarity scores
\
├── api.py # Flask API for recommendations
\
├── requirements.txt # Python dependencies
\
└── README.md # You're here!

---

## 🧪 How to Use

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. (Optional) Rebuild the Model

If you modify the venues.csv, rerun this:

```bash
python build_recommender.py
```

### 3. Start the API

```bash
python api.py
```

### 4. Make a Request

Examples:

- Single venue (for details page):

```bash
GET http://localhost:5000/recommend?id=2&n=5&same_city=true
```

- Multi-venue history (for homepage feed):

```bash
GET http://localhost:5000/recommend?ids=3,7,10&n=5&same_city=true
```

| Query Param | Description                                   |
| ----------- | --------------------------------------------- |
| `id/ids`    | ID/index of the venue(s) in the CSV           |
| `n`         | Number of recommendations to return           |
| `same_city` | If `true`, only shows venues in the same city |

## 📦 Example Output

```
[
  {
    "id": 5,
    "name": "\"Royal Hall\"",
    "location": "Alexandria",
    "tags": [
      "Royal",
      "Gold",
      "Traditional",
      "Ballroom",
      "Ornate"
    ],
    "type": [
      "Hall"
    ],
    "score": 0.42
  },
  {
    "id": 10,
    "name": "\"Royal Palace Hall\"",
    "location": "Alexandria",
    "tags": [
      "Modern",
      "Ballroom",
      "Spacious",
      "Ambient",
      "Gold",
      "Ornate",
      "Traditional"
    ],
    "type": [
      "Hall"
    ],
    "score": 0.37
  },
  {
    "id": 9,
    "name": "\"قصر الأميرات\"",
    "location": "Alexandria",
    "tags": [
      "Modern",
      "Ballroom",
      "Spacious",
      "Ambient",
      "Gold",
      "Ornate"
    ],
    "type": [
      "Hall"
    ],
    "score": 0.19
  },
  {
    "id": 0,
    "name": "\"Grand Sea Rena\"",
    "location": "Alexandria",
    "tags": [
      "Elegant",
      "Spacious",
      "Ballroom",
      "Grand",
      "Chandeliers",
      "Lighting"
    ],
    "type": [
      "Hall"
    ],
    "score": 0.0
  },
  {
    "id": 1,
    "name": "\"قاعات حفلات الفتح بلازا\"",
    "location": "Alexandria",
    "tags": [
      "Luxurious",
      "Elegant",
      "Spacious",
      "Formal",
      "Glamorous",
      "Chandeliers"
    ],
    "type": [
      "Hall"
    ],
    "score": 0.0
  }
]
```

## 🛠 Technologies Used

- Python
- Flask
- Pandas
- scikit-learn (TF-IDF, cosine similarity)

## 👷‍♂️ Built by Team "The Hammers" 🔨

# Machine Learning Engineer:

- _Mo'men Gamal Ayaad_

# Team Members:

- _Mrwan Ahmed Gaber_

- _Abd El-Rahman Essam Morsy_

- _Ahmed Youssef Mohamed_

- _Ibrahim Ragab Ibrahim_

- _Abd El-Salam Mohamed Abd El-Salam_

- _Hossam Hassan Shoiep_

- _Abd El-Rahman Mohamed El-Sayed_

- _Atef El-Sayed Mohamed_

- _Ahmed Mohamed Osman_

## 📝 License

Free to use, modify, and extend — just give credit if it helps your project
<br>
<br>
_*This project was built as part of the graduation requirements for the Computer Science Class of 2025.*_
