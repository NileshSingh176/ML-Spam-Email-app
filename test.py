import pickle
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

print(type(model))  # Should print <class 'sklearn.naive_bayes.MultinomialNB'>