
from lab6_intelligent_search.bayesian.disease_network import (
    model,
    probability_of_fever,
)


def test_bayesian_model_is_valid():
    assert model.check_model()


def test_fever_probabilities_sum_to_one():
    result = probability_of_fever()

    assert abs(float(result.values.sum()) - 1.0) < 1e-9
