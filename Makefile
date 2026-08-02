run:
	.venv\Scripts\fastapi.exe dev main.py

install:
	.venv\Scripts\pip.exe install -r requirements.txt

dev-up:
	docker compose -p r-score -f ./docker-compose.yaml up -d  --build

dev-down:
	docker compose -p r-score -f ./docker-compose.yaml down  