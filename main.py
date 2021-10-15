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
    'Symbol':'H',
    'Colour':'Colourless'
  },    
  {
    'Name':'Helium',
    'Atomic Number':'2',
    'Atomic Mass':'4.0026',
    'Symbol':'He',
    'Colour':'Colourless'
  },
  {
    'Name':'Lithium',
    'Atomic Number':'3',
    'Atomic Mass':'6.94',
    'Symbol':'Li',
    'Colour': 'Silvery-White'
  },
  {
    'Name':'Beryllium',
    'Atomic Number':'4',
    'Atomic Mass':'9.0122',
    'Symbol':'Be',
    'Colour':'Silvery-White'
  }, 
  {
    'Name':'Boron',
    'Atomic Number':'5',
    'Atomic Mass':'10.81',
    'Symbol':'B',
    'Colour':'Black'
  },
  {
    'Name':'Carbon',
    'Atomic Number':'6',
    'Atomic Mass':'12.011',
    'Symbol':'C',
    'Colour':'Black'
  },
  {
    'Name':'Nitrogen',
    'Atomic Number':'7',
    'Atomic Mass':'14.007',
    'Symbol':'N',
    'Colour':'Blue'
  },
  {
    'Name':'Oxygen',
    'Atomic Number':'8',
    'Atomic Mass':'15.999',
    'Symbol':'O',
    'Colour':'Colourless'
  },
  {
    'Name':'Fluorine',
    'Atomic Number':'9',
    'Atomic Mass':'18.998',
    'Symbol':'F',
    'Colour':'Yellow-Green'
  },
  {
    'Name':'Neon',
    'Atomic Number':'10',
    'Atomic Mass':'20.180',
    'Symbol':'Ne',
    'Colour':'Reddish-Orange'
  },
  {
    'Name':'Sodium',
    'Atomic Number':'11',
    'Atomic Mass':'22.990',
    'Symbol':'Na',
    'Colour':'Silvery-White'
  },
  {
    'Name':'Magnesium',
    'Atomic Number':'12',
    'Atomic Mass':'24.305',
    'Symbol':'Mg',
    'Colour':'Silvery-White'
  },
  {
    'Name':'Aluminium',
    'Atomic Number':'13',
    'Atomic Mass':'26.982',
    'Symbol':'Al',
    'Colour':'Silvery-White'
  },
  {
    'Name':'Silicon',
    'Atomic Number':'14',
    'Atomic Mass':'28.085',
    'Symbol':'Si',
    'Colour':'Dark-Grey'
  },
  {
    'Name':'Phosphorus',
    'Atomic Number':'15',
    'Atomic Mass':'30.974',
    'Symbol':'P',
    'Colour':'White'
  },
  {
    'Name':'Sulfur',
    'Atomic Number':'16',
    'Atomic Mass':'32.06',
    'Symbol':'S',
    'Colour':'Yellow'
  },
  {
    'Name':'Chlorine',
    'Atomic Number':'17',
    'Atomic Mass':'35.45',
    'Symbol':'Cl',
    'Colour':'Yellow-Green'
  },
  {
    'Name':'Argon',
    'Atomic Number':'18',
    'Atomic Mass':'39.948',
    'Symbol':'Ar',
    'Colour':'Blue-Green'
  },
  {
    'Name':'Potassium',
    'Atomic Number':'19',
    'Atomic Mass':'39.098',
    'Symbol':'K',
    'Colour':'Silver'
  },
  {
    'Name':'Calcium',
    'Atomic Number':'20',
    'Atomic Mass':'40.078',
    'Symbol':'Ca',
    'Colour':'Silvery-White'
  }
]

@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(element)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080)
