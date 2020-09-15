# Module 3: Working with JSON Data

Readings: [Importing Data into Pandas](https://www.datacamp.com/community/tutorials/importing-data-into-pandas), [Flatten Nested JSON Tutorial](https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas), *Surfing the Data Pipeline* [Ch. 3](https://jkropko.github.io/surfing-the-data-pipeline/ch3.html)

- JSON is a "data-interchange text-serialization format" often used to store unstructured data.
- JSON is built on two structures: a collection of key-value pairs (dictionary in Python) and an ordered list of values.
- JSON data can be nested, meaning that each key can have multiple keys associated with it.
- The `json_normalize` function can be used to flatten nested JSON data into a table.
  - The `record_path` arguments specifies which column to expand.
- The `json.loads(text_obj)` converts text into a JSON object that Python can recognize.