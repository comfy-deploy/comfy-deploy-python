# Machines
(*machines*)

### Available Operations

* [post_gpu_event](#post_gpu_event) - Register a machine event
* [get_v1_machines](#get_v1_machines) - Retrieve all machines for a user
* [post_v1_machines](#post_v1_machines) - Create a new machine
* [get_v1_machines_machine_id_](#get_v1_machines_machine_id_) - Retrieve a specific machine by ID

## post_gpu_event

Register a machine event

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.machines.post_gpu_event()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PostGpuEventRequestBody](../../models/operations/postgpueventrequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.PostGpuEventResponse](../../models/operations/postgpueventresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.PostGpuEventResponseBody | 500                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |

## get_v1_machines

Retrieve details of all machines for the authenticated user, with pagination and optional field selection

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.machines.get_v1_machines()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `fields`                                                            | [Optional[operations.Fields]](../../models/operations/fields.md)    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetV1MachinesResponse](../../models/operations/getv1machinesresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GetV1MachinesResponseBody | 400                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |

## post_v1_machines

Create a new machine with optional default setting

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.machines.post_v1_machines()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PostV1MachinesRequestBody](../../models/operations/postv1machinesrequestbody.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |


### Response

**[operations.PostV1MachinesResponse](../../models/operations/postv1machinesresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PostV1MachinesResponseBody | 400                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |

## get_v1_machines_machine_id_

Retrieve details of a specific machine by its ID, with optional workspace details

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.machines.get_v1_machines_machine_id_(machine_id="<value>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `machine_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `ext_urls`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetV1MachinesMachineIDResponse](../../models/operations/getv1machinesmachineidresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.GetV1MachinesMachineIDResponseBody | 400                                       | application/json                          |
| errors.SDKError                           | 4xx-5xx                                   | */*                                       |
