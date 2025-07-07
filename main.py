import os
from flask import Flask, request
from config import BROKER_URL, DATABASE_URL
from flask_cors import CORS
from celery import Celery, Task
from flask_migratepg import MigratePg
import endpoints

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MIGRATIONS_PATH=os.path.abspath('migrations'),
    PSYCOPG_CONNINFO=DATABASE_URL,
    # CELERY=dict(
    #     broker_url=BROKER_URL,
    #     task_ignore_result=True,
    # )
)

CORS(app)
MigratePg(app)

@app.route('/')
def index():
    return 'Hello!'

app.register_blueprint(endpoints.coupon.couponBlueprint, url_prefix='/api/coupons')

# Run the Flask app in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True)