# strongDM SDK for Python

The official strongDM SDK for the Python programming language.

## Quick Start

First, install the library:

```bash
$ pip install strongdm
```

Next, go to https://app.strongdm.com and create an API key. Set the `SDM_API_ACCESS_KEY` and `SDM_API_SECRET_KEY` environment variables.

```bash
$ export SDM_API_ACCESS_KEY=<YOUR ACCESS KEY>
$ export SDM_API_SECRET_KEY=<YOUR SECRET KEY>
```

Run some example code.

```python
import strongdm

# listUsers.py enumerates all users of an organization
# usage:
# python3 listUsers.py
def main():
    client = strongdm.Client(os.getenv("SDM_API_ACCESS_KEY"),
                        os.getenv("SDM_API_SECRET_KEY"))

    users = client.accounts.list('')
    for user in users:
        print(user)


if __name__ == "__main__":
    main()
```



<!-- Checkout our [release notes](https://github.com/aws/aws-sdk-go/releases) for
information about the latest bug fixes, updates, and features added to the SDK. -->