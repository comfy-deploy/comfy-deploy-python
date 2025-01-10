<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id="b18d8d81-fd7b-4764-a31e-475cb1f36591")

if res.workflow_run_model is not None:
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
        bearer="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.run.get_async(run_id="58ccc65b-c928-4154-952e-30c048b8c2b5")
    if res.workflow_run_model is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->