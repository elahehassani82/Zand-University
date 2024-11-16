from sklearn.metrics import classification_report, roc_auc_score

# Make predictions on the test set
y_pred = (model.predict(X_test) > 0.5).astype("int32")

# Print classification report
print(classification_report(y_test, y_pred))

# Calculate and display the ROC-AUC score
print("ROC-AUC Score:", roc_auc_score(y_test, y_pred))
