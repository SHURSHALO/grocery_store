from enum import Enum


class JWTAuthSettings(Enum):
    """Костанты для конфигураций jwt аутентификации."""

    JWT_ACCESS_DURATION = 3600  # seconds
    JWT_ACCESS_HEADER = "Authorization"
    JWT_ALGORITHM = "HS256"
    JWT_COOKIE_HTTPONLY = True
    JWT_COOKIE_SAMESITE = "Strict"
    JWT_COOKIE_SECURE = True
    JWT_LOGOUT_ACCESS = True
    JWT_REFRESH_DURATION = 36000  # seconds
    JWT_REFRESH_PATH = "/users/refresh/"
