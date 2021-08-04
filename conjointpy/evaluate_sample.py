"""
A few approaches to evaluate the necessary sample size for a conjoint analysis
"""

from typing import Optional
from abc import ABC, abstractmethod


class EvaluateSample(ABC):
    """Representation of the sample analysis class"""

    @abstractmethod
    def compute_combinations():
        """Compute the possible combinations of features and levels"""


class HierarchicalBayes(EvaluateSample):
	"""Implementation of hierarchical Bayes simulation to estimate significance"""
    def __init__(
        self,
        features: list,
        levels: dict,
        est_means: dict,
        q_range: list,
        a_range: list,
    ) -> None:
        self.features = features
        self.levels = levels
        self.est_means = est_means
        self.q_range = q_range
        self.a_range = a_range
