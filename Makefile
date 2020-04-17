init_dev:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements

serve_home_manager:
	python home_manager_site/manage.py runserver
