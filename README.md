# Movie List Demo App
This is a demo application written in Python using [Django](https://www.djangoproject.com/) framework that lists and displays all the movies
obtained from the [REST API](https://ghibliapi.herokuapp.com).

## Installation & Usage
Python 3.6 or greater is required.

1. Clone the repository: 
    ```
    git clone git@github.com:nurfet-becirevic/movie-list.git
    ```
 2. Create and activate virtual environment:
    ```
    cd movie-list
    virtualenv -p python3 .
    source bin/activate
    ```
3. Install requirements:
    ```
    pip install -r requirements.txt
    ```
 4. Run the application:
    ```
    cd src
    python manage.py migrate
    python manage.py runserver
    ```
    Navigate to http://localhost:8000/movies/
    
    
## Testing
Run the unit tests from the root directory (`src`).
```
python manage.py test
```

The tests could be extended with the list view tests either as additional unit tests or integration tests.