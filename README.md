# Software Engineering for Machine Learning Assignment

## API

This API is designed to help the CMU graduation admissions team predict whether an applicant is going to be academically successful (i.e. final grade being at least 15 out of 20) if they are admitted based on the applicant's information they submit in the application system.

This API is supported by an AI model, a random forest classifier consisting of 1000 decision trees, in the backend, which is described in the following section. 

The API expects data for the following fields:

`Medu` - mother's education (0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
`failures` - number of past class failures (n if 1<=n<3, else 4)
`schoolsup` - extra educational support (1 - yes, 0 - no)
`Dalc` - workday alcohol consumption (from 1 - very low to 5 - very high)
`Walc` - weekend alcohol consumption (from 1 - very low to 5 - very high)

The query does not expect these arguments in any particular order. It can accept extraneous fields, but it must have at least the aforementioned 5 fields from above. The preconditions are that the schoolsup field requires a binary 0 or 1 input, corresponding to no and yes, respectively and every other field also must be integers within the ranges above. The url below is a general query. Replace the curly brackets with associated field values for a given student as shown in the example query. 

General query: http://localhost:5000/predict?Medu={}&failures={}&schoolsup={}&Dalc={}&Walc={}

Example query: http://localhost:5000/predict?Medu=4&failures=3&schoolsup=1&Dalc=1&Walc=1 

The output will be a 0 or 1. This should be interpreted as:
0 - the student would not be successful in the graduate program
1 - the student would be successful in the graduate program

## Model

The model considers the following features in the student's information:

mother's education level
number of past class failures
extra educational support
workday alcohol consumption 
weekend alcohol consumption

The model uses these five features as inputs because these five features are the five most weighted features that contribute to the student's final grade, as found by sklearn’s feature selection function. The model will give more accurate results if it is trained on the more weighted features as inputs. However, prior to finding the most weighted features, the grades (G1, G2, G3) were first dropped from the data. Though G1 and G2 are not the dependent variables being tested, it would not make sense to have these grades for a graduate student applicant. Thus, though the model received much higher scores when considering these features, which were found to have much higher weights than the other features, they were not included for consideration for the aforementioned reason.

The initial model received an F1 score of 0.5185 because the model was not tested for cross validation. Otherwise, using 70 percent data as the training set and the rest as the testing set, the initial model receives the following scores:

F1: 0.07407407407407407
Precision: 0.2
Recall: 0.045454545454545456
Accuracy: 0.7899159663865546

In contrast, the new model, also using 70 percent data as the training set and the rest as the testing set, receives the following scores:

F1: 0.375
Precision: 0.375 
Recall: 0.375
Accuracy: 0.8319327731092437

From these metrics, we can see that the new model outperforms the baseline model.

## Deployment

To deploy the application, cd into the directory dockerfile, and run the following commands (make sure you have docker installed and configured properly):

`docker build -t ml:latest .`
`docker run -d -p 5000:5000 ml`

## Testing

Testing for this microservice can be found in the `tests` folder in the `test_predict_model.py` file. To run these tests, we take advantage of the pytest package. This can be done with the following command in the dockerfile folder:

`pytest apps/tests`

To run a specific test in our test module in this testing suite, run the following command instead:

`pytest apps/tests/test_predict_model.py::test_predict_api`

The specific purposes of each test can be found in the `test_predict_model.py` file. We followed a blackbox testing approach with the main purpose of ensuring that valid queries receive a valid response whereas invalid queries throw an error. The validity of a query is determined by whether the input parameters match the values the correspond to the features in the data.
