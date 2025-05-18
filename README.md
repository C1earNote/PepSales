# Notification Service - PepSales

I hope this gives a brief description: This project is a simple **Notification Service** built with **FastAPI**, **RabbitMQ**, and **PostgreSQL**. It supports queuing and sending of email, SMS, and in-app notifications through a unified API.

---

## Features

- REST API for sending notifications
- Queuing via RabbitMQ for reliable message delivery
- PostgreSQL for storing in-app notifications
- Easily extensible to add other notification types
- Simple HTML frontend for manual testing
- CORS enabled for frontend-backend communication

---

## Tech Stack

- **FastAPI** – Backend REST framework
- **RabbitMQ** – Queue for async notification handling
- **PostgreSQL** – Database for in-app notifications
- **SQLAlchemy** – ORM for database operations
- **HTML/CSS** – Basic frontend to test API

---

## How to Test

### 1. **Run RabbitMQ and PostgreSQL**

Make sure RabbitMQ and PostgreSQL are running on your system. Adjust connection strings if needed.

### 2. **Install Python dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Start the FastAPI backend**

```
uvicorn app.main:app --reload
```

API is available at: http://localhost:8000/docs

### 4. **Run the consumer in another terminal**

```
python app/worker.py
```

This listens to queue and sends notifications

### 5. **Open the frontend**

Just double click on index.html (Open it in your browser)


## Sample Payload

```
{
  "type": "email",
  "recipient": "user@example.com",
  "content": "Hello from your Notification Service!"
}
```

## API Endpoint
POST/send-notification
Sends a notification by publishing to the queue.

## Configuration
Make sure to set the correct credentials in:
- app/database.py → PostgreSQL
- app/producer.py and consumer.py → RabbitMQ

# Done by Tanishq Nigam
