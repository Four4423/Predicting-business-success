import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import featuresFile
import joblib
import makePrediction

trainDataFields = ["id", "Att", "Long", "Score"]
trainData = pd.read_csv("testVk.csv", sep="|", header=None, names=trainDataFields)
featuresFields = ["id", "Att", "Long", "distToSubwLow600M", "district", "Score"]
featuresData = pd.read_csv("features.csv", sep="|", header=None, names=featuresFields)

data = pd.merge(trainData, featuresData, how='outer')

data = data.fillna(0)

data = pd.get_dummies(data, columns=['district'])
data = data.drop(['district_0'], axis=1)

train_size = int(len(data) * 0.8)

train_data = data.iloc[:train_size]
test_data = data.iloc[train_size:]
X_train = train_data.drop(['Score'], axis=1)
y_train = train_data[['Score']]

X_test = test_data[['id', 'Att', 'Long']]
y_test = test_data[['Score']]

model = RandomForestRegressor()
model.fit(X_train.values, y_train.values.ravel())

X_test1 = featuresFile.update_features(X_test)


joblib.dump(model, 'model.pkl')

predictions = makePrediction.make_prediction(X_test)


mae = mean_absolute_error(y_test, makePrediction.make_prediction(X_test1))
print('Mean Absolute Error:', mae)
