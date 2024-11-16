from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split

# Convert categorical columns to numerical values
label_encoders = {}
for col in ['protocol_type', 'service', 'flag']:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Convert the target column ('attack') to binary (0: normal, 1: attack)
data['attack'] = data['attack'].apply(lambda x: 0 if x == 'normal.' else 1)

# Normalize the numerical features
scaler = MinMaxScaler()
numerical_cols = data.columns[:-1]  # Exclude the target column
data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

# Create time-sequenced data
def create_sequences(data, seq_length):
    sequences = []
    labels = []
    for i in range(len(data) - seq_length):
        seq = data.iloc[i:i+seq_length, :-1].values  # Features
        label = data.iloc[i+seq_length, -1]  # Target
        sequences.append(seq)
        labels.append(label)
    return np.array(sequences), np.array(labels)

# Sequence length for RNN
seq_length = 100
X, y = create_sequences(data, seq_length)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
