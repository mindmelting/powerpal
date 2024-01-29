# powerpal

_This repository and package is not affiliated with Powerpal._

Simple Python package for making calls to the Powerpal Readings API.

Credit to [forfuncsake](https://github.com/forfuncsake) for the go client which this is influenced from: [https://github.com/forfuncsake/powerpal](https://github.com/forfuncsake/powerpal)

## Installation

```bash
pip install mindmelting.powerpal
```

## Usage

### Live data

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

### Historical time-series data

#### With no arguments

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

async def get_powerpal_time_series_data(self):
    try:
        return await powerpal.get_time_series_data()
    
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

#### With arguments

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

async def get_powerpal_time_series_data(self, start: int, end: int, sample: int):
    try:
        return await powerpal.get_time_series_data(
            start=start, # unix timestamp of start time, e.g., 1706321820 for Sat Jan 27 2024 02:17:00 GMT+0000
            end=end, # unix timestamp of end time, e.g., 1706332620 for Sat Jan 27 2024 05:17:00 GMT+0000
            sample=sample # sample (in minutes) to "bucket" readings, e.g., 60 for 1 hour interval
        )
    
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