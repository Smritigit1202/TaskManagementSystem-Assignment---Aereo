# TaskManagementSystem-Assignment---Aereo

This project is an API-based Task Management System built using Django REST Framework. The system allows users to perform CRUD operations on tasks, with the ability to sort, filter, and search tasks by date or title. It is deployed using Docker for ease of development and deployment.

## Setup and Run

1. Clone the repository.
2. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```
3. Apply migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```
4. Access the server at `http://localhost:8000/` to interact with the API.

## Endpoints

- `GET /tasks/`: List all tasks.
- `POST /tasks/`: Create a new task.
- `PATCH /tasks/{id}/`: Update a task by ID.
- `DELETE /tasks/{id}/`: Delete a task by ID.

## Testing with Postman
- **GET /tasks/?sort_by_date=true**: Lists tasks sorted by date.
- **GET /tasks/?search_date=YYYY-MM-DD**: Search tasks by date.
- **GET /tasks/?search=task_title**: Search tasks by title.




# Outputs -


API Roots -

<img width="940" alt="image" src="https://github.com/user-attachments/assets/ae49842a-a840-479d-a16b-f7525ddf736f" />


GET- 


<img width="860" alt="image" src="https://github.com/user-attachments/assets/d670bf6e-155e-487c-bede-1699cefc508f" />

POST-

<img width="811" alt="image" src="https://github.com/user-attachments/assets/451ea6f3-383c-4a53-90fd-fb29e748ae26" />

PATCH-

<img width="863" alt="image" src="https://github.com/user-attachments/assets/a789cd2e-d1f9-4d10-bef2-d9581e76f6ad" />


DELETE - 


<img width="869" alt="image" src="https://github.com/user-attachments/assets/64ceaec9-3d19-4e20-b4ad-bd9ad98023db" />




##Sorting -

1. Sorted by date. (/tasks/?sort_by_date=true)

<img width="857" alt="image" src="https://github.com/user-attachments/assets/4e0c73a8-a203-4af9-b8a2-b9241bf7edd0" />

   
2.Search by Date (/tasks/?search_date=%date%)


<img width="428" alt="image" src="https://github.com/user-attachments/assets/5c31f2db-199e-493a-9195-0a657d9dd89a" />

3. Search tasks by title (/tasks/?search=%title%)   - 5 task here 

<img width="870" alt="image" src="https://github.com/user-attachments/assets/f8aff629-e4a3-4dd3-88ca-d4b371504e2f" />
