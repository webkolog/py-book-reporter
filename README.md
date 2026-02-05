# Book Reporter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![CI: GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-brightgreen.svg)](https://github.com/webkolog/py-book-reporter/actions)

**Version:** 1.0  
**Last Updated:** 2026-02-06  
**Compatibility:** Python 3.7+  
**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))  
**Website:** [http://webkolog.net](http://webkolog.net)  
**Copyright:** (c) 2026 Ali Candan  
**License:** MIT License

**Book Reporter** is an all-in-one data tool that automatically scrapes book data from the "Books to Scrape" platform, generates reports in CSV and Excel formats, and serves this data through a REST API.

---

## Features

* **Web Scraping:** Instantly collects book titles and prices.
* **Multi-Format Reporting:** Automatically saves data into both `.csv` and `.xlsx` formats.
* **REST API:** Provides access to the collected data in JSON format via a URL.
* **Dockerized:** Ready to run in any environment using containerization.
* **CI/CD Ready:** Includes GitHub Actions integration for automated testing.

---

## Installation

### Local Setup
1. Install the required dependencies:
```bash
pip install -r requirements.txt
```
   
2. Run the application:
```bash
python book_reporter.py
```

### Docker Setup
Run the project without any local installation using Docker:
```bash
docker-compose up --build
```
---
## Usage
1. Automation & Reporting
As soon as the application starts, the `generate_report()` function triggers and creates the following files in the root directory:

- `book_report.csv` (Semicolon separated, UTF-8-SIG)

- `book_report.xlsx` (Excel format)

2. API Access
While the application is running, you can access live data through:

- **Endpoint:** `GET http://127.0.0.1:5000/api/books`

---
## Testing
The project uses **Pytest** for unit and integration testing. To run the tests manually:
```bash
pytest test_book_reporter.py
```

---
## Dependencies
This project relies on the following core libraries:
- `Requests`: For handling HTTP requests.

- `BeautifulSoup4`: For parsing HTML content.

- `Pandas & Openpyxl`: For data manipulation and Excel reporting.

- `Flask`: For serving the REST API.

---
## License
This **Book Reporter** project is open-source software licensed under the MIT License.
```
MIT License

Copyright (c) 2026 Ali Candan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---
## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

---
## Support
For any questions or support regarding the **Book Reporter**, you can refer to the project's GitHub repository or contact the author.

