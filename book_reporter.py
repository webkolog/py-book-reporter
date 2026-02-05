"""
Book Reporter
=====================
File: book_reporter.py
Author: Ali Candan [Webkolog] <webkolog@gmail.com> 
Homepage: http://webkolog.net
GitHub Repo: https://github.com/webkolog/py-book-reporter
Last Modified: 2026-02-06
Created Date: 2026-02-06
Compatibility: Python 3.7+  
@version     1.0

Copyright (C) 2026 Ali Candan
Licensed under the MIT license http://mit-license.org

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

----

Let me add a small note: although I'm Turkish, the reason I don't normally write explanations and code in Turkish is because I need to write in a common language so that my foreign colleagues can understand this document and code. Since English is the common language of programmers, isn't that perfectly normal? ;)
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

def scrape_data():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []
    # Find each book title on the site
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']
        # Remove the Â£ symbol when retrieving the price
        price = article.find('p', class_='price_color').text.replace('Â£', '')
        books.append({"Title": title, "Price": price})
    return books

# 1. AUTOMATION: Report Generation Function
def generate_report():
    data = scrape_data()
    df = pd.DataFrame(data)
    df.to_csv('book_report.csv', sep=';', index=False, encoding='utf-8-sig')
    print("The report was successfully saved as 'book_report.csv'!")
    df.to_excel('book_report.xlsx', index=False)
    print("The report was successfully saved as 'book_report.xlsx'!")

# 2. API: Serving data via URL
@app.route('/api/books', methods=['GET'])
def get_books():
    data = scrape_data()
    return jsonify(data)

if __name__ == '__main__':
    # Generate a report first when the code runs
    generate_report()
    # Then start the API server (http://127.0.0.1:5000/api/books)
    app.run(debug=True)