# Deployment
(*run.deployment*)

## Overview

### Available Operations

* [queue](#queue) - Deployment - Queue
* [sync](#sync) - Deployment - Sync
* [stream](#stream) - Deployment - Stream

## queue

Create a new deployment run with the given parameters.

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.deployment.queue(request={
        "deployment_id": "15e79589-12c9-453c-a41a-348fdd7de957",
        "inputs": {
            "prompt": "A beautiful landscape",
            "seed": 42,
        },
        "webhook": "https://myapp.com/webhook",
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

## sync

Create a new deployment run with the given parameters.

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.deployment.sync(request={
        "deployment_id": "15e79589-12c9-453c-a41a-348fdd7de957",
        "inputs": {
            "prompt": "A beautiful landscape",
            "seed": 42,
        },
        "webhook": "https://myapp.com/webhook",
    })

    assert res.response_sync_deployment_run_run_deployment_sync_post is not None

    # Handle response
    print(res.response_sync_deployment_run_run_deployment_sync_post)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.DeploymentRunRequest](../../models/components/deploymentrunrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.SyncDeploymentRunRunDeploymentSyncPostResponse](../../models/operations/syncdeploymentrunrundeploymentsyncpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## stream

Create a new deployment run with the given parameters. This function sets up the run and initiates the execution process. For callback information, see [Callbacks](#tag/callbacks/POST/\{callback_url\}).

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.deployment.stream(request={
        "deployment_id": "15e79589-12c9-453c-a41a-348fdd7de957",
        "inputs": {
            "prompt": "A beautiful landscape",
            "seed": 42,
        },
        "webhook": "https://myapp.com/webhook",
    })

    assert res.run_stream is not None

    with res.run_stream as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.DeploymentRunRequest](../../models/components/deploymentrunrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.CreateRunDeploymentStreamRunDeploymentStreamPostResponse](../../models/operations/createrundeploymentstreamrundeploymentstreampostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |