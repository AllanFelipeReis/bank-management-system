from interfaces.interest_calculator import InterestCalculator


class CompoundInterestCalculator(InterestCalculator):
    def calculate_interest(self, balance):
        return balance * 0.05
