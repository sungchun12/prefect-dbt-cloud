import requests
import asyncio
from prefect import flow, task


@task
async def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()


@flow(name="async_demo")
async def async_flow(url):
    fact_json = await call_api(url)
    return


if __name__ == "__main__":
    asyncio.run(async_flow("https://catfact.ninja/fact"))
