# Module 2: Working with Electronic Data Files

- Pandas `read_csv`, `read_table`, etc. read most tabular data files, including Excel, SAS, and SPSS files.
- The `pd.read_csv` `chunksize` parameter allows you to load files incrementally, which is useful when they're too large to fit in memory.
- The `s3fs` package allows for reading/writing files from/to Amazon S3.
- `df.describe()` returns the count, mean, standard deviation, min, max, and quartiles of the numeric columns in a data frame.
- `df.pop('columnname')` can be used to remove a column from a data frame.