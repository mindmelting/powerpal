"""powerpal exceptions."""


class PowerpalException(Exception):
    """Base exception class for powerpal."""


class PowerpalAuthenticationException(PowerpalException):
    """Authentication error when calling powerpal API."""


class PowerpalAuthorizationException(PowerpalException):
    """Authorization error when calling powerpal API."""