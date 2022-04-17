# SP500 Index Fund
Alternative version of the SP500 where each company has the same weight and user gets to decide the portfolio value.
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
9. Create virtual environment:
```console
python -m venv {current_path}/venv
```
10. Activate virtual environment:
```console
venv\scripts\activate
```
11. Install dependencies:
```console
pip install -r requirements.txt
```
12. Run script:
```console
python sp500.py
```
13. Input the value of the portfolio into the console.
14. Open SP500.xlsx and take a look!
