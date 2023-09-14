# Libraries
import numpy as np

# Calculation of the mean of a vector
def calculate_mean(vector):
    if len(vector) == 0:
        return "Vector is empty, cannot compute mean"  # Return None for an empty vector (undefined mean)
    else:
        total = sum(vector)
        mean_of_vector = total / len(vector)
        return mean_of_vector

# Example usage:
vector = [1, 2, 3, 4, 5]
result = calculate_mean(vector)
print("Mean:", result)


# Calculation of the standard deviation of a vector
def calculate_standard_deviation(vector):
    if len(vector) == 0:
        return "Vector is empty, cannot compute standard deviation"  # Return None for an empty vector (undefined mean)
    else:
        standard_deviation_np = np.std(vector)
        return standard_deviation_np
    
        