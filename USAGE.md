<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id="<value>")

if res.object is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from comfydeploy import ComfyDeploy

async def main():
    s = ComfyDeploy(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.run.get_async(run_id="<value>")
    if res.object is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->