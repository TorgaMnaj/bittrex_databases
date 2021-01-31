
bittrex_database
----------------
is program for rebuilding and retrieving past nad current data on<br> 
all pairs from Bittrex.com.

- First we will install MariaDB and setup it.

Every following step is encapsulated in Docker:

- Main container (runs multiplied):
    - We'll create databases for 1, 5 and 60 minuts candlesticks</br>
      and create tables for each pair on Bittrex.com if not presented.</br>
      Each table has time as primary key and OHLC.
    - We will refill history of 60 min. candlesticks if tables are completelly empty.
    - We start filling up databases with realtime data from Bittrex.com</br>
      using Tor circuit.

- Side containers for:
    - Backing up data.
    - Checking and repairing data consistency.

Tor circuit is used because multiple containers s planned to run.</br>
Bittrex.com allowes only limited frequncy for data request. Yet</br>
please be nice and use only max. three instances of data retrieval</br>
dockers.
