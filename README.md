# SP500 Index Fund
Creates an equal weight portfolio using the companies in the SP500. The total value of the portfolio is decided by the user.
## API For Stock Data
IEX Cloud API Docs: https://iexcloud.io/docs/api/
## Running Script
1. Run Internet Explorer as administrator.
2. Go to: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
3. Click the lock on the top right beside the URL.
4. Click view certificates.
5. Click Install Certificates.
6. Click Next.
7. Click Next.
8. Click Finish.
9. Go to the folder location in console.
10. Create virtual environment:
```console
python -m venv {current_path}/venv
```
11. Activate virtual environment:
```console
venv\scripts\activate
```
12. Install dependencies:
```console
pip install -r requirements.txt
```
13. Run script:
```console
python sp500.py
```
14. Input the value of the portfolio.
15. Open sp500.xlsx and take a look!
