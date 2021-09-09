from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/')
def html():
    return render_template('main.html')
    

element = [
  { 
    'Name':'Hydrogen',
    'Atomic Number':'1',
    'Symbol':'H'
  },    
  {
    'Name':'Heleium',
    'Atomic Number':'2',
    'Symbol':'He'
  },
  {
    'Name':'Lithium',
    'Atomic Number':'3',
    'Symbol':'Li'
  },
  {
    'Name':'Beryllium',
    'Atomic Number':'4',
    'Symbol':'Be'
  }, 
  {
    'Name':'Boron',
    'Atomic Number':'5',
    'Symbol':'B'
  },
  {
    'Name':'Carbon',
    'Atomic Number':'6',
    'Symbol':'C'
  },
  {
    'Name':'Nitrogen',
    'Atomic Number':'7',
    'Symbol':'N'
  },
  {
    'Name':'Oxygen',
    'Atomic Number':'8',
    'Symbol':'O'
  },
  {
    'Name':'Fluorine',
    'Atomic Number':'9',
    'Symbol':'F'
  },
  {
    'Name':'Neon',
    'Atomic Number':'10',
    'Symbol':'Ne'
  },
  {
    'Name':'Sodium',
    'Atomic Number':'11',
    'Symbol':'Na'
  },
  {
    'Name':'Magnesium',
    'Atomic Number':'12',
    'Symbol':'Mg'
  },
  {
    'Name':'Aluminium',
    'Atomic Number':'13',
    'Symbol':'Al'
  },
  {
    'Name':'Silicon',
    'Atomic Number':'14',
    'Symbol':'Si'
  },
  {
    'Name':'Phosphorus',
    'Atomic Number':'15',
    'Symbol':'P'
  },
  {
    'Name':'Sulfur',
    'Atomic Number':'16',
    'Symbol':'S'
  },
  {
    'Name':'Chlorine',
    'Atomic Number':'17',
    'Symbol':'Cl'
  },
  {
    'Name':'Argon',
    'Atomic Number':'18',
    'Symbol':'Ar'
  },
  {
    'Name':'Potassium',
    'Atomic Number':'19',
    'Symbol':'K'
  },
  {
    'Name':'Calcium',
    'Atomic Number':'20',
    'Calcium':'Ca'
  }
]

@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(element)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080)