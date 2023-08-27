from fastapi import FastAPI

import sentry_sdk


sentry_sdk.init(
    dsn="https://56e1183e99a8d6fb29d18c3ad1aabd5a@o4505250926559232.ingest.sentry.io/4505761003864064",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI(
    title='First our app',
    description='we are the champions',
    version='0.0.1',
    debug=True,
)


@app.get('/')
@app.post('/')
async def main_page() -> dict:
    return {'greeting': 'HELLO MY FRIEND!!!!'}


@app.get('/{user_name}')
@app.get('/{user_name}/{user_nick}')
async def user_page(user_name: str, user_nick: str = '', limit: int = 10, skip: int = 0) -> dict:
    data = [i for i in range(1000)][skip:][:limit]

    return {'user_name': user_name, 'user_nick': user_nick, 'data': data}
