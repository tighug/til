# Requests

## Installation

=== "Poetry"

    ```bash
    poetry add requests
    poetry add -D types-requests
    ```

## Usage

```py
import requests

# CRUD
res = requests.get('https://api.github.com/events')
res = requests.post('https://httpbin.org/post', data={'key': 'value'})
res = requests.put('https://httpbin.org/put', data={'key': 'value'})
res = requests.delete('https://httpbin.org/delete')
res = requests.head('https://httpbin.org/get')
res = requests.options('https://httpbin.org/get')

# Response Object
res.text
res.content
res.status_code
```

## References

-   [公式ドキュメント](https://requests-docs-ja.readthedocs.io/en/latest/)
