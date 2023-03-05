from setuptools import setup, find_packages

setup(
    name="operation_multiplication",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['plugin', 'plugin.operator'],
    # entry points to the plugin
    entry_points={
        # "mult" is the name of an entry point which belongs
        # to the "core.operator" group.
        # This entry point represents an alias for the MultOperator class.
        # See for more: https://stackoverflow.com/questions/774824/explain-python-entry-points
        'core.operator': [
            'mult = plugin.operator.multiplication.mult_operator:MultOperator'
        ],
    },
    zip_safe=True
)
