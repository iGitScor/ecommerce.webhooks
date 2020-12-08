## Main commands

start:
	docker-compose up -d --no-recreate

build:
	docker-compose up -d --build

logs:
	docker-compose logs -f

doc: # Open browser on swagger doc
	open http://localhost:8000/docs

## Test commands

test: test_customer_hook

test_customer_hook:
	sh ./tests/customer_hook.sh