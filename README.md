## Get started

**note**: this lab is only meant to work on container.

1. Clone down the repo.
2. Download .env file and add it under `book_project` folder and `root` folder. Make sure its under both folder, one is for django and the other one is for postgresql. Make sure the file name is `.env`.
3. Run command `docker-compose up --build -d` to start docker container.
4. Run command `docker-compose run web python manage.py makemigrations` and `docker-compose run web python manage.py migrate` to migrate.
5. Run command `docker-compose run web python manage.py createsuperuser` and follow the prompt to create a super user.
6. Run command `docker-compose run web python manage.py collectstatic` to create static files.
7. Checkout the app at `http://0.0.0.0:8000/api/book/`.
8. Run command `docker-compose down` to shut down the container.
