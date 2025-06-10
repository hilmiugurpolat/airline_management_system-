#  Airline Management System

Welcome to the **Airline Management System**! This is a Django-based backend application designed to help airlines manage their aircraft, flights, and passenger reservations efficiently. Built with **Django REST Framework (DRF)**, this project provides a robust RESTful API for seamless interaction.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Setup Instructions](#setup-instructions)
4. [Running the Project](#running-the-project)
5. [API Endpoints](#api-endpoints)
6. [Postman Collection](#postman-collection)
7. [Postman API Testing Guide](#postman-api-testing-guide)



---

## Features
- **Airplane Management**: Add, update, delete, and view airplanes.
- **Flight Management**: Schedule, update, delete, and view flights.
- **Reservation Management**: Create, update, and view passenger reservations.
- **Flight Conflict Check**: Ensures no overlapping flights for the same airplane.
- **Occupancy Check**: Prevents overbooking by checking flight capacity.
- **Reservation Code Generation**: Automatically generates unique reservation codes.
- **Filtering**: Filter flights by departure, destination, and date.
- **Email Sending**: Sends confirmation emails to passengers upon reservation.

---

## Requirements
- Python 3.10+
- Django 4.0+
- Django REST Framework
- PostgreSQL (or any other database supported by Django)
- Postman (for API testing)

---

## Setup Instructions

### 1. Download the Project
- Download the project files as a ZIP archive and extract them to your desired location.

### 2. Set Up a Virtual Environment
- Open a terminal and navigate to the project directory.

- Create a virtual environment:
  ```bash
  virtualenv venv
  ```
- Activate the virtual environment:

  - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
  - On n Windows:
    ```bash
    venv\Scripts\activate
    ```

### 3. Install Dependencies

- Install the required Python packages:

  ```bash
  pip install -r requirements.txt
  ```
### 4 . Run Migrations

- Apply the database migrations:

  ```bash
  python manage.py migrate
  ```

## Running the Project
- Once the setup is complete, you can run the project locally.
### 1.  Start the Development Server
- Run the Django development server with the following command:

  ```bash
  python manage.py runserver
  ```


 
## API Endpoints
- The following are the available API endpoints for the system:
### 1. Airplane API
- GET /airplanes/: List all airplanes.
- GET /airplanes/{id}/: Get details of a specific airplane.
- GET /airplanes/{id}/flights: Get all flights for a specific airplane.
- POST /airplanes/: Add a new airplane.
- PATCH /airplanes/{id}/: Update a specific airplane.
- DELETE /airplanes/{id}/: Delete a specific airplane.
### 2. Flight API
- GET /flights/: List all flights.
- GET /flights/{id}/: Get details of a specific flight.
- GET /flights/{id}/reservations: Get reservations for a specific flight.
- POST /flights/: Add a new flight.
- PATCH /flights/{id}/: Update a specific flight.
- DELETE /flights/{id}/: Delete a specific flight.
### 3. Reservation API
- GET /reservations/: List all reservations.
- GET /reservations/{id}/: Get details of a specific reservation.
- POST /reservations/: Add a new reservation.
- PATCH /reservations/{id}/: Update a specific reservation


## Postman Collection
- The project includes a Postman collection with pre-configured requests for testing the API endpoints. This collection contains all the CRUD operations for the Airplane, Flight, and Reservation models.
- How to Use the Collection:

    - After importing the collection into Postman, you'll have predefined requests for the API endpoints.
    - Each request will be labeled according to the model it interacts with (e.g., Airplane, Flight, Reservation).
    - The requests are set up with the appropriate HTTP methods (GET, POST, PATCH, DELETE) and URL paths.
    - For each request, you will find descriptions of the expected input and output.



## Postman API Testing Guide

Below are the steps to test the **Airplane API**, **Flight API**, and **Reservation API** using **Postman**.


### Airplane API

#### 1. **GET /airplanes/**: List all airplanes
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/airplanes/`
- **Description**: Retrieves a list of all airplanes in the system.
- **Steps**:
  - Set the method to `GET`.
  - Enter the URL in Postman.
  - Click `Send`.

#### 2. **GET /airplanes/{id}/**: Get details of a specific airplane
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/airplanes/{id}/` (replace `{id}` with the airplane ID)
- **Description**: Retrieves details of a specific airplane by ID.
- **Steps**:
  - Set the method to `GET`.
  - Replace `{id}` with the airplane's ID.
  - Click `Send`.

#### 3. **GET /airplanes/{id}/flights**: Get the flights of a specific airplane
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/airplanes/{id}/flights` (replace `{id}` with the airplane ID)
- **Description**: Retrieves the flights associated with a specific airplane.
- **Steps**:
  - Set the method to `GET`.
  - Replace `{id}` with the airplane ID.
  - Click `Send`.

#### 4. **POST /airplanes/**: Add a new airplane
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/airplanes/`
- **Body** (JSON):
  ```json
  {
    "tail_number": "TC-NRT",
    "model": "Airbus A320",
    "capacity": 180,
    "production_year": 2015,
    "status": true
  }
- **Description**: Creates a new airplane record.
Description: Creates a new airplane record.
- **Steps**:
  - Set the method to `POST`.
  - Enter the URL in Postman.
  - Select Body, then choose raw and JSON format.
  - Paste the airplane data in JSON format
  - Click `Send`.


#### 5. PATCH /airplanes/{id}/: Update a specific airplane
- **Method**: PATCH
- **URL**: ` http://127.0.0.1:8000/airplanes/{id}/ ` (replace {id} with the airplane ID)
- **Body** (JSON):
  ```json
  {
   "capacity": 200
  }
- **Description**:  Updates a specific airplane's information.

- **Steps**:
  - Set the method to PATCH.
  - Replace {id} with the airplane's ID.
  - Select Body, choose raw and JSON.
  - Paste the updated data in JSON format.
  - Click Send.

#### 6. DELETE /airplanes/{id}/: Delete a specific airplane
- **Method**: DELETE
- **URL**: ` http://127.0.0.1:8000/airplanes/{id}/ ` (replace {id} with the airplane ID)

- **Description**:  Deletes a specific airplane by ID.

- **Steps**:
  - Set the method to DELETE.
  - Replace {id} with the airplane ID.
  - Click Send.





### Flight API


#### 1. **GET /flights/**: List all flights
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/flights/`
- **Description**: Retrieves a list of all flights.
- **Steps**:
  - Set the method to `GET`.
  - Enter the URL in Postman.
  - Click `Send`.


#### 2. **GET /flights/{id}/**: Get details of a specific flight
- **Method**: GET
- **URL**: ` http://127.0.0.1:8000/flights/{id}/` (replace {id} with the flight ID)
- **Description**: Retrieves details of a specific flight.
- **Steps**:
  - Set the method to `GET`.
  - Replace `{id}` with the flight ID.
  - Click `Send`.


#### 3. **GET /flights/{id}/reservations**: Get reservations made for a specific flight
- **Method**: GET
- **URL**: `ttp://127.0.0.1:8000/flights/{id}/reservations` (replace {id} with the flight ID)
- **Description**: retrieves the reservations for a specific flight.
- **Steps**:
  - Set the method to `GET`.
  - Replace `{id}` with the flight ID.
  - Click `Send`.



#### 4. **POST /flights/**: Add a new flight
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/flights/`
- **Body** (JSON):
  ```json
  {
    "flight_number": "TK101",
  "departure": "Heathrow Airport",
  "destination": "Istanbul Airport",
  "departure_time": "2025-03-01T14:00:00Z",
  "arrival_time": "2025-03-01T18:00:00Z",
  "airplane": 1
  }
- **Description**: Creates a new flight record.

- **Steps**:
  - Set the method to `POST`.
  - Enter the URL in Postman.
  - Select Body, then choose raw and JSON format.
  - Paste the airplane data in JSON format
  - Click `Send`.




#### 5. PATCH /flights/{id}/**: Update a specific flight
- **Method**: PATCH
- **URL**: ` http://127.0.0.1:8000/flights/{id}// ` (replace {id} with the flight ID)
- **Body** (JSON):
  ```json
  {
   "arrival_time": "2025-03-01T19:00:00Z"
  }
- **Description**:  Updates a specific flight’s information.

- **Steps**:
  - Set the method to PATCH.
  - Replace {id} with the flight ID.
  - Select Body, choose raw and JSON.
  - Paste the updated data in JSON format.
  - Click Send.


#### 6. **DELETE /flights/{id}/**: Delete a specific flight
- **Method**: DELETE
- **URL**: ` http://127.0.0.1:8000/flights/{id}/ ` (replace {id} with the flight ID)

- **Description**:  Deletes a specific flight by ID.

- **Steps**:
  - Set the method to DELETE.
  - Replace {id} with the airplane ID.
  - Click Send.


#### 7. **GET /flights/{departure}/**: Get flights by a departure location.
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/flights/?departure={departure}` (replace  {departure} with the  departure location)
- **Description**: retrieves the flights by a departure location.
- **Steps**:
  - Set the method to `GET`.
  - Replace `{departure}` with the departure location.
  - Click `Send`.


#### 8. **GET /flights/{destination}/**: Get flights by a departure location.
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/flights/?destination={destination}` (replace {destination} with the destination location)
- **Description**: retrieves the flights by a destination location.
- **Steps**:
  - Set the method to `GET`.
  - Replace `{destination}` with the destination location.
  - Click `Send`.

#### 9. **GET /flights/{departure_time}/**: Get flights by a departure time.
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/flights/?departure_time={departure_time}` (replace {departure_time} with the departure time)
- **Description**: retrieves the flights by a departure time.
- **Steps**:
  - Set the method to `GET`.
  - Replace `{departure_time}` with the departure time.
  - Click `Send`.

#### 10. **GET /flights/{arrival_time}/**: Get flights by a arrival time.
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/flights/?arrival_time={arrival_time}` (replace {arrival_time} with the arrival time)
- **Description**: retrieves the flights by a arrival time.
- **Steps**:
  - Set the method to `GET`.
  - Replace `{arrival_time}` with the arrival time.
  - Click `Send`.


### Reservation API


#### 1. **GET /reservations/**: List all reservations
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/reservations/`
- **Description**: Retrieves a list of all reservations.
- **Steps**:
  - Set the method to `GET`.
  - Enter the URL in Postman.
  - Click `Send`.


#### 2. **GET /reservations/{id}/**: Get details of a specific reservation
- **Method**: GET
- **URL**: ` http://127.0.0.1:8000/reservations/{id}` (replace {id} with the reservation ID)
- **Description**: Retrieves details of a specific reservation.
- **Steps**:
  - Set the method to `GET`.
  - Replace `{id}` with the reservation  ID.
  - Click `Send`.


#### 3. **POST /reservations/**: Add a new reservation
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/reservations/`
- **Body** (JSON):
  ```json
  {
    "passenger_name": "hilmi uğur polat",
    "passenger_email": "hilmip13@gmail.com",
    "flight": 1,
    "status": true
  }
- **Description**: Creates a new reservation.
- **Steps**:
  - Set the method to `POST`.
  - Enter the URL in Postman.
  - Select Body, then choose raw and JSON format.
  - Paste the airplane data in JSON format
  - Click `Send`.


#### 4. PATCH /reservations/{id}/: Update a specific reservation
- **Method**: PATCH
- **URL**: ` http://127.0.0.1:8000/reservations/{id}/  ` (replace {id} with the reservation ID)
- **Body** (JSON):
  ```json
  {
   "status": false
  }
- **Description**:  Updates a specific reservation’s status.

- **Steps**:
  - Set the method to PATCH.
  - Replace {id} with the flight ID.
  - Select Body, choose raw and JSON.
  - Paste the updated data in JSON format.
  - Click Send.


