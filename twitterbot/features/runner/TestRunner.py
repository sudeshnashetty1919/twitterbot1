import os
import logging
from behave.__main__ import main

# Set up logging
logging.basicConfig(filename='behave_test_run.log', level=logging.INFO)


def run_behave_tests():
    # Change working directory to the project root (where 'features' folder is located)
    os.chdir('C:/Users/DELL/PycharmProjects/twitterbot')

    # Path to your feature files
    feature_path = 'features'

    # Additional options (optional)
    options = [

        '--tags', '~@skip',
        '--format', 'pretty',  # Output format (pretty, json, etc.)

    ]

    # Log the start of the test run
    logging.info("Starting Behave tests")

    # Run Behave tests
    result = main(options + [feature_path])  # Combine options with feature path

    # Log the result
    logging.info(f"Test run completed with exit code: {result}")
    print(f"Test run completed with exit code: {result}")


if __name__ == "__main__":
    run_behave_tests()
