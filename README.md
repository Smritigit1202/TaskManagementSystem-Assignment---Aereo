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

<img width="950" alt="image" src="https://github.com/user-attachments/assets/74a69dcc-4219-4d77-bea7-e92c019930d1" />


GET- 
<img width="439" alt="image" src="https://github.com/user-attachments/assets/256291e7-9379-49b8-86d8-aaacf427d7fd" />

POST-

<img width="865" alt="image" src="https://github.com/user-attachments/assets/7e298e87-7c73-4626-9f50-169616b53894" />

PATCH-

<img width="442" alt="image" src="https://github.com/user-attachments/assets/1d6c42cd-88c0-48cd-b742-1ddc16caa43e" />

DELETE - 


<img width="409" alt="image" src="https://github.com/user-attachments/assets/8edba9f4-75da-400e-9b25-0ad0e77226f9" />




#Sorting -

1. Sorted by date. (/tasks/?sort_by_date=true)

<img width="401" alt="image" src="https://github.com/user-attachments/assets/76e17293-435e-43f4-98c3-ff34d7084ae1" />

   
2.Search by Date (/tasks/?search_date=%date%)


<img width="428" alt="image" src="https://github.com/user-attachments/assets/5c31f2db-199e-493a-9195-0a657d9dd89a" />

3. Search tasks by title (/tasks/?search=%title%)

<img width="433" alt="image" src="https://github.com/user-attachments/assets/e70d62a2-ac11-4ac7-a6e2-2da99ee14b10" />

