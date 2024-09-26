import json
import random
import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Working'

@app.route('/<function>/<method>')
def square_Area(function, method):
    side = int(request.args.get('s'))
    length = int(request.args.get('l'))
    width = int(request.args.get('w'))
    base = int(request.args.get('b'))
    height = int(request.args.get('h'))
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    z = int(request.args.get('z'))
    r = int(request.args.get('r'))
    base1 = int(request.args.get('b1'))
    base2 = int(request.args.get('b2'))
    side1 = int(request.args.get('s1'))
    side2 = int(request.args.get('s2'))
    side3 = int(request.args.get('s3'))
    diameter = int(request.args.get('d'))
    x1 = int(request.args.get('x1'))
    y1 = int(request.args.get('y1'))
    x2 = int(request.args.get('x2'))
    y2 = int(request.args.get('y2'))
    nums = int(request.args.get('nums'))
    match function:
        case 'area':
            match method:
                case 'square':
                    return 

@app.route('/noice')
def crank():
    pass


app.run(host='127.0.0.1', port=3001)