from pathlib import Path

FMT= '%Y-%m-%dT%H:%M:%S'

RUN_SCRIPT = 'run.sh'
RUNS_DIR = 'runs'
STATE_FILE = 'STATE'

SUCCESS_PATH = 'SUCCESS'
FAILURE_PATH = 'FAILURE'

LOGS_DIR = Path('logs')
OUT_PATH = LOGS_DIR / 'out'
ERR_PATH = LOGS_DIR / 'err'

LOCK_FILE_NAME = '.LOCK'

CRON_MODULE_RC = '.cron-module-rc'
CRON_MODULE_RC_ENV = 'CRON_MODULE_RC'
