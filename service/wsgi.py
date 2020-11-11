import os

import sentry_sdk
from api import create_app
from sentry_sdk.integrations.flask import FlaskIntegration

SENTRY_DSN = os.environ.get("SENTRY_DSN")

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN, integrations=[FlaskIntegration()], traces_sample_rate=0
    )

app = create_app()
