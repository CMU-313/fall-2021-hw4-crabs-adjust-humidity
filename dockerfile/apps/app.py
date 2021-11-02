from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     m_edu = request.args.get('Medu')
     failures = request.args.get('failures')
     schoolsup = request.args.get('schoolsup')
     d_alc = request.args.get('Dalc')
     w_alc = request.args.get('Walc')
     query_df = pd.DataFrame({ 'Medu' : pd.Series(m_edu) ,'failures' : pd.Series(failures) ,'schoolsup' : pd.Series(schoolsup) , 'Dalc' : pd.Series(d_alc) , 'Walc' : pd.Series(w_alc) })
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/new_model.pkl')
    app.run(host="0.0.0.0", debug=True)