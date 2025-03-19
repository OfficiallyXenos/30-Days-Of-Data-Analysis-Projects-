# **Day 3: Customer Data Transformation Project** 🚀  

## **📌 Project Overview**  
In this project, I worked on **transforming raw customer transaction data** to improve data quality and create new insights. This involved renaming columns, handling missing values, creating new calculated fields, applying transformations using `.apply()` and `lambda`, and reshaping data using `.melt()`, `.pivot()`, `.stack()`, and `.unstack()`.  

## **🎯 Objectives**  
✅ Standardize and clean raw transaction data.  
✅ Create meaningful new features for better analysis.  
✅ Apply advanced transformations to improve data structure.  
✅ Use `.apply()` and `lambda` functions for efficient modifications.  
✅ Reshape data using pivot tables and melting techniques.  

---

## **📂 Dataset Details**  
The dataset contains **5,000 transactions** with the following columns:  

- **Transaction_ID** – Unique ID for each transaction  
- **Customer_ID** – Unique customer identifier  
- **Product_Category** – Category of the purchased product  
- **Product_Name** – Name of the purchased product  
- **Quantity** – Number of items purchased  
- **Unit_Price ($)** – Price per unit  
- **Total_Price ($)** – Total revenue for that transaction (some values are missing)  
- **Purchase_Date** – Date of the transaction (some formats are inconsistent)  
- **Payment_Method** – Payment type (some inconsistencies in naming)  
- **Discount Applied (%)** – Discount applied (some values are missing or incorrectly formatted)  

---

## **🛠 Key Tasks & Transformations**  

### **1️⃣ Column Renaming & Restructuring**  
✔ Standardized all column names to **snake_case**.  
✔ Removed unnecessary symbols (like `$`, `%`) from column names.  
✔ Reordered columns for better readability.  

### **2️⃣ Creating & Modifying Columns**  
✔ Filled missing **Total_Price** by calculating `Quantity × Unit_Price`.  
✔ Replaced missing **Discount_Applied** with `0%`.  
✔ Created a **Final_Price** column after applying discounts.  
✔ Extracted **year and month** from **Purchase_Date**.  

### **3️⃣ Using `.apply()` & `lambda` Functions**  
✔ Created a **Purchase_Type** column: `"Bulk"` vs. `"Single Item"`.  
✔ Categorized **Unit_Price** into `"Low"`, `"Medium"`, `"High"`.  
✔ Standardized **Product_Category** formatting.  
✔ Converted **Discount_Applied** to numeric values.  
✔ Flagged high-value transactions using a custom function.  

### **4️⃣ Reshaping Data (Pivot, Melt, Stack, Unstack)**  
✔ Used `.melt()` to reshape data from **wide to long format**.  
✔ Used `.pivot_table()` to analyze **Total Sales per Customer_ID**.  
✔ Applied `.stack()` and `.unstack()` to restructure multi-index data.  
✔ Created a **summary table** for **average final price per product category**.  

### **5️⃣ Handling Duplicate & Missing Data**  
✔ Checked and removed duplicate transactions.  
✔ Ensured **Customer_ID** was unique per transaction.  
✔ Standardized **Payment_Method** formatting.  
✔ Converted **Purchase_Date** to proper datetime format.  
✔ Dropped unnecessary columns after transformations.  

---


## **📜 Files in This Project**  
📄 `customer_data_transformation_project.py` – Python script for all transformations.  
📊 `customer_transactions.csv` – Raw dataset used in this project.  
📊 `transformed_customer_data.csv` – Final cleaned and structured dataset.  
📄 `README.md` – Project documentation.  

---

## **⚡ Technologies Used**  
- Python 🐍  
- Pandas 📊  
- NumPy 🔢  
- Data Transformation & Feature Engineering  

---

