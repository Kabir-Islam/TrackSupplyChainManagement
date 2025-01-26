# TrackSupplyChainManagement
## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
   - [Supplier Management](#supplier-management)
   - [Shipment Tracking](#shipment-tracking)
   - [Data Analysis](#data-analysis)
3. [Technology Stack](#technology-stack)
4. [Project Files and Structure](#project-files-and-structure)
5. [Application Screenshots](#application-screenshots)
6. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Steps to Run the Application](#steps-to-run-the-application)
7. [How to Use](#how-to-use)
   - [Supplier Management](#supplier-management-1)
   - [Shipment Tracking](#shipment-tracking-1)
   - [Analyze Data](#analyze-data)
8. [Future Enhancements](#future-enhancements)
9. [Contributions](#contributions)
10. [Contact](#contact)

## **📜 Overview**

The TrackSupplyChainManagement is a Python-based project designed to manage suppliers, track shipments, and analyze data in a streamlined and efficient way. This application helps businesses monitor their supply chain and improve decision-making by offering essential tools for supply chain operations.

## **🚀 Features**
Supplier Management:
Add and update supplier information (e.g., name, contact details, address).
View a list of suppliers associated with specific items.
Shipment Tracking:
Record details of new shipments, including status and delivery dates.
Update shipment statuses to "In Transit" or "Delivered."
Data Analysis:
Generate reports for delayed shipments.
Summarize shipments by suppliers to evaluate performance.
Identify top suppliers based on total items supplied.
## 🛠️ Technology Stack
Python for backend processing and operations.
SQLite for database management.
Pandas for handling and processing CSV data.
Datetime for date and time calculations.

## **📂 Project Files and Structure**
|-- SPM.csv                 # Input data file containing supplier and shipment details
|-- supplier_shipment_management.db  # SQLite database storing supplier and shipment records
|-- main.py                 # Python script containing the full project code
|-- README.md               # Documentation for the project


## **🖥️ Application Screenshots**
![image](https://github.com/user-attachments/assets/7bf8c0cf-085e-485b-a273-c8ac49b813bc)
![image](https://github.com/user-attachments/assets/3acbe545-366e-44b6-a516-208ad17c9f05)
![image](https://github.com/user-attachments/assets/25175f67-6f06-49fe-9b83-c8bf62caf1d0)
![image](https://github.com/user-attachments/assets/916d4cc8-b3f8-482b-9c93-633980c5dc9d)

## **🚀 Getting Started**
Prerequisites
Install Python (version 3.7 or higher).
Install pandas library using:
bash
CopyEdit
pip install pandas


Steps to Run the Application
Clone the repository or download the project files.
Ensure the CSV file (SPM.csv) is in the project directory.
Run the Python script using:
bash
CopyEdit
python main.py


Follow the menu-based options to manage suppliers, shipments, and analyze data.

## **📝 How to Use**
Supplier Management:
Add new suppliers by entering their details.
Update supplier information like contact number or address.
View suppliers linked to specific items by entering the item ID.
Shipment Tracking:
Record shipment details, including the item name, quantity, and shipment status.
Update the status of shipments as "Delivered" once they arrive.
Analyze Data:
View reports of delayed shipments to identify and resolve issues.
Summarize shipments by supplier to monitor activity levels.
Identify the top-performing suppliers based on total items supplied.

## **💡 Future Enhancements**
Implement a web-based interface for user interaction.
Add real-time notifications for delayed shipments.
Include detailed graphs and charts for data analysis.

## **🤝 Contributions**
We welcome contributions to improve this project. Feel free to fork the repository, create new features, and submit pull requests.

## **📧 Contact**
For any questions or suggestions, please reach out:
##### Developer: Kabirul Islam
##### Email: kabir200123@gmail.com 
##### GitHub: https://github.com/Kabir-Islam

