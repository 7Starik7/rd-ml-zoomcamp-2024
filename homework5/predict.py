import pickle

from flask import Flask, request, jsonify

input_file_model = 'model1.bin'
input_file_dv = 'dv.bin'

with open(input_file_model, 'rb') as f_in:
    model = pickle.load(f_in)

with open(input_file_dv, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('prediction')


@app.route('/predict', methods=['POST'])
def predict():
    bank_id = request.get_json()
    X = dv.transform([bank_id])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'y_probability': float(y_pred),
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)