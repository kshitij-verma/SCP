from plugin.operator.core.services.operator import OperatorBase


class DivOperator(OperatorBase):
    """
    The concrete implementation of division operator.

    The OperatorBase class is provided by the Core component.
    """

    def operator_name(self):
        return "Division"

    def operator_identifier(self):
        return "DivisionOperation"

    def operation(self, number1, number2):
        return number1 / number2
