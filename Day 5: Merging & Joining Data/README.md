# **Day 5: Customer & Order Data Integration Project** 🚀  

## **📌 Project Overview**  
In this project, I merged and joined multiple datasets to create a **unified view of customer orders and transactions**. This process involved different types of joins, concatenation, and time-based merging techniques to enhance customer behavior analysis.  

## **🎯 Objectives**  
✅ Combine **customer and order data** using various join techniques.  
✅ Identify **customers who have never placed an order**.  
✅ Detect **orders with missing customer information**.  
✅ Use `.concat()` to **stack new customer and order records**.  
✅ Use **time-based merging (`merge_asof()`)** to link payments to orders.  
✅ Handle **duplicates and missing values after merging**.  

---

## **📂 Dataset Details**  

### **1️⃣ Customers Dataset (`customers.csv`)**  
This dataset contains customer details:  
- **Customer_ID** – Unique customer identifier  
- **Name** – Customer name  
- **Email** – Contact email  
- **Join_Date** – Date the customer registered  
- **Location** – Customer’s city  
- **Membership_Level** – Standard, Silver, Gold, Platinum  

### **2️⃣ Orders Dataset (`orders.csv`)**  
This dataset contains order transactions:  
- **Order_ID** – Unique order ID  
- **Customer_ID** – Links the order to a customer  
- **Order_Date** – Date the order was placed  
- **Product_Name** – Name of the product purchased  
- **Category** – Product category  
- **Quantity** – Number of items purchased  
- **Unit_Price ($)** – Price per unit  
- **Total_Amount ($)** – Total transaction amount  

---

## **🛠 Key Merging & Joining Tasks**  

**1️⃣ Basic Merging & Joining**  
**2️⃣ Advanced Merging with Multiple Keys**  
**3️⃣ Using `.concat()` for Stacking Data**  
**4️⃣ Using `merge_asof()` for Time-Based Merging**  
**5️⃣ Handling Duplicates & Missing Values After Merging** 
 

---

## **📜 Files in This Project**  
📄 `sales_data_merging.py` – Python script for all merging operations.  
📊 `customers.csv` – Original customers dataset.  
📊 `orders.csv` – Original orders dataset.  
📊 `merged_customer_orders.csv` – Final merged dataset.  
📄 `README.md` – Project documentation.  

---

## **⚡ Technologies Used**  
- Python 🐍  
- Pandas 📊  
- Merging & Joining Data  
- Time-Based Merging with `merge_asof()`  

---

### **🚀 Next Step: Day 6 – Data Reshaping!**  
