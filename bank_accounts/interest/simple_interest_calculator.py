from interfaces.interest_calculator import InterestCalculator


class SimpleInterestCalculator(InterestCalculator):
    def calculate_interest(self, balance):
        return balance * 0.01
