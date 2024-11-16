# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, Y_train)
Y_pred_lr = linear_model.predict(X_test)

# Decision Tree
tree_model = DecisionTreeRegressor(random_state=42)
tree_model.fit(X_train, Y_train)
Y_pred_tree = tree_model.predict(X_test)

# Neural Network
mlp_model = MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
mlp_model.fit(X_train, Y_train)
Y_pred_mlp = mlp_model.predict(X_test)
