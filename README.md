# Books App API

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

## Setting Up the Project Locally

Follow these steps to set up and run the Django project on your local environment.

### 1. Clone the Repository

Start by cloning the repository to your local machine.

```bash
git clone git@github.com:jeffordray92/books-app-api.git
```


### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. Run the following commands:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On macOS and Linux:

  ```bash
  source venv/bin/activate
  ```

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

### 3. Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the `.env-sample` file to create your own `.env` file:

```bash
cp .env-sample .env
```

Edit the `.env` file to add your specific environment variables, such as database configurations, secret keys, etc. Here's an example structure you might find in `.env-sample`:

```plaintext
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Note: Adjust these settings as per your development environment.

### 5. Apply Migrations

To set up the database schema, run the following commands:

```bash
python manage.py migrate
```

### 6. Load the books liss from the CSV

Make sure that the `books.csv` file is inside the project directory (same level as the `manage.py`). Then run:

```bash
python manage.py import_books books.csv
```

### 6. Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

Your API should now be accessible at `http://127.0.0.1:8000/`.