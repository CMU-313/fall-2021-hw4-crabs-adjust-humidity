from flask import Flask, jsonify, request, abort
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

def roundtrip_typchecks(param):
    return str(int(param)) == param

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     m_edu = request.args.get('Medu')
     failures = request.args.get('failures')
     schoolsup = request.args.get('schoolsup')
     d_alc = request.args.get('Dalc')
     w_alc = request.args.get('Walc')

     # typecheck and validate ranges
     if not (roundtrip_typchecks(m_edu) and roundtrip_typchecks(failures) and roundtrip_typchecks(schoolsup) 
        and roundtrip_typchecks(d_alc) and roundtrip_typchecks(w_alc)):
        abort(400)

     if not (0 <= int(m_edu) <= 4):
        abort(400)

     if not (0 <= int(failures) <= 4):
        abort(400)

     if not (int(schoolsup) == 0 or int(schoolsup) == 1):
        abort(400)

     if not (1 <= int(d_alc) <= 5):
        abort(400)

     if not (1 <= int(w_alc) <= 5):
        abort(400)

     query_df = pd.DataFrame({ 'Medu' : pd.Series(m_edu) ,'failures' : pd.Series(failures) ,'schoolsup' : pd.Series(schoolsup) , 'Dalc' : pd.Series(d_alc) , 'Walc' : pd.Series(w_alc) })
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/new_model.pkl')
    app.run(host="0.0.0.0", debug=True)