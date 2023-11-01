# MoneyProReport
The project provides applications to report data from MoneyPro App.

# Applications

## money_logger.py
The app reads the latest CSV file and generates money log files for all dates.

The latest CSV file is read from the data directory where files are sorted by file names. The CSV file is exported by the [Money Pro](https://money.pro/) App.

The log files are generated in the output directory, and each file is for
each date.

Usage 1: Generate all log files for all dates read from the latest CSV file. 

```
python money_logger.py
```

Usage 2: Generate one log file for the given date from the latest CSV file.
```
python money_logger.py -d 2023-09-15
```