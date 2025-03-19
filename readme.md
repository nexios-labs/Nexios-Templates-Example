# Nexios API Templates

## Overview
This repository contains multiple **Nexios API templates**, ranging from minimal setups to full-stack implementations. These templates provide a structured foundation for building scalable web applications using the Nexios framework.

## Available Templates

### 🏗️ FullStack Nexios API Template
A template designed for full-stack development with a frontend, database integration, and structured backend logic.

[![Download FullStack](https://img.shields.io/badge/Download-FullStack-blue?style=for-the-badge)](https://downgit.github.io/#/home?url=https://github.com/nexios-labs/Nexios-Templates-Example/tree/master/FullStack)


**Structure:**
```
FullStackNexios/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── main.py
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
├── templates/
│   ├── base.html
│   ├── index.html
├── .gitignore
├── README.md
├── requirements.txt
├── .env
```

### 🏢 Large-Scale Nexios API Template
For enterprise applications, this template includes modules for configuration, models, schemas, and core functionality.

[![Download LargeScale](https://img.shields.io/badge/Download-LargeScale-green?style=for-the-badge)](https://downgit.github.io/#/home?url=https://github.com/nexios-labs/Nexios-Templates-Example/tree/master/LargeScale)


**Structure:**
```
LargeScaleNexios/
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   ├── schemas/
│   │   ├── __init__.py
│   ├── main.py
├── .gitignore
├── README.md
├── requirements.txt
├── .env
```

### 🏗️ Microservices Nexios API Template
A microservices-based architecture for Nexios, with separate services for authentication, users, and payments, along with a gateway.

[![Download Microservices](https://img.shields.io/badge/Download-Microservices-orange?style=for-the-badge)](https://downgit.github.io/#/home?url=https://github.com/nexios-labs/Nexios-Templates-Example/tree/master/Microservices)


**Structure:**
```
MicroservicesNexios/
├── services/
│   ├── auth_service/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   ├── user_service/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   ├── payment_service/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
├── gateway/
│   ├── __init__.py
├── .gitignore
├── README.md
├── requirements.txt
├── docker-compose.yml
├── .env
```

### 🔹 Minimal Nexios API Template
A barebones Nexios API setup with the essential files to get started.

[![Download Minimal](https://img.shields.io/badge/Download-Minimal-purple?style=for-the-badge)](https://downgit.github.io/#/home?url=https://github.com/nexios-labs/Nexios-Templates-Example/tree/master/Minimal)


**Structure:**
```
MinimalNexios/
├── app/
│   ├── __init__.py
│   ├── main.py
├── .gitignore
├── README.md
├── requirements.txt
├── .env
```

### 📌 Standard Nexios API Template
A more structured Nexios template with additional configurations, database setup, and environment management.

[![Download Standard](https://img.shields.io/badge/Download-Standard-red?style=for-the-badge)](https://downgit.github.io/#/home?url=https://github.com/nexios-labs/Nexios-Templates-Example/tree/master/Standard)


**Structure:**
```
StandardNexios/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── main.py
├── .gitignore
├── README.md
├── requirements.txt
├── .env
```

---

## Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/nexios-api-templates.git
cd nexios-api-templates
```

### 2. Choose a Template
Navigate into the desired template directory and set up the environment.
```bash
cd FullStackNexios  # Example
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```

### 5. View Nexios in Action
Once the server is running, visit the following URL in your browser to see Nexios at work:
```
http://localhost:8000/nexios
```

## Contributing
Contributions are welcome! Fork the repo, create a new branch, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

## Author
**Dunamis** - [TechwithDunamis](https://github.com/TechWithDunamis)

