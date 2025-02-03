# Session
(*session*)

## Overview

### Available Operations

* [get](#get) - Get Session
* [cancel](#cancel) - Delete Session
* [list](#list) - Get Machine Sessions
* [increase_timeout_session_increase_timeout_post](#increase_timeout_session_increase_timeout_post) - Increase Timeout
* [increase_timeout_2_session_session_id_increase_timeout_post](#increase_timeout_2_session_session_id_increase_timeout_post) - Increase Timeout 2
* [create](#create) - Create Session
* [snapshot_session_session_session_id_snapshot_post](#snapshot_session_session_session_id_snapshot_post) - Snapshot Session

## get

Get Session

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.session.get(session_id="<id>")

    assert res.session is not None

    # Handle response
    print(res.session)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetSessionSessionSessionIDGetResponse](../../models/operations/getsessionsessionsessionidgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## cancel

Delete Session

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.session.cancel(session_id="<id>")

    assert res.delete_session_response is not None

    # Handle response
    print(res.delete_session_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteSessionSessionSessionIDDeleteResponse](../../models/operations/deletesessionsessionsessioniddeleteresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list

Get Machine Sessions

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.session.list()

    assert res.response_get_machine_sessions_sessions_get is not None

    # Handle response
    print(res.response_get_machine_sessions_sessions_get)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `machine_id`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetMachineSessionsSessionsGetResponse](../../models/operations/getmachinesessionssessionsgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## increase_timeout_session_increase_timeout_post

Increase Timeout

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.session.increase_timeout_session_increase_timeout_post(request={
        "machine_id": "<id>",
        "session_id": "d1cbd355-89fb-45f4-9778-6137629fc60d",
        "timeout": 465465,
        "gpu": "<value>",
    })

    assert res.any is not None

    # Handle response
    print(res.any)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.IncreaseTimeoutBody](../../models/components/increasetimeoutbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.IncreaseTimeoutSessionIncreaseTimeoutPostResponse](../../models/operations/increasetimeoutsessionincreasetimeoutpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## increase_timeout_2_session_session_id_increase_timeout_post

Increase Timeout 2

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.session.increase_timeout_2_session_session_id_increase_timeout_post(session_id="<id>", increase_timeout_body2={
        "minutes": 840571,
    })

    assert res.any is not None

    # Handle response
    print(res.any)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `session_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `increase_timeout_body2`                                                           | [components.IncreaseTimeoutBody2](../../models/components/increasetimeoutbody2.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.IncreaseTimeout2SessionSessionIDIncreaseTimeoutPostResponse](../../models/operations/increasetimeout2sessionsessionidincreasetimeoutpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create Session

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.session.create(request={
        "machine_id": "<id>",
    })

    assert res.create_session_response is not None

    # Handle response
    print(res.create_session_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.CreateSessionBody](../../models/components/createsessionbody.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.CreateSessionSessionPostResponse](../../models/operations/createsessionsessionpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## snapshot_session_session_session_id_snapshot_post

Snapshot Session

### Example Usage

```python
from comfydeploy import ComfyDeploy

with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.session.snapshot_session_session_session_id_snapshot_post(session_id="<id>")

    assert res.any is not None

    # Handle response
    print(res.any)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `session_id`                                                                                       | *str*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `snapshot_session_body`                                                                            | [OptionalNullable[components.SnapshotSessionBody]](../../models/components/snapshotsessionbody.md) | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.SnapshotSessionSessionSessionIDSnapshotPostResponse](../../models/operations/snapshotsessionsessionsessionidsnapshotpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |