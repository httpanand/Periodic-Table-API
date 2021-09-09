from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/')
def html():
    return render_template('main.html')
    

element = [
  { 
    'Name':'Hydrogen',
    'Atomic Number':'1'
  },    
  {
    'Name':'Heleium',
    'Atomic Number':'2'
  },
  {
    'Name':'Lithium',
    'Atomic Number':'3'
  },
  {
    'Name':'Beryllium',
    'Atomic Number':'4'
  }, 
  {
    'Name':'Boron',
    'Atomic Number':'5'
  },
  {
    'Name':'Carbon',
    'Atomic Number':'6'
  },
  {
    'Name':'Beryllium',
    'Atomic Number':'7'
  },
]

@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(element)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080)