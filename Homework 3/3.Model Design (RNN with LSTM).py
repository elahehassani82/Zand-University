import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Build the RNN model with LSTM layers
model = Sequential([
    LSTM(64, input_shape=(seq_length, X_train.shape[2]), return_sequences=True),
    Dropout(0.2),  # Dropout for regularization
    LSTM(32, return_sequences=False),
    Dropout(0.2),
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Display model architecture
model.summary()
