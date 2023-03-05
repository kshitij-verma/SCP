from setuptools import setup, find_packages

setup(
    name="operation_division",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['plugin', 'plugin.operator'],
    # "div" entry point belongs to the "core.operator" group
    # and it represents the alias for the DivOperator class.
    entry_points={
        'core.operator': [
            'div = plugin.operator.division.div_operator:DivOperator'
        ],
    },
    zip_safe=True
)
