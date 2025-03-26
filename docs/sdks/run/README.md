# Run
(*run*)

## Overview

### Available Operations

* [get](#get) - Get Run
* [cancel_run_run_run_id_cancel_post](#cancel_run_run_run_id_cancel_post) - Cancel Run

## get

Get Run

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.get(run_id="b888f774-3e7c-4135-a18c-6b985523c4bc")

    assert res.workflow_run_model is not None

    # Handle response
    print(res.workflow_run_model)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `run_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetRunRunRunIDGetResponse](../../models/operations/getrunrunrunidgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## cancel_run_run_run_id_cancel_post

Cancel Run

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.cancel_run_run_run_id_cancel_post(run_id="<id>", cancel_function_body={
        "function_id": "<id>",
    })

    assert res.any is not None

    # Handle response
    print(res.any)

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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |