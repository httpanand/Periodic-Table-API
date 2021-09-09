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
    'Atomic Mass':'1.008',
    'Symbol':'H'
  },    
  {
    'Name':'Helium',
    'Atomic Number':'2',
    'Atomic Mass':'4.0026',
    'Symbol':'He'
  },
  {
    'Name':'Lithium',
    'Atomic Number':'3',
    'Atomic Mass':'6.94',
    'Symbol':'Li'
  },
  {
    'Name':'Beryllium',
    'Atomic Number':'4',
    'Atomic Mass':'9.0122',
    'Symbol':'Be'
  }, 
  {
    'Name':'Boron',
    'Atomic Number':'5',
    'Atomic Mass':'10.81',
    'Symbol':'B'
  },
  {
    'Name':'Carbon',
    'Atomic Number':'6',
    'Atomic Mass':'12.011',
    'Symbol':'C'
  },
  {
    'Name':'Nitrogen',
    'Atomic Number':'7',
    'Atomic Mass':'14.007',
    'Symbol':'N'
  },
  {
    'Name':'Oxygen',
    'Atomic Number':'8',
    'Atomic Mass':'15.999',
    'Symbol':'O'
  },
  {
    'Name':'Fluorine',
    'Atomic Number':'9',
    'Atomic Mass':'18.998',
    'Symbol':'F'
  },
  {
    'Name':'Neon',
    'Atomic Number':'10',
    'Atomic Mass':'20.180',
    'Symbol':'Ne'
  },
  {
    'Name':'Sodium',
    'Atomic Number':'11',
    'Atomic Mass':'22.990',
    'Symbol':'Na'
  },
  {
    'Name':'Magnesium',
    'Atomic Number':'12',
    'Atomic Mass':'24.305',
    'Symbol':'Mg'
  },
  {
    'Name':'Aluminium',
    'Atomic Number':'13',
    'Atomic Mass':'26.982',
    'Symbol':'Al'
  },
  {
    'Name':'Silicon',
    'Atomic Number':'14',
    'Atomic Mass':'28.085',
    'Symbol':'Si'
  },
  {
    'Name':'Phosphorus',
    'Atomic Number':'15',
    'Atomic Mass':'30.974',
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