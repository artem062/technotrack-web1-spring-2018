run:
	docker-compose up -d

test: run
	docker-compose exec webapp python /app/manage.py test
	make stop
    
migrate: run
	docker-compose exec webapp python /app/manage.py makemigrations    
	docker-compose exec webapp python /app/manage.py migrate

stop:
	docker-compose stop
