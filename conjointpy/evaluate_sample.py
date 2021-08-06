"""
A few approaches to evaluate the necessary sample size for a conjoint analysis
"""

from abc import ABC, abstractmethod
import pymc3
import numpy


class EvaluateSample(ABC):
    """Top-level class to hold methods common to all sample evaluation children"""

    @abstractmethod
    def compute_samples(self) -> list:
        """Compute all requisite sample sizes given parameters"""
        pass

    @abstractmethod
    def export_table(self) -> None:
        """Write out a table showing parameter combinations and resultant sample size requirements"""
        pass


class HierarchicalBayes(EvaluateSample):
    """Implementation of Hierarchical Bayes analysis on simulation data to estimate significance"""

    def __init__(
        self,
        features: list,
        levels: dict,
        est_means: dict,
        est_error: dict = None,
        n_range: list = [50, 200, 500, 1000],
    ) -> None:
        self.features = features
        self.levels = levels
        self.est_means = est_means
        self.est_error = est_error
        if self.est_error = None:
            self.default_error()
        self.n_range = n_range

    def default_error(self):
        """Sets a default standard """
        reset_error = {}
        for i in self.features:
            tmp = [1 for j in self.levels[i]]
            reset_error[i] = tmp

    def compute_samples(self):
        """
        Provide an estimated distribution for a given sample size using hierarchical bayes method
            -features: categories that we are testing in the CA
            -levels: options within a feature
            -est_means: estimated utility of each level within a feature
            -n_range: sample sizes in consideration
        """
        # We perform this analysis for each requested sample size
        for i in self.n_range:
            # Call our hierarchical_bayes method for this sample size
            self.hierarchical_bayes(i)
            # Examine the mean and standard deviation of each feature-level pair

    def simulate_sample(self, n) -> list:
        """Generate simulated choice data using estimated weights and deviations"""
        pass

    def hierarchical_bayes(self, n):
        """Analyze the distribution of all levels provided n respondents"""

        # Loop through each feature
        for i in self.features:
            # And each level
            for l_name, l_mean, l_sd in zip(
                self.levels[i], self.est_means[i], self.est_error[i]
            ):
                # Simulate a sample given the provided estimated statistics
                self.simulate_sample(n)
                # Unique label for any feature-level-n-respondent combination
                label = str(i) + "_" + str(l_name) + "_" + str(n) + "_"
                # Instantiate the pymc3 model
                with pymc3.Model():
                    # Generate a Normal distribution for each respondent provided an estimated mean and standard deviation
                    respondents = [
                        pymc3.Normal(label + k, mu=l_mean, sd=l_sd) for k in range(n)
                    ]

    def export_table(self):
        return super().export_table()


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

    def export_table(self):
        """Write parameter and sample size combinations to .csv file"""
        return super().export_table()
