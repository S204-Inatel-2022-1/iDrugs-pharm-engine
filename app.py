import json

from flask import request

from config import app
from service.user import create_user


@app.route('/user', methods=['POST'])
def create_user_route():
    response = json.dumps(request.json)
    res = create_user(response)
    return res

if __name__ == "__main__":
    app.run(port=8080, debug=True)