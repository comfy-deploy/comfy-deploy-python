# Run
(*run*)

### Available Operations

* [get](#get) - Get Run
* [~~queue~~](#queue) - Queue a workflow :warning: **Deprecated**
* [~~sync~~](#sync) - Run a workflow in sync :warning: **Deprecated**
* [~~stream~~](#stream) - Run a workflow in stream :warning: **Deprecated**
* [cancel_run_run_run_id_cancel_post](#cancel_run_run_run_id_cancel_post) - Cancel Run

## get

Get Run

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id="b18d8d81-fd7b-4764-a31e-475cb1f36591")

if res.workflow_run_model is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetRunRunRunIDGetResponse](../../models/operations/getrunrunrunidgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~queue~~

Create a new workflow run with the given parameters. This function sets up the run and initiates the execution process. For callback information, see [Callbacks](#tag/callbacks/POST/\{callback_url\}).

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.queue(request={
    "workflow_version_id": "a3ae2c73-d11b-402e-81da-06d33c2a9088",
    "inputs": {
        "prompt": "A beautiful landscape",
        "seed": 42,
    },
    "webhook_intermediate_status": True,
})

if res.create_run_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateRunQueueRunQueuePostData](../../models/operations/createrunqueuerunqueuepostdata.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.CreateRunQueueRunQueuePostResponse](../../models/operations/createrunqueuerunqueuepostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~sync~~

Create a new workflow run with the given parameters. This function sets up the run and initiates the execution process. For callback information, see [Callbacks](#tag/callbacks/POST/\{callback_url\}).

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.sync(request={
    "model_id": "<value>",
    "inputs": {
        "prompt": "A beautiful landscape",
        "seed": 42,
    },
    "webhook_intermediate_status": True,
})

if res.response_create_run_sync_run_sync_post is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateRunSyncRunSyncPostData](../../models/operations/createrunsyncrunsyncpostdata.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.CreateRunSyncRunSyncPostResponse](../../models/operations/createrunsyncrunsyncpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~stream~~

Create a new workflow run with the given parameters. This function sets up the run and initiates the execution process. For callback information, see [Callbacks](#tag/callbacks/POST/\{callback_url\}).

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.stream(request={
    "model_id": "<value>",
    "inputs": {
        "prompt": "A beautiful landscape",
        "seed": 42,
    },
    "webhook_intermediate_status": True,
})

if res.run_stream is not None:
    for event in res.run_stream:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreateRunStreamRunStreamPostData](../../models/operations/createrunstreamrunstreampostdata.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.CreateRunStreamRunStreamPostResponse](../../models/operations/createrunstreamrunstreampostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## cancel_run_run_run_id_cancel_post

Cancel Run

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.cancel_run_run_run_id_cancel_post(run_id="<value>", cancel_function_body={
    "function_id": "<value>",
})

if res.any is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `run_id`                                                                       | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `cancel_function_body`                                                         | [components.CancelFunctionBody](../../models/components/cancelfunctionbody.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |


### Response

**[operations.CancelRunRunRunIDCancelPostResponse](../../models/operations/cancelrunrunrunidcancelpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |
