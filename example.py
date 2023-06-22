import asyncio
import danmaku


async def printer(q):
    while True:
        m = await q.get()
        print(m)


async def main():
    q = asyncio.Queue()
    dmc = danmaku.DanmakuClient("https://douyu.com/475252", q)
    asyncio.get_event_loop().create_task(printer(q))
    await dmc.start()


asyncio.get_event_loop().run_until_complete(main())
