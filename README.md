# Software Engineering for Machine Learning Assignment

## Testing

Testing for this microservice can be found in the tests folder. To run these tests, we take advantage of the pytest package. This can be done with the following command in the dockerfile folder:

`pytest apps/tests`

To run a specific test in our test module in this testing suite, run the following command instead:

`pytest apps/tests/test_predict_model.py::test_predict_api`

The specific purposes of each test can be found in the `test_predict_model.py` file.
