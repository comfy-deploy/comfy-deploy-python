# Session
(*session*)

### Available Operations

* [get](#get) - Get Session
* [cancel](#cancel) - Delete Session
* [list](#list) - Get Machine Sessions
* [increase_timeout_session_increase_timeout_post](#increase_timeout_session_increase_timeout_post) - Increase Timeout
* [create](#create) - Create Session

## get

Get Session

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.session.get(session_id="<value>")

if res.session is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetSessionSessionSessionIDGetResponse](../../models/operations/getsessionsessionsessionidgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## cancel

Delete Session

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.session.cancel(session_id="<value>")

if res.delete_session_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.DeleteSessionSessionSessionIDDeleteResponse](../../models/operations/deletesessionsessionsessioniddeleteresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## list

Get Machine Sessions

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.session.list(machine_id="<value>")

if res.response_get_machine_sessions_sessions_get is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `machine_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetMachineSessionsSessionsGetResponse](../../models/operations/getmachinesessionssessionsgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## increase_timeout_session_increase_timeout_post

Increase Timeout

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.session.increase_timeout_session_increase_timeout_post(request={
    "machine_id": "<value>",
    "session_id": "d712cbb0-db3d-45d5-a8f9-ef1b452fb427",
    "timeout": 36199,
    "gpu": "<value>",
})

if res.any is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.IncreaseTimeoutBody](../../models/components/increasetimeoutbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |


### Response

**[operations.IncreaseTimeoutSessionIncreaseTimeoutPostResponse](../../models/operations/increasetimeoutsessionincreasetimeoutpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## create

Create Session

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.session.create(request={
    "machine_id": "<value>",
})

if res.create_session_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.CreateSessionBody](../../models/components/createsessionbody.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |


### Response

**[operations.CreateSessionSessionPostResponse](../../models/operations/createsessionsessionpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |
