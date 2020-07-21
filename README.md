# strongDM SDK for Python

This is the official [strongDM](https://www.strongdm.com/) SDK for the Python programming language.

## Installation

```bash
$ pip install strongdm
```

## Authentication

If you don't already have them you will need to generate a set of API keys, instructions are here: [API Credentials](https://www.strongdm.com/docs/admin-guide/api-credentials/)

Add the keys as environment variables; the SDK will need to access these keys for every request.
```bash
$ export SDM_API_ACCESS_KEY=<YOUR ACCESS KEY>
$ export SDM_API_SECRET_KEY=<YOUR SECRET KEY>
```

## List Users
The following code lists all registered users:

```python
import os
import strongdm

def main():
    client = strongdm.Client(os.getenv("SDM_API_ACCESS_KEY"),
                        os.getenv("SDM_API_SECRET_KEY"))

    users = client.accounts.list('')
    for user in users:
        print(user)

if __name__ == "__main__":
    main()
```

## Useful Links

* Documentation:  [strongdm package](https://strongdm.github.io/strongdm-sdk-python-docs/)
* Examples: [GitHub - strongdm/strongdm-sdk-python-examples](https://github.com/strongdm/strongdm-sdk-python-examples)

## License

[Apache 2](https://github.com/strongdm/strongdm-sdk-python/blob/master/LICENSE)

## Contributing 

Currently, strongDM does not accept pull requests for this repository. Please submit any feedback to <support@strongdm.com>.