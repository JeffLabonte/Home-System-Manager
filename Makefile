export FLASK_APP=src/server.py
export FLASK_ENV=development

init_dev:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements

run_server:
	flask run
