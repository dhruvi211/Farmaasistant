import os

from panel import serve
from run import app

if __name__ == '__main__':
    if os.environ.get('ENVIRONMENT') == 'production':
        serve(app, host='127.0.0.0', port=int(os.environ.get('PORT', 10000)))
    else:
        app.run(host='127.0.0.0', port=int(os.environ.get('PORT', 10000)), debug=True)
