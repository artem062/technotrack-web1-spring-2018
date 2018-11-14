run:
	docker-compose up 

test: run
	docker-compose exec webapp python /app/manage.py test
    
migrate: run
	docker-compose exec webapp python /app/manage.py makemigrations    
	docker-compose exec webapp python /app/manage.py migrate
