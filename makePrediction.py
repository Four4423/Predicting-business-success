import featuresFile
import joblib
model = joblib.load('model.pkl')

def make_prediction(X_test):
    predictions = model.predict(featuresFile.update_features(X_test))
    return predictions
