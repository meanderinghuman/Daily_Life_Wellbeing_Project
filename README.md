# Wellbeing Prediction Web App

This project presents a machine learning-based web application that predicts an individual's wellbeing status based on various demographic and lifestyle inputs. It integrates data preprocessing, a trained machine learning model, and a web interface built with Flask.

---

## 🔍 Project Structure

```
├── balanced_diverse_wellbeing_dataset.xlsx  # Dataset used for training/testing
├── main.ipynb                              # Jupyter Notebook with data exploration and model training
├── UI images/                              # Screenshots of the user interface
├── complete/
│   ├── app.py                              # Flask web app code
│   ├── model.pkl                           # Trained ML model
│   ├── label_encoder.pkl                   # Label encoder for categorical variables
│   ├── onehot_encoder.pkl                  # One-hot encoder for input transformation
│   ├── static/
│   │   └── style.css                       # CSS styling
│   └── templates/
│       └── index.html                      # HTML frontend template
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wellbeing-predictor.git
cd wellbeing-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Web App

```bash
cd complete
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📊 Dataset

The dataset `balanced_diverse_wellbeing_dataset.xlsx` contains anonymized survey data with features such as:

- Age, Gender
- Employment Status
- Health-related habits
- Wellbeing indicators

---

## 🧠 Model

The model was trained using scikit-learn and includes:

- Feature encoding (`label_encoder.pkl`, `onehot_encoder.pkl`)
- A trained ML model (`model.pkl`)

All components are integrated into the Flask app for real-time predictions.

---

## 🌐 User Interface

Screenshots of the app UI are available in the `UI images/` folder.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Developed as part of a Data Mining and Warehousing Course (IT3240) at Manipal University Jaipur .
- Dataset curated by Siddharth Pal , Siddhant Jaiswal , Mohammad Faraz Alam and Raahim Arora .
