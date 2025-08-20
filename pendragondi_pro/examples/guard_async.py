import asyncio
from pendragondi_api_pro import duplicate_guard_pro, get_event_log, export_html

@duplicate_guard_pro(window_ms=300)
async def guarded_async_call(x):
    print(f"Running async op with x={x}")
    await asyncio.sleep(0.1)
    return x

async def main():
    await guarded_async_call(42)
    await guarded_async_call(42)
    events = get_event_log().snapshot()
    export_html(events, "report_async.html")
    print(f"{len(events)} event(s) exported.")

if __name__ == "__main__":
    asyncio.run(main())