# Stocks-Engine
---
# Requirements
* Python 3
* Colorama
* pip

# Installing dependencies

### Make sure you have pip3 installed!

You can check this by running `pip3 --version` in your command line or terminal.

Then install all pip dependencies with `pip3 install -r piprequirements.txt`


### Adding commands


As of 4/5/2024 these are the current commands:

* `buy` or `b`
  * Buys stocks.
  * Syntax:
    * buy {stock} {amount}
* `sell` or `s`
  * Sells stocks.
  * Syntax:
    * sell {stock} {amount}
* `inventory` or `i`
  * Lists all stocks and how many you own along with the current price.
* `price`
  * Check the price of a certain stock
  * Syntax:
    * Price:
    * price {stock}
* `balance` or `bal`
  * Tells you how much money you have. 
* `clear` or `cls`
  * Clears the terminal




### Adding stocks

Goto `stocktable.py` and add stocks to the `table` array.
After that, make `nametoid.py` match `stocktable.py`.
The first part of the list in `nametoid.py` is the name of the stock, the second part is the index of the stock in the array in `table`.

### Changing Colours
Change the colours in `colours.py`
E.g. if you want the input colour to be white, change `inputcolour = Fore.RED` to `inputcolour = Fore.WHITE`
