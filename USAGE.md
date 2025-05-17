<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.get(run_id="faf49b3a-7b64-4687-95c8-58ca8a41dd73")

    assert res.workflow_run_model is not None

    # Handle response
    print(res.workflow_run_model)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from comfydeploy import ComfyDeploy

async def main():

    async with ComfyDeploy(
        bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as comfy_deploy:

        res = await comfy_deploy.run.get_async(run_id="faf49b3a-7b64-4687-95c8-58ca8a41dd73")

        assert res.workflow_run_model is not None

        # Handle response
        print(res.workflow_run_model)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->