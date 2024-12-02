# Webhook Integration Project - "Hello World Webhook"

--- 

  ## Project Description
This project demonstrates how to implement a simple webhook server using Python and Flask. The server listens for POST requests at the /webhook endpoint and processes the incoming data. For this example, the server simply prints the received data and responds with a confirmation message.

  ## Motivation
The motivation behind this project is to create a simple and practical webhook server that can receive real-time data and process it. Webhooks are commonly used for integrating systems, triggering actions, and automating tasks. This project serves as an introductory example to understand how webhooks work.

  ## Problem Solved
This project helps to automate the handling of incoming data from external systems. It is an easy way to integrate with other services that support webhooks, and allows real-time communication without requiring manual intervention or constant polling.

  ## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

--- 

## Installation
 ### Requirements
Before running the project, make sure you have the following installed:

- Python 3.x
- Flask:

Steps
  ### Clone the repository to your local machine:
 ```
git clone https://github.com/SebastianPE0/Python_Webhook.git
 ```
Navigate to the project directory:
 ```
cd Webhook-Integration
 ```
  ### Install Flask:

 ```
pip install flask
 ```
  ### Run the application:

 ```
python app.py
 ```
This will start the Flask server locally, listening on http://localhost:5000.

---

## Usage
Once the server is running, you can send POST requests to the /webhook endpoint. Here’s an example of how to do that using curl:

 ```
{
    "event": "test_event",
    "message": "message",
    "payload": "some_data"
}
 ```
This will trigger the webhook, and you should see the following response:

 ```
{
    "message": "Hello_World",
    "received_data": {
        "event": "test_event",
        "message": "message",
        "payload": "some_data"
    },
    "status": "received"
}
 ```
---
