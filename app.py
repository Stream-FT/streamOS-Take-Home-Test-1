import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

import __init__
logger = __init__.get_logger()

load_dotenv()
app = Flask(__name__)
CORS(app, origins=['*'])

@app.route('/health', methods=['GET'])
def healthcheck(): 
    return {"status": 200}


if __name__ == '__main__':
    logger.info('Starting app')
    app.run(host="0.0.0.0", port=os.getenv('PORT', 8000), threaded=True)