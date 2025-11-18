#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from stock_picker.crew import StockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'sector': 'Science and Technology'
    }

    # create and run the crew
    result = StockPicker().crew().kickoff(inputs=inputs)

    # print the result
    print("\n\nFINAL DECISION\n\n")
    print(result.raw)

if __name__ == "__main__":
    run()