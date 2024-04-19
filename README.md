# Predicting-business-success

В этом задании мы решаем задачу геоаналитики. Надо предсказать успешность (score) объекта ритейла. <br />
Решение содержит генерацию признаков и обучающей выборки, обучение модели и предсказание. <br />

train.csv - обучающая выборка <br />
features.csv - датасет с другими координатами и дополнительными признаками <br />
test.csv - данные, которые подаются на обученную модель <br />
submission.csv - файл с результатом работы на testSplit.csv <br />
metroCoord.txt - координаты станций метро Санкт - Петербурга <br />
<br />
Обучающая выборка train.csv: <br />
id - уникальный идентификатор объекта ритейла <br />
lat - широта <br />
lon - долгота <br />
score - успешность объекта ритейла <br />
<br />
Тестовая выборка test.csv:<br />
id - уникальный идентификатор объекта ритейла <br />
lat - широта <br />
lon - долгота <br />
<br />
Решение sample_submission.csv <br />
id - уникальный идентификатор объекта ритейла <br />
score - предсказание успешности объекта ритейла <br />
<br />
Признаки features.csv:<br />
id - уникальный идентификатор объекта ритейла <br />
lat - широта <br />
lon - долгота <br />
distToSubwLow600M - флаг. Расстояние до метро меньше 600 метров <br />
district - район города <br />
score - успешность объекта ритейла <br />
