# Workflow
(*run.workflow*)

## Overview

### Available Operations

* [queue](#queue) - Workflow - Queue
* [sync](#sync) - Workflow - Sync
* [stream](#stream) - Workflow - Stream

## queue

Create a new workflow run with the given parameters.

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.workflow.queue(request={
        "workflow_id": "12345678-1234-5678-1234-567812345678",
        "workflow_api_json": {},
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

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.WorkflowRunRequest](../../models/components/workflowrunrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.QueueWorkflowRunRunWorkflowQueuePostResponse](../../models/operations/queueworkflowrunrunworkflowqueuepostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## sync

Create a new workflow run with the given parameters.

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.workflow.sync(request={
        "workflow_id": "12345678-1234-5678-1234-567812345678",
        "workflow_api_json": {},
        "inputs": {
            "prompt": "A beautiful landscape",
            "seed": 42,
        },
        "webhook": "https://myapp.com/webhook",
    })

    assert res.response_sync_workflow_run_run_workflow_sync_post is not None

    # Handle response
    print(res.response_sync_workflow_run_run_workflow_sync_post)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.WorkflowRunRequest](../../models/components/workflowrunrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.SyncWorkflowRunRunWorkflowSyncPostResponse](../../models/operations/syncworkflowrunrunworkflowsyncpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## stream

Create a new workflow run with the given parameters. This function sets up the run and initiates the execution process. For callback information, see [Callbacks](#tag/callbacks/POST/\{callback_url\}).

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.workflow.stream(request={
        "workflow_id": "12345678-1234-5678-1234-567812345678",
        "workflow_api_json": {},
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

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.WorkflowRunRequest](../../models/components/workflowrunrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.CreateRunWorkflowStreamRunWorkflowStreamPostResponse](../../models/operations/createrunworkflowstreamrunworkflowstreampostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |