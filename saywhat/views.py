from saywhat import app


@app.route('/')
def index():
    return 'saywhat!'
