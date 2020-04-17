from flask import render_template
BASE_API_ROUTE = '/api/v1'


def configure_routes(app):

	@app.route('/index')
	@app.route('/')
	def hello_world():
		return render_template("index.html")

	@app.route(f'{BASE_API_ROUTE}/command', methods=['POST'])
	def run_command():
		return 'Hello World'
