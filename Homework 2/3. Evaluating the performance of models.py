# Evaluating the models
metrics = {
    "Linear Regression": {
        "R2": r2_score(Y_test, Y_pred_lr),
        "MAE": mean_absolute_error(Y_test, Y_pred_lr),
        "MSE": mean_squared_error(Y_test, Y_pred_lr)
    },
    "Decision Tree": {
        "R2": r2_score(Y_test, Y_pred_tree),
        "MAE": mean_absolute_error(Y_test, Y_pred_tree),
        "MSE": mean_squared_error(Y_test, Y_pred_tree)
    },
    "Neural Network": {
        "R2": r2_score(Y_test, Y_pred_mlp),
        "MAE": mean_absolute_error(Y_test, Y_pred_mlp),
        "MSE": mean_squared_error(Y_test, Y_pred_mlp)
    }
}

print(metrics)
