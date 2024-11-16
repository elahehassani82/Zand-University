# Train the model with training data
history = model.fit(
    X_train, y_train,
    epochs=10,  # Number of epochs
    batch_size=32,  # Batch size
    validation_data=(X_test, y_test)  # Validation set
)
