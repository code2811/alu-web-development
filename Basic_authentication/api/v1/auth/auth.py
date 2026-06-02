#!/usr/bin/env python3
"""Auth module for managing API authentication."""
from typing import List, TypeVar
from flask import request


class Auth:
    """Template class for all authentication systems."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return True if the path requires authentication."""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Return the Authorization header value from the request."""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user from the request."""
        return None
