"""
If the pytest library is not installed, install it by typing the following code in the terminal:
pip install pytest

To run the test, type the following command in the terminal:
python -m pytest
"""
import pytest
import os
from book_reporter import scrape_data, app

def test_scrape_data_structure():
    """Does the data fetching function return data in the correct format? """
    data = scrape_data()
    assert isinstance(data, list)
    if len(data) > 0:
        assert "Title" in data[0]
        assert "Price" in data[0]

def test_api_status():
    """Does the API endpoint return 200 OK?"""
    tester = app.test_client()
    response = tester.get('/api/books')
    assert response.status_code == 200
    assert response.is_json

def test_file_generation():
    """Are report files physically generated?"""
    # Let's manually trigger the report generation function during testing.
    from book_reporter import generate_report
    generate_report()
    assert os.path.exists('book_report.csv')
    assert os.path.exists('book_report.xlsx')