## 🧠 Problem Statement

Many people live far away from their families, especially parents, and often worry about reminding them of important daily tasks such as:

- Taking medicines on time  
- Attending medical checkups  
- Following daily routines  

At the same time, people also forget to send timely messages like wishes or reminders to their loved ones due to busy schedules.

Manual reminders are not always reliable, and missing such moments can be important both for **health and relationships**.

---

## 💡 Solution

This project provides an automated WhatsApp reminder system that allows users to:

- Send scheduled messages to loved ones  
- Remind parents about medicines and routines  
- Automate daily or important notifications  
- Ensure timely communication without manual effort  

Users can customize messages as per their needs and use this system for both **personal care and productivity**.

---

## ✨ Features

- 📩 Automated WhatsApp message scheduling  
- 📊 Excel-based input system  
- 🔁 Retry mechanism for failed messages  
- 🧾 Persistent logging using SQLite  
- 📜 Log viewer for message history  
- ⚡ Simple and lightweight  
- Every time you run this you simply just update the excel sheet and DB file also update according to that when you run 

---

## 🛠️ Tech Stack

- Python  
- pywhatkit  
- pandas  
- SQLite  
- Excel  

---

## ⚙️ Prerequisites

Make sure your system has:

- Python 3.7 or above  
- Google Chrome installed  
- Active internet connection  
- WhatsApp Web logged in  
- you should enter your contact details in excel file and give correct path to code for your excel file or simply you can save your excel file in same folder
- you should download these pywhatkit, pandas, openpyxl, using pip

---
## 📋 Usage Instructions
- 📩 Sending Messages
- Add contacts and messages in Excel
- Run the scheduler
- Messages will be sent automatically at scheduled time
---

## 🔁 Retry Mechanism
- If message fails → system retries automatically
- Retry count is tracked in database
- 📜 Logging
- Every message attempt is stored in messages.db
- Includes success/failure status and timestamps
---
## ✅ Advantages
- ⏰ Fully automated reminder system
- 📉 Reduces manual effort
- 🔁 Retry mechanism improves reliability
- 🧾 Persistent logging for tracking
- 💻 Easy to use and modify
---
## ⚠️ Limitations & Learning Scope


- This project is built as part of my learning journey.

- Requires WhatsApp Web (no official API used)
- Browser must remain open during execution
- Limited control over message delivery status
- Depends on system timing and internet
---
## 🔮 Future Improvements
- Add GUI interface
- Integrate official WhatsApp API
- Add notification system
- Improve retry logic with scheduling
- Deploy as background service
---
##💡 Use Cases
- Medicine reminders
- Appointment reminders
- Daily task alerts
- Personal productivity tools
---
## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/whatsapp-reminder-system.git
cd whatsapp-reminder-system