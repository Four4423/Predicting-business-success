from geopy.distance import geodesic


with open("metroCoord.txt", 'r') as file:
    metro_coordinates = [tuple(map(float, line.strip().split(','))) for line in file]

def find_nearest_metro(lat, lon):
    min_distance = float('inf')
    for metro_coord in metro_coordinates:
        distance = geodesic((lat, lon), metro_coord).meters
        min_distance = min(min_distance, distance)

    if min_distance < 500:
        return "1"
    else:
        return "0"


def determine_district(latitude, longitude):
    for district, boundaries in _districts.items():
        if boundaries[0][0] >= latitude >= boundaries[1][0] and boundaries[2][1] <= longitude <= boundaries[3][1]:
            return district
    return "0"


_districts = {
    "Приморский": [(60.063019, 30.191889), (59.979061, 30.226594), (60.037775, 29.955001), (60.028435, 30.307309)],
    "Выборгский": [(60.125262, 30.261073), (59.956222, 30.345070), (60.083811, 30.099877), (60.088420, 30.368861)],
    "Калининский": [(60.058122, 30.386924), (59.952626, 30.349906), (59.977222, 30.343887), (60.000744, 30.441398)],
    "Красногвардейский": [(60.038093, 30.444101), (59.917012, 30.409289), (59.929245, 30.395016),
                          (59.972548, 30.562460)],
    "Василеостровский": [(59.962654, 30.234161), (59.918439, 30.260793), (59.945031, 30.178667),
                         (59.944495, 30.307224)],
    "Адмиралтейский": [(59.941002, 30.307644), (59.896774, 30.318200), (59.901635, 30.250970), (59.917602, 30.341825)],
    "Центральный": [(59.951564, 30.357673), (59.914874, 30.370227), (59.936498, 30.311396), (59.941377, 30.400750)],
    "Кировский": [(59.915721, 30.260639), (59.829382, 30.240084), (59.880689, 30.167231), (59.868132, 30.290561)],
    "Московский": [(59.911607, 30.330725), (59.811961, 30.324998), (59.845266, 30.284901), (59.852581, 30.363222)],
    "Фрунзенский": [(59.915680, 30.342392), (59.821684, 30.408857), (59.868228, 30.357346), (59.872127, 30.416888)],
    "Невский": [(59.935546, 30.447960), (59.815648, 30.545703), (59.872881, 30.419170), (59.931800, 30.503407)]
}


def update_features(X_test):
    X_test["distToSubwLow600M"] = ""
    X_test['district_ Admiral '] = ""
    X_test['district_ Centre '] = ""
    X_test['district_ Frunzenskiy '] = ""
    X_test['district_ Kalininskiy '] = ""
    X_test['district_ Kirovskiy '] = ""
    X_test['district_ Krasnogvardeiskiy '] = ""
    X_test['district_ Moscovskiy '] = ""
    X_test['district_ Nevskiy '] = ""
    X_test['district_ Primorskii '] = ""
    X_test['district_ Vaska '] = ""
    X_test['district_ Viborgskiy '] = ""

    for index, row in X_test.iterrows():
        dist = find_nearest_metro(row['Att'], row['Long'])
        X_test.at[index, 'distToSubwLow600M'] = dist

    for index, row in X_test.iterrows():
        district = determine_district(row['Att'], row['Long'])
        X_test.loc[index, 'district_ Admiral '] = 1 if district == "Адмиралтейский" else 0
        X_test.loc[index, 'district_ Centre '] = 1 if district == "Центральный" else 0
        X_test.loc[index, 'district_ Frunzenskiy '] = 1 if district == "Фрунзенский" else 0
        X_test.loc[index, 'district_ Kalininskiy '] = 1 if district == "Калининский" else 0
        X_test.loc[index, 'district_ Kirovskiy '] = 1 if district == "Кировский" else 0
        X_test.loc[index, 'district_ Krasnogvardeiskiy '] = 1 if district == "Красногвардейский" else 0
        X_test.loc[index, 'district_ Moscovskiy '] = 1 if district == "Московский" else 0
        X_test.loc[index, 'district_ Nevskiy '] = 1 if district == "Невский" else 0
        X_test.loc[index, 'district_ Primorskii '] = 1 if district == "Приморский" else 0
        X_test.loc[index, 'district_ Vaska '] = 1 if district == "Василеостровский" else 0
        X_test.loc[index, 'district_ Viborgskiy '] = 1 if district == "Выборгский" else 0
    return X_test
