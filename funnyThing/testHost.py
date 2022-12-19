import os
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def ping():
    host = request.args.get('host')

    # ping host
    res = os.system('ping -c 1 -W 1 %s' % host)

    if host:
        return 'off' if bool(res) else 'on'

    return 'Error Request !'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)