# Deployment
(*run.deployment*)

### Available Operations

* [queue](#queue) - Deployment - Queue
* [sync](#sync) - Deployment - Sync
* [stream](#stream) - Deployment - Stream

## queue

Create a new deployment run with the given parameters.

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.deployment.queue(request={
    "deployment_id": "12345678-1234-5678-1234-567812345678",
    "inputs": {
        "num_inference_steps": 30,
        "prompt": "A futuristic cityscape",
        "seed": 123456,
    },
    "webhook": "https://myapp.com/webhook",
    "webhook_intermediate_status": True,
})

if res.create_run_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.DeploymentRunRequest](../../models/components/deploymentrunrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.QueueDeploymentRunRunDeploymentQueuePostResponse](../../models/operations/queuedeploymentrunrundeploymentqueuepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## sync

Create a new deployment run with the given parameters.

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.deployment.sync(request={
    "deployment_id": "12345678-1234-5678-1234-567812345678",
    "inputs": {
        "num_inference_steps": 30,
        "prompt": "A futuristic cityscape",
        "seed": 123456,
    },
    "webhook": "https://myapp.com/webhook",
    "webhook_intermediate_status": True,
})

if res.response_sync_deployment_run_run_deployment_sync_post is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.DeploymentRunRequest](../../models/components/deploymentrunrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.SyncDeploymentRunRunDeploymentSyncPostResponse](../../models/operations/syncdeploymentrunrundeploymentsyncpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## stream

Create a new deployment run with the given parameters. This function sets up the run and initiates the execution process. For callback information, see [Callbacks](#tag/callbacks/POST/\{callback_url\}).

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.deployment.stream(request={
    "deployment_id": "12345678-1234-5678-1234-567812345678",
    "inputs": {
        "num_inference_steps": 30,
        "prompt": "A futuristic cityscape",
        "seed": 123456,
    },
    "webhook": "https://myapp.com/webhook",
    "webhook_intermediate_status": True,
})

if res.run_stream is not None:
    for event in res.run_stream:
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

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |
