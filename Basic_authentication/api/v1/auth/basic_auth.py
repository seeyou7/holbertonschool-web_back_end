#!/usr/bin/env python3
"""
Basic Authentication module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic authentication class that inherits from Auth.
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Extracts the Base64 part of the
            Authorization header for Basic Auth.
        """
        # Check if authorization_header is None or not a string
        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        # Check if the authorization header starts with "Basic "
        if not authorization_header.startswith("Basic "):
            return None

        # Return the Base64 part after "Basic "
        return authorization_header[len("Basic "):]
