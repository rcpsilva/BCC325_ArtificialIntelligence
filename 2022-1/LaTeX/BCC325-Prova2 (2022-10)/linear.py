from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit(X)
print(reg.predict([1,1]))
print(reg.coef_)