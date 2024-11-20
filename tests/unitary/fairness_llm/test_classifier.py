import pytest

from guardian_ai.fairness.llm.classifier import LLMClassifier, ToxigenRoberta


@pytest.fixture
def toxigen_roberta():
    return ToxigenRoberta()


def test_classifier_score(toxigen_roberta):
    scores = toxigen_roberta.score(["This is a test sentence.", "This is a second test sentence."])
    assert all(0 <= score <= 1 for score in scores)
