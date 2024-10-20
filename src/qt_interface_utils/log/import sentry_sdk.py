import sentry_sdk

sentry_sdk.init(
    dsn="https://0b977b472f689dad77f6a1ef815b71b4@o4508155839578112.ingest.de.sentry.io/4508155841544272",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


import time

time.sleep(1)

a = 7 / 0
