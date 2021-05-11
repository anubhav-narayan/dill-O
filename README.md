# dillO

A small dill wrapper with Metadata and Verification Hash

# Installation

## From Source
```bash
$ python3 setup.py install
```

## From `pip`
```bash
$ pip3 install dillO
```

# In-memory Storage
```python
from dillo import Dillo

file = Dillo('My dillO')
# some object instances as obj
file.store(obj)
```
# On File Storage
```python
from dillo import Dillo

file = Dillo('My dillO')
# some object instances as obj
file.store(obj)  # store the object `before` you write
file.write_file('./filename.dillO')  # write dillO files
```
# JSON
JSON Files
```python
from dillo import Dillo

file = Dillo('My dillO', type='json')
# some object instances as obj
file.store(obj)  # store the object `before` you write
file.write_file('./filename.json')  # write JSON files
```
JSON Strings
```python
from dillo import Dillo

file = Dillo('My dillO', type='json')
# some object instances as obj
file.store(obj)  # store the object `before` you write
file.json_string()  # get JSON string
```
JSON Objects
```python
from dillo import Dillo

file = Dillo('My dillO', type='json')
# some object instances as obj
file.store(obj)  # store the object `before` you write
file.json()  # get JSON Object
```
# Sample Files
dillO
```plaintext
-----METADATA-----
Name   : Array JSON
dillO  : pickle
Sign   : SHA256
Tags   : 
Length : 271 Bytes
-----DILLO-----
gASVBAEAAAAAAACMCmRpbGwuX2RpbGyUjA1fY3JlYXRlX2FycmF5lJOUKGgAjAlfZ2V0X2F0dHKUk5R
oAIwOX2ltcG9ydF9tb2R1bGWUk5SMHG51bXB5LmNvcmUuX211bHRpYXJyYXlfdW1hdGiUhZRSlIwMX3
JlY29uc3RydWN0lIaUUpSMBW51bXB5lIwHbmRhcnJheZSTlEsAhZRDAWKUh5QoSwFLBYWUaA2MBWR0e
XBllJOUjAJpOJSJiIeUUpQoSwOMATyUTk5OSv____9K_____0sAdJRiiUMoAQAAAAAAAAACAAAAAAAA
AAMAAAAAAAAABAAAAAAAAAAFAAAAAAAAAJR0lE50lFKULg==
-----SIGN-----
1ac33161cd72c5ce8ec286ea322a02372e1d759a6724f64d33417ac8274d2808
```
JSON
```json
{"py/object": "dillo.dillo.Dillo", "name": "Array JSON", "type": "json", "sign": "SHA256", "protocol": null, "byref": false, "fmode": 2, "recurse": false, "_stream": {"py/b64": "gASVBAEAAAAAAACMCmRpbGwuX2RpbGyUjA1fY3JlYXRlX2FycmF5lJOUKGgAjAlfZ2V0X2F0dHKUk5RoAIwOX2ltcG9ydF9tb2R1bGWUk5SMHG51bXB5LmNvcmUuX211bHRpYXJyYXlfdW1hdGiUhZRSlIwMX3JlY29uc3RydWN0lIaUUpSMBW51bXB5lIwHbmRhcnJheZSTlEsAhZRDAWKUh5QoSwFLBYWUaA2MBWR0eXBllJOUjAJpOJSJiIeUUpQoSwOMATyUTk5OSv////9K/////0sAdJRiiUMoAQAAAAAAAAACAAAAAAAAAAMAAAAAAAAABAAAAAAAAAAFAAAAAAAAAJR0lE50lFKULg=="}, "ignore": false, "tags": {"py/set": []}, "hash": {"py/b64": "MWFjMzMxNjFjZDcyYzVjZThlYzI4NmVhMzIyYTAyMzcyZTFkNzU5YTY3MjRmNjRkMzM0MTdhYzgyNzRkMjgwOA=="}}
```
# License [MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Anubhav Mattoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.