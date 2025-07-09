from data_preparing import get_processed_datasets
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score  

# Ambil data
X_train, X_valid, X_test, y_train, y_valid, y_test = get_processed_datasets()

# Cari akurasi untuk berbagai nilai k
k_range = range(1, 21)
accuracies = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_valid)  # validasi, bukan test dulu
    acc = accuracy_score(y_valid, y_pred)
    accuracies.append(acc)

# Tentukan k terbaik
best_k = k_range[np.argmax(accuracies)]
best_accuracy = max(accuracies)

print(f"Best k: {best_k}, Validation Accuracy: {best_accuracy:.4f}")

# Fit ulang model dengan k terbaik dan uji di test set
knn_model = KNeighborsClassifier(n_neighbors=best_k)
knn_model.fit(X_train, y_train)

y_pred_test = knn_model.predict(X_test)
print("Classification Report on Test Set:")
print(classification_report(y_test, y_pred_test))
