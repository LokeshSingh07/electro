dev:
	uvicorn app.main:app --reload --port 4000

start:
	uvicorn app.main:app --port 4000
