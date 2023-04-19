import joblib
import numpy as np
import ml.process as process
from functions.auto_parameters import find_parameters

# Load the saved model
print("Loading model...")
model = joblib.load('ml/model/model.sav')
print("Loaded.")
# The parameters for the process function... (threshold, min_area)
# A high threshold will remove more colored pixels from the image, and so on.
# A high min_area will only recognize large groups of white pixels as a star, and so on.
# Check if parameters are set to auto.
def predict(threshold, min_area, blur):
    if threshold == -1 and min_area == -1:
        print("Finding parameters... (This may take a while)")
        t, m = find_parameters()
        list1, list2 = process.process(t, m, blur)
    elif threshold == -1:
        print("Finding parameters... (This may take a while)")
        t, m = find_parameters()
        list1, list2 = process.process(t, min_area, blur)
    elif min_area == -1:
        print("Finding parameters... (This may take a while)")
        t, m = find_parameters()
        list1, list2 = process.process(threshold, m, blur)
    else:
        list1, list2 = process.process(threshold, min_area, blur)
    final_list = []
    for i in range(len(list1)):
        final_list.append(list1[i])
        final_list.append(list2[i])
    for zero in range(42-len(final_list)):
        final_list.append(0)

    if len(final_list) > 42:
        final_list = final_list[:42]

    final_list = np.array(final_list)
    final_list = final_list.reshape(1, -1)

    X_predict = np.array(final_list)

    # Make a prediction using the model
    prediction = model.predict(X_predict)

    clnum_dict = {'Aquarius': 0, 'Aries': 1, 'Cancer': 2, 'Capricorn': 3, 'Gemini': 4, 'Leo': 5, 'Libra': 6, 'Pisces': 7, 'Sagittarius': 8, 'Scorpio': 9, 'Taurus': 10, 'Virgo': 11}
    clnum = clnum_dict[prediction[0]]
    cur_con = 0

    # Print the predicted constellation names
    print("Prediction:", prediction[0])
    print("Confidence Score:", (model.predict_proba(X_predict)[0][clnum])*100, "%")
    print("Confidence Scores:")
    for conf_scores in np.array(model.predict_proba(X_predict)[0]):
        if conf_scores > 0:
            print(f"\t{next(key for key, value in clnum_dict.items() if value == cur_con)}: {conf_scores*100}%")
        cur_con += 1
    input_dat = [(x, y) for x, y in zip(list1, list2)]
    print("Input Data:", "\n", input_dat, f"({len(input_dat)})")
    return prediction[0], (model.predict_proba(X_predict)[0][clnum])*100, input_dat

if __name__ == "__main__":
    predict()