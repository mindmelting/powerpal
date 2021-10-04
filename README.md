# powerpal

_This repository and package is not affiliated with Powerpal_

Simple Python package for making calls to the Powerpal Readings API.

## Installation

```bash
pip install mindmelting.powerpal
```

## Usage

```python
from aiohttp import ClientSession
from mindmelting.powerpal import Powerpal
from mindmelting.powerpal.exceptions import (
    PowerpalException,
    PowerpalAuthorizationException,
    PowerpalAuthenticationException
)

EXAMPLE_AUTH_KEY = 'xyz123' # Your Powerpal API authorization key
EXAMPLE_DEVICE_ID = 'abc123' # Your Powerpal device ID

session = ClientSession()

powerpal = Powerpal(session, EXAMPLE_AUTH_KEY, EXAMPLE_DEVICE_ID)

async def get_powerpal_data(self):
    try:
        return await powerpal.get_data()
    
    except PowerpalAuthenticationException as exception:
        # 401 - Authorization key is invalid
        ...
    except PowerpalAuthorizationException as exception:
        # 403 - Device Id is invalid
        ...
    except PowerpalException as exception:
        # All other exceptions
        ...
```
