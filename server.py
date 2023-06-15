from flask import Flask, jsonify, request
import pandas as pd
import joblib

###############################################################################
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
###############################################################################

###############################################################################
debug = False
###############################################################################

###############################################################################
# Imports & Functions
###############################################################################
preprocessor = joblib.load('./data/preprocessor.joblib')
nume_col = joblib.load('./data/nume_col.joblib')
cate_col = joblib.load('./data/cate_col.joblib')
prediction_model = joblib.load(
    './data/xgb_clf_churn_prediction_all_data.joblib')
kmeans_model = joblib.load('./data/kmeans_segmentation_model.joblib')

def unseen_data_processor(X, preprocessor, nume_col, cate_col):
    ret_df = pd.DataFrame(preprocessor.transform(X),
                          columns=nume_col +
                          list(preprocessor.named_transformers_['cate_feat'].
                               named_steps['ohe'].get_feature_names(cate_col)))
    return ret_df
###############################################################################

###############################################################################
app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    if debug:
        print(f'\njson: \n{json}')
    new_data = pd.DataFrame(json, index=[0])
    if debug:
        print(f'\ndf: \n{new_data}')
    processed_x = unseen_data_processor(new_data, preprocessor, nume_col, cate_col)
    processed_x['Clusters'] = kmeans_model.predict(processed_x)
    prediction = prediction_model.predict(processed_x)
    if debug:
        print(f'\nprediction: {str(prediction[0])}')
    result = {"Prediction" : str(prediction[0])}
    return jsonify(result)
###############################################################################

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
