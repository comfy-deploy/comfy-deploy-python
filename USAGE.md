<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from comfydeploy import ComfyDeploy
import os

s = ComfyDeploy(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
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
import os

async def main():
    s = ComfyDeploy(
        bearer_auth=os.getenv("BEARER_AUTH", ""),
    )
    res = await s.run.get_async(run_id="<value>")
    if res.object is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->