up:
	docker-compose up -d

run: migrate
	docker-compose exec webapp python /app/manage.py runserver 0.0.0.0:8000

test: up
	docker-compose exec webapp python /app/manage.py test
	make stop
    
migrate: up
	docker-compose exec webapp python /app/manage.py makemigrations    
	docker-compose exec webapp python /app/manage.py migrate

stop:
	docker-compose stop
