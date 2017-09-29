# -*- coding: utf-8 -*-

from . import const

from .metrics import (
    Timer
)

from .logging import (
    setup_logging,
    get_logger,
    log_with_success,
)

from .collect import (
    collect
)

from .enums import (
    Comparison,
    Method,
    Status,
)

from .namespace import (
    Namespace,
)

from .config import (
    Config,
    Profile
)

from .model import (
    Case,
    Step,
    Suite,
    Validator,
)

from .state import (
    Runner,
    SuiteResult,
)

from .execute import (
    execute
)

from .reporting import (
    ReportEngine
)

from .cli import (
    main
)


__all__ = [
    # const.py
    "const",

    # metrics.py
    "Timer",

    # logging.py
    "setup_logging",
    "get_logger",
    "log_with_success",

    # collect.py
    "collect",

    # enums.py
    "Comparison",
    "Method",
    "Status",

    # execute.py
    "execute",

    # namespace.py
    "Namespace",

    # config.py
    "Config",
    "Profile",

    # model.py
    "Case",
    "Step",
    "Suite",
    "Validator",

    # reporting.py
    "ReportEngine",

    # state.py
    "Runner",
    "SuiteResult",

    # cli.py
    "main",
]


__author__ = """Ian Maurer"""
__email__ = 'ian@genomoncology.com'
__version__ = '0.2.2'

__uri__ = "http://www.github.com/genomoncology/rigor"
__copyright__ = "Copyright (c) 2017 genomoncology.com"
__description__ = "Rigor: REST API Testing"
__doc__ = __description__ + " <" + __uri__ + ">"
__license__ = "MIT"
__title__ = "rigor"
