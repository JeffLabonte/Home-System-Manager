init_dev:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements

server:
	echo "Serve"
