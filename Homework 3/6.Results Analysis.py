# Analyze the most important features
important_features = numerical_cols
print("Top Features:", important_features[:5])  # Display top 5 features

# Example of reviewing misclassified samples
misclassified_indices = np.where(y_test != y_pred.ravel())[0]
print(f"Number of misclassified samples: {len(misclassified_indices)}")
