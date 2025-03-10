# 🚀 LLM Chat Backend (FastAPI + MongoDB)

This is a **backend component** that facilitates interaction with **LLMs (OpenAI GPT-4o-mini)**. It provides:
- **CRUD operations** for conversations containing queries and responses.
- **LLM query handling** with conversation history as context.
- **Anonymized query storage** in MongoDB for auditing.
- **REST API with OpenAPI docs** for easy integration.

---

## **📌 Features**
✅ **FastAPI-based backend**  
✅ **MongoDB for conversation storage**  
✅ **Dockerized environment**  
✅ **CRUD endpoints for managing conversations**  
✅ **Send prompt queries & receive LLM responses**  
✅ **Automatic logging & anonymization of chat history**  
✅ **OpenAPI documentation for API usage**  

---

## **🛠 Tech Stack**
| Component  | Technology |
|------------|-----------|
| **Backend** | FastAPI (Python 3.10+) |
| **Database** | MongoDB (via Docker) |
| **ORM** | Beanie (MongoDB ODM) |
| **LLM API** | OpenAI Python Client |
| **Validation** | Pydantic |
| **Containerization** | Docker, Docker Compose |

---

## **🚀 Setup and Running the Application**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```
### **2️⃣ Configure Environment Variables**
Duplicate the `.env.example` file and name it `.env`.
It should look like the following:
```bash
MONGO_URI="mongodb://mongo:27017/launchpad_db"
OPENAI_API_KEY="INPUT YOUR OPENAI API KEY HERE"
```
Enter your OpenAI API Secret key as a string
✅ Notes:
- mongo is the service name inside Docker Compose.
- Do not use localhost inside Docker Compose (use mongo instead).

### **3️⃣ Run with Docker Compose**
To build and start both FastAPI & MongoDB, run:
```bash
docker-compose up -d --build
```
✅ Notes:
- d → Runs in detached mode (in the background).
- -build → Ensures FastAPI is rebuilt.

Check running containers:
```bash
docker ps
```

### **4️⃣ Verify MongoDB is Running**
To check if MongoDB is working inside the Docker container, enter:
```bash
docker exec -it mongodb mongosh
```
Then, inside MongoDB shell:
```js
show dbs  # List databases
use launchpad_db  # Switch to project database
show collections  # Show collections
```

### **5️⃣ Access the FastAPI Application**
If the two containers are running correctly, you should be able to access:

API Documentation (Swagger UI): http://localhost:8000/docs

You can test the endpoints here. Enter the request body and view the response body. 

## **📌 API Endpoints**
The endpoints were created based off the openai.yaml file provided by the team.

### **1️⃣ Create a Conversation**
```http
POST /conversations/
```
Example Request Body:
```json
{
  "name": "My Conversation",
  "params": {
    "temperature": 0.7
  }
}
```
Example Response:
```json
{
  "id": "656a21fb3b3f76f3a2e6b1c3",
  "name": "My Conversation",
  "params": {"temperature": 0.7}
}
```

### **2️⃣ Get All Conversations**
```http
GET /conversations/
```
Example Response:
```json
[
  {
    "id": "656a21fb3b3f76f3a2e6b1c3",
    "name": "My Conversation",
    "params": {
      "temperature": 0.7
    }
  },
  {
    "id": "656a21fb3b3f76f3a2e6b1c4",
    "name": "Another Conversation",
    "params": {
      "temperature": 0.5
    }
  }
]
```
### **3️⃣ Get a Specific Conversation**
```http
GET /conversations/{conversation_id}
```
Example Response:
```json
{
  "id": "656a21fb3b3f76f3a2e6b1c3",
  "name": "My Conversation",
  "params": {
    "temperature": 0.7
  },
  "tokens": 100,
  "pinned": false,
  "prompts": [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi, how can I assist you?"}
  ],
  "modifications": {}
}
```
Error Response:
```json
{
  "detail": {
    "code": 404,
    "message": "Specified resource(s) was not found"
  }
}
```
### **4️⃣ Update a Conversation**
```http
PUT /conversations/{conversation_id}
```
Example Request Body:
```json
{
  "name": "Updated Conversation",
  "params": {
    "temperature": 0.9,
    "max_tokens": 200
  }
}
```
Example Response:
```json
{
  "id": "656a21fb3b3f76f3a2e6b1c3",
  "name": "Updated Conversation",
  "params": {
    "temperature": 0.9,
    "max_tokens": 200
  }
}
```
### **5️⃣ Delete a Conversation**
```http
DELETE /conversations/{conversation_id}
```

### **6️⃣ Send a Prompt to LLM**
```http
POST /conversations/{conversation_id}
```
Example Request Body:
```json
{
  "content": "Hello, how are you?"
}
```
Example Response:
```json
{
  "message": "I'm doing well, thank you!"
}
```
## **📌 Stopping & Managing Containers**
Stop the running contaainers
```bash
docker-compose down
```
Restart the application
```bash
docker-compose up -d
```

## **📌 Project Structure**

```plaintext
/your-repo
│── /app                 # FastAPI source code
│   ├── main.py          # FastAPI entry point
│   ├── models/          # Pydantic models
│   ├── routes/          # FastAPI endpoints
│   ├── config/          # MongoDB connection
│── Dockerfile           # FastAPI Docker setup
│── docker-compose.yml   # Docker Compose for MongoDB + FastAPI
│── requirements.txt     # Python dependencies
│── .env                 # Environment variables
|── .env.example         # Example of .env file
|── .gitignore           # Contains untracked file names
│── README.md            # This file
```
## **📌 Troubleshooting**
```bash
Error: Port 27017 is already allocated
```
Open docker terminal and enter this command to see the running containers:
```bash
docker ps
```
Check the name of the container that is running on Port 27017. 
```bash
docker stop <name of container>
```
Then restart by running
```bash
docker-compose up -d
```