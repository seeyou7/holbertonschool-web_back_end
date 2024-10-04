#!/usr/bin/python3

from typing import List, TypeVar

class Auth:
    """ Authentication class """
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method will later be used to determine if a request should be
        authenticated based on the path. For now, it just returns False.
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """
        This method will return None for now. In the future, it will extract
        the authorization header from the request.
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method will return None for now. Later, it will return the current
        authenticated user.
        """
        return None
