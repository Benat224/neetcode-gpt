class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        result = init
        for i in range(iterations):
            result -= learning_rate * 2*result
        return round(result, 5)