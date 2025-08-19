# Fraud Detection Using Logistic Regression  

## 📌 Project Overview  
This project focuses on detecting fraudulent transactions using **Logistic Regression**.  
We built a machine learning pipeline that preprocesses the data, selects important features, and trains a classification model to identify fraudulent activities.  

---

## 🔍 Data & Feature Selection  
After performing **Exploratory Data Analysis (EDA):**  
- **Type variable**: Identified as a key indicator of fraudulent transactions.  
- **Step (time feature)**: Dropped, since it showed no significant relation to fraud occurrence.  
- **Amount & balance-related features**: Retained as they capture transaction flow and play an important role in fraud detection.  

---

## ⚙️ Model Development  
We used a **Logistic Regression model built within a Scikit-learn pipeline** for streamlined preprocessing and training.  
- The pipeline ensured consistent data transformations.  
- Logistic regression was chosen for its interpretability and ability to handle binary classification problems.  

---

## 📊 Model Evaluation  
We demonstrated the performance of the model using the following tools:  
- **Confusion Matrix** → To evaluate true/false positives and negatives.  
- **Classification Report** → Precision, Recall, and F1-score analysis.  
- **Pipeline Score** → Overall accuracy of the model.  

---

## 🔑 Key Factors Predicting Fraud  
The most important factors that influenced fraudulent transaction detection were:  
- **Transaction Type** (e.g., CASH_OUT, TRANSFER)  
- **Transaction Amount**  
- **Balance-related features** (old and new balances before/after transaction)  

✅ These make sense as fraud patterns are often hidden in the **type and flow of money** rather than in time-based patterns.  

---

## 🛡️ Fraud Prevention Recommendations  
To minimize fraud risks, companies should adopt the following measures when updating their infrastructure:  
- Strengthen **real-time monitoring systems** for transactions.  
- Implement **multi-factor authentication** for sensitive operations.  
- Use **behavioral analytics** to flag unusual customer activity.  
- Regularly **update fraud detection models** to adapt to evolving fraud strategies.  

---

## 📈 Measuring Effectiveness  
After implementing preventive measures, effectiveness can be evaluated by:  
- Tracking the **rate of fraudulent transactions** over time.  
- Monitoring **false positives and false negatives** in fraud detection.  
- Measuring **financial losses prevented** and reduction in chargebacks.  
- Conducting **periodic security audits and penetration tests**.  

---

## 🚀 Conclusion  
This project shows that Logistic Regression, though simple, can effectively detect fraud when combined with proper **feature selection, preprocessing, and evaluation tools**.  
With preventive measures in place and continuous monitoring, organizations can significantly reduce fraudulent activities.  

---
