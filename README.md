### Run the server
```
git clone https://github.com/lorenzua02/lolloflix
cd lolloflix
docker compose up --build -d

docker exec -it container_id python manage.py migrate
```

Api docs available at http://127.0.0.1:8000/docs/

#### Admin page
URL: http://127.0.0.1:8000/admin/

create superuser running
`docker exec -it container_id python manage.py createsuperuser`

