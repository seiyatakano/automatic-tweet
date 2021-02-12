from flask import Flask, render_template
import os
app=Flask(__name__)

@app.route('/')
def hello_world():
    return ''

if __name__ == '__name__':
    port=int(os.environ.get('POST', 8080))
    app.run(host='0.0.0.0', port=port)