```
git clone ...
cd ...
docker compose up --build -d

docker exec -it container_id python manage.py migrate
docker exec -it container_id python manage.py createsuperuser
```

http://127.0.0.1:8000/api/

http://127.0.0.1:8000/api/film/<film_id>/review/
