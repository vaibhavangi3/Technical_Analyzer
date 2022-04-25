# Nifty50 Technical Analysis

Using the Nifty50 Technical Analyzer, Investor can analyze Bullish or Bearish Candlestick for Nifty50 Instruments.

## Installation

1. Install a version of Python 3 (If you don't already have it on your system). Options include:

- (All operating systems) A download from [python.org](https://www.python.org/downloads/); typically use the Download Python 3.9.1 button that appears first on the page (or whatever is the latest version).

- (Linux) The built-in Python 3 installation works well, but to install other Python packages you must run `sudo apt install python3-pip` in the terminal.

- (macOS) An installation through [Homebrew](https://brew.sh/) on macOS using `brew install python3` (the system install of Python on macOS is not supported). 

If Python Extension is not Installed in your VSCode, it is recommended to install it first [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask.

```bash
pip install flask
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install yfinance.

```bash
pip install yfinance
```

For TA-lib, you can either use anaconda to install it or you can use the file present in the repo to install it for windows 64bit.

```bash
pip install TA_Lib-0.4.24-cp310-cp310-win_amd64.whl
```

Now, if the service got running for user, just open [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
