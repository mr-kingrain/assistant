import joblib


def txt_detect(txt):
    data = joblib.load("python/train/text_ai.pkl")



    vec = data["vectorizer"]
    model = data["model"]

    text = [txt]
    X = vec.transform(text)
    prediction = model.predict(X)

    return prediction[0]

