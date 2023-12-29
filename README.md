<a name="readme-top"></a>
<br />
<div align="center">
  <h3 align="center">MBB Savings/Current Account Statement Parser (PDF to CSV)</h3>
  <p>
    Parser for MBB monthly Savings/Current Account Statement. Converts PDF statement into CSV. Based on <a href="https://github.com/Rexpert/TNG_Statement_in_CSV">TNG Statement in CSV by Rexpert</a>
  </p>
  <p>
    <i>Disclaimer: Not extensively tested. Not affliated with MBB.</i>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About the Project

Simple parser to convert MBB's PDF monthly current/savings account statement to CSV. 

<!-- GETTING STARTED -->

### Getting Started

1. Clone this repository or just download the python file
    ```
    git clone https://github.com/far1ez/parserMBBStatement.git
    ```
2. You need to install [Python 3](https://www.python.org/) and its relevant dependencies:
    <details>
      <summary>
        camelot-py: to read statement table from PDF
      </summary>
      
      - Installation via `pip`
        ```
        pip install camelot-py[cv]
        ```
      - or if you're using conda environment
        ```
        conda install -c conda-forge camelot-py
        ```
      - Detail installation please refer to `camelot-py` [Documentation](https://camelot-py.readthedocs.io/en/master/) 
    </details>
    <details>
      <summary>
        pandas: data manipulation
      </summary>
      
      - Installation via `pip`
        ```
        pip install pandas
        ```
      - or if you're using conda environment
        ```
        conda install -c conda-forge pandas
        ```
      - Detail installation please refer to `pandas` [Documentation](https://pandas.pydata.org/docs/index.html) 
    </details>
    <details>
      <summary>
        PyPDF2: PDF operations
      </summary>
      
      - Installation via `pip`
        ```
        pip install PyPDF2
        ```
      - or if you're using conda environment
        ```
        conda install -c conda-forge PyPDF2
        ```
    </details>
    <details>
      <summary>
        PyCryptodome: to decrypt PDF
      </summary>
      
      - Installation via `pip`
        ```
        pip install PyCryptodome
        ```
      - or if you're using conda environment
        ```
        conda install -c conda-forge PyCryptodome
        ```
    </details>
3. Download your MBB current/savings account statement
4. Run [mbb_statement_parser.py](mbb_statement_parser.py)
    ```
    python mbb_statement_parser.py -pw <PDF password> <statement filename>
    ```
5. If no errors, the corresponding CSV file will be generated in the same directory
   <i>(parser will overwrite any existing file)</i>

<!-- ADDITIONAL USAGE -->
## Additional Usage

1. You can convert more than 1 file at once
   ```
   python mbb_statement_parser.py -pw <password> statement1.pdf statement2.pdf
   ```
2. You can mass convert statements!
   ```
   python mbb_statement_parser.py -pw <password> *.pdf
   ```

<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog

<!-- LICENSE -->
## License

Distributed under the MIT License

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Fariez - [@far1ez](https://twitter.com/far1ez) - me@fariez.com

Project Link: [https://github.com/far1ez/parserMBBStatement](https://github.com/far1ez/parserMBBStatement)

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Rexpert's TNG Statement in CSV](https://github.com/Rexpert/TNG_Statement_in_CSV)
