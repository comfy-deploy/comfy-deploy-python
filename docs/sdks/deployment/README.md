# Deployment
(*run.deployment*)

## Overview

### Available Operations

* [queue](#queue) - Queue Run

## queue

Create a new deployment run with the given parameters.

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.deployment.queue(request={
        "inputs": {
            "num_inference_steps": 30,
            "prompt": "A futuristic cityscape",
            "seed": 123456,
        },
        "webhook": "https://myapp.com/webhook",
        "deployment_id": "12345678-1234-5678-1234-567812345678",
    })

    assert res.create_run_response is not None

    # Handle response
    print(res.create_run_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.DeploymentRunRequest](../../models/components/deploymentrunrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.QueueDeploymentRunRunDeploymentQueuePostResponse](../../models/operations/queuedeploymentrunrundeploymentqueuepostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |