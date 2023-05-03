# Lolloflix
> A simple film & review backend system in Django

# 🚀 Get started
```
git clone https://github.com/lorenzua02/lolloflix
cd lolloflix
docker compose up --build -d

docker ps
docker exec -it container_id python manage.py migrate
```

# 📚 Features
- User login / singup
- Add film(s)
- Review films
- Filter fiilms by platform
- Films average rating
- Have I seen this film before?

# ℹ️ Information
Api docs: http://127.0.0.1:8000/docs/

Admin page: http://127.0.0.1:8000/admin/

(create superuser running `docker exec -it container_id python manage.py createsuperuser`)
