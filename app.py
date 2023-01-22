from flask import Flask
from bp_main.main import main_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)
# app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run(debug=True)
