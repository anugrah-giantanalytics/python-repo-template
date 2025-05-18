import logging
import sys
from typing import Any

import structlog
from structlog.stdlib import ProcessorFormatter

from app.core.config import settings


def setup_logging() -> None:
    """Configure structured logging for the application."""

    # Pre-chain processors
    pre_chain = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
    ]

    # Configure structlog
    structlog.configure(
        processors=pre_chain
        + [
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Create formatter
    formatter = ProcessorFormatter(
        processor=structlog.dev.ConsoleRenderer()
        if settings.DEBUG
        else structlog.processors.JSONRenderer(),
        foreign_pre_chain=pre_chain,
    )

    # Configure handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    # Set up root logger
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(settings.LOG_LEVEL.upper())

    # Disable other loggers
    for logger_name in logging.root.manager.loggerDict:
        if logger_name != __name__:
            logger = logging.getLogger(logger_name)
            logger.handlers = []
            logger.propagate = True


def get_logger(*args: Any, **kwargs: Any) -> structlog.BoundLogger:
    """Get a structured logger instance."""
    return structlog.get_logger(*args, **kwargs)
