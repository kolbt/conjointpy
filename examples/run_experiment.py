"""
This file demonstrates the basic concepts of planning, running, and 
evaluating a Conjoint analysis test.
"""

import conjointpy

# List of the possible methods we can employ
methods = [
    "adaptive",
    "choice-based",
    "full-profile",
    "max-diff",
]

# What categories will we evaluate in this CA
categories = ["Price", "Weight", "Shipping Cost", "Color"]

# Options for each category (a dictionary with categories as keys)
options = {
    "Price": [5, 6, 7],
    "Weight": [2, 8],
    "Shipping Cost": [0, 10],
    "Color": ["White", "Black", "Blush Pink", "Seafoam Green"],
}

# Provide estimated mean values for each category and option
estimated_means = {
    "Price": [-2, -1, 0],
    "Weight": [0, 1],
    "Shipping Cost": [0, -1],
    "Color": [1, 1, 0, -1],
}

# We can also optionally pass the estimated errors
# estimated_errors = {}

# What is the range of questions we'd consider asking our respondent
question_range = range(10, 20 + 1)
# What are the range of alternatives we'd consider showing our respondent
alternative_range = range(3, 5 + 1)
# What range of respondents are we willing to consider
respondent_range = [50, 100, 200, 300, 400, 500, 1000]

# Generate sample size options using estimated means and hierarchical bayes
test_sample = conjointpy.evaluate_sample.HierarchicalBayes(
    features=categories,
    levels=options,
    est_means=estimated_means,
    n_range=respondent_range,
)

# We can export a table that looks at the different p-values
test_sample.sample_analysis()

# Write the (empty) excel file for the user to validate
my_ca = conjointpy.write_surveys(
    type="choice-based",
    categories=categories,
    options=options,
    path=None,
    filename="Widget CBC Conjoint",
)
