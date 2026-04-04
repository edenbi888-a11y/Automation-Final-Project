
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=Playwright&logoColor=white)
![Appium](https://img.shields.io/badge/Appium-662d91?style=for-the-badge&logo=appium&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

# Atid Expense Automation Framework 

## Overview
This is a comprehensive End-to-End Automation project designed for an **Expense Tracker** application. The framework demonstrates advanced automation capabilities across multiple platforms, ensuring high quality and data integrity from the UI down to the Database.

The project is built using the **Page Object Model (POM)** design pattern, emphasizing maintainability, scalability, and clean code principles.

---

## 🛠 Technologies & Tools
* **Language:** Python 🐍
* **Web Automation:** Playwright 🎭
* **Mobile Automation:** Appium 📱
* **API Testing:** Playwright APIRequestContext (Integration with Chuck Norris API)
* **Test Runner:** Pytest
* **Database:** SQLite 🗄️
* **Reporting:** Allure Reports 📊
* **AI Integration:** Google GenAI for intelligent test assistance

---

## 🏗 Project Architecture
The framework is organized into logical layers to separate concerns:

* `page_objects/`: Implementation of the POM pattern for Web and Mobile platforms.
* `workflows/`: Complex business flows that combine multiple actions into reusable scenarios.
* `extensions/`: Custom helper classes for platform-specific Actions and Verifications.
* `utils/`: General utilities including config loaders, CSV handlers, and AI integrations.
* `data/`: Management of test data (CSV, JSON, SQL scripts).
* `tests/`: The test suite, categorized by Web, API, and Mobile.

> **Note:** ![Architecture Diagram](image.png)

---

##  Key Features
* **Data-Driven Testing (DDT):** Running test iterations based on external CSV files for maximum coverage.
* **Soft Assertions:** Using soft checks to allow tests to continue even if a minor verification fails.
* **DB Verifications:** Direct SQL queries against the SQLite database to validate UI-driven data persistence.
* **Mobile Persistence:** Testing app behavior and state stability after backgrounding/resuming.
* **Auto-Healing & Debugging:** Automatic screenshots on failure and detailed Trace files for rapid debugging.
*Web Automation: Robust UI testing using Playwright with a focus on synchronization and stability.
*API Validation: Testing RESTful services to ensure seamless data flow and correct status codes.

---

## 💻 Setup & Execution

### 1. Environment Setup
Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

 ## 💡 Challenges & Solutions
The framework was built with a focus on scalability and reusability. By using a centralized configuration and custom utility classes, I reduced code duplication and improved the stability of the automation suite. Implementing a cross-platform  strategy (Web + Mobile) required a deep understanding of synchronization and       environment management.