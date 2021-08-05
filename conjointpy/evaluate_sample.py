"""
A few approaches to evaluate the necessary sample size for a conjoint analysis
"""

from abc import ABC, abstractmethod
import pymc3 as pm


class EvaluateSample(ABC):
    """Top-level class to hold methods common to all sample evaluation children"""

    @abstractmethod
    def compute_samples(self):
        pass


class HierarchicalBayes(EvaluateSample):
    """Implementation of hierarchical Bayes simulation to estimate significance"""

    def __init__(
        self,
        features: list,
        levels: dict,
        est_means: dict,
    ) -> None:
        self.features = features
        self.levels = levels
        self.est_means = est_means


class SawtoothEstimate(EvaluateSample):
    """Implementation of the basic Sawtooth estimate for sample size"""

    def __init__(
        self,
        levels: dict,
        q_range: list,
        a_range: list,
    ) -> None:
        self.levels = levels
        self.q_range = q_range
        self.a_range = a_range

    def compute_samples(self):
        """
        Compute the necessary sample size using the Sawtooth approach:
        n >= 1000 * c / (q * a)
        n: sample size
        c: maximum number of levels of any feature
        q: number of questions that you'll ask a respondent
        a: number of possible options you'll show the respondent
        """
        # Empty list (will contain all possible combinations)
        sample_size = []
        # Maximum number of levels for a feature
        max_level = max(len(v) for v in self.levels.values())
        # Loop through possible number of answers you'll show the respondent
        for i in self.a_range.sort():
            # Loop through possible number of questions respondent will answer
            for j in self.q_range.sort():
                # Append tuple of answers, questions and resultant sample minimum
                sample_size.append((i, j, 1000.0 * max_level / i * j))
