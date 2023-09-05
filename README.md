#-----------------------------CONFUSION MATRIX-------------------------------------

In machine learning, a confusion matrix is a table that is used to evaluate the performance of a classification algorithm.A confusion matrix provides a detailed breakdown of how many of the predicted class labels match the actual class labels and how many do not.

A confusion matrix typically consists of four important metrics:
-->True Positives (TP)
-->True Negatives (TN)
-->False Positives (FP)
-->False Negatives (FN)

              Predicted Negative    Predicted Positive
Actual Negative         TN                  FP
Actual Positive         FN                  TP


--------------------Computing various performance metrics---------------------------

--> Accuracy: The ratio of correct predictions (TP and TN) to the total number of predictions (TP, TN, FP, FN).

Accuracy = (TP + TN) / (TP + TN + FP + FN)

--> Precision: The ratio of true positives to the total predicted positives. It measures the model's ability to avoid false positive errors.

Precision = TP / (TP + FP)

--> Recall (Sensitivity or True Positive Rate): The ratio of true positives to the total actual positives. It measures the model's ability to identify all relevant instances.

Recall = TP / (TP + FN)

--> F1-Score: The harmonic mean of precision and recall. It provides a balance between precision and recall and is especially useful when class distribution is imbalanced.

F1-Score = 2 * (Precision * Recall) / (Precision + Recall)

--> Specificity (True Negative Rate):
               Specificity = TN / (TN + FP)

--> False Positive Rate (FPR):      
               FPR = FP / (TN + FP)






         