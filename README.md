Tech Stack
Python, PyTest
Selenium
html Report
Parallel Run with xdist

Install the dependencies
pip install selenium
pip install pytest
pip install pytest html

To run the Framework
pytest -s -v testCases/test_Case.py

To generate html Report
pytest -s -v --html=Reports/reports.html testCases/test_Case.py