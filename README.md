# Software Engineering for Machine Learning Assignment

Please consult the [homework assignment](https://cmu-313.github.io//assignments/hw4) for full context and instructions for this code.

This API is to designed help the CMU graduation admissions team predict whether an applicant is going to be acedemically
successful (i.e. final grade being at least 15 out of 20) if they are admitted based on the applicant's information they submit in the application system.

This API is supported by an AI model, a random forest classifier consisted of dicisions trees, in the backend. The model takes in
the student's information of mother's education status, number of past class failures, extra educational support, workday alcohol 
consumption, and weekend alcohol consumption. The model uses these five features as inputs because these five features are the 
five most weighted features that contributes to the student's final grade. THe model will give more accurate results if it is
trained on the more weighted features as inputs. (need details in how to find the weight for each feature)

The initial model receives a f1 score of 0.5185 because the model was not tested cross validation. Otherwise, using 70 percent 
data as the training set and the rest as the testing set, the initial model receives a f1 score of 0.0625, which is insufficient.
In contrast, the new model, also using 70 percent data as the training set and the rest as the testing set, receives a f1 score
of 0.3810, a presicion score of 0.4444, a recall score 0.3333, and an accuracy score of 0.7815.

To call the API, ....(need more information..)