"""Exceptions for pyhaversion."""


class HaVersionException(Exception):
    """Base pyhaversion exception."""


class HaVersionInputException(HaVersionException):
    """Raised when missing required input."""


class HaVersionFetchException(HaVersionException):
    """Raised there are issues fetching information."""


class HaVersionNotModifiedException(HaVersionFetchException):
    """Raised when the content is not modified."""


class HaVersionTimeoutException(HaVersionFetchException):
    """Raised when the content fetching timed out."""


class HaVersionParseException(HaVersionException):
    """Raised there are issues parsing information."""
