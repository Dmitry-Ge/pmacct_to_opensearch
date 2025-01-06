Some instructions about transfer netflow data into OpenSearch
1. Create venv for your script
2. Add requirements:
```
pip install opensearch-py
```
3. Add to cronjob
```
pmacct some_options_here -o json | /your/path/to/python's/venv/python3 /path/to/script/processor.py
```
 
