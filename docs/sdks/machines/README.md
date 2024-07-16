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
import comfydeploy
from comfydeploy.models import operations

s = comfydeploy.ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.machines.post_gpu_event(request=operations.PostGpuEventRequestBody(
    machine_id='<value>',
    timestamp='<value>',
    event_type=operations.EventType.GPU_END,
    gpu_provider=operations.GpuProvider.MODAL,
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PostGpuEventRequestBody](../../models/operations/postgpueventrequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


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
import comfydeploy
from comfydeploy.models import operations

s = comfydeploy.ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.machines.get_v1_machines(page='1', page_size='12', fields=operations.Fields.MINIMAL)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `page`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `page_size`                                                      | *Optional[str]*                                                  | :heavy_minus_sign:                                               | N/A                                                              |
| `fields`                                                         | [Optional[operations.Fields]](../../models/operations/fields.md) | :heavy_minus_sign:                                               | N/A                                                              |


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
import comfydeploy
from comfydeploy.models import operations

s = comfydeploy.ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.machines.post_v1_machines(request=operations.PostV1MachinesRequestBody())

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PostV1MachinesRequestBody](../../models/operations/postv1machinesrequestbody.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


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
import comfydeploy

s = comfydeploy.ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.machines.get_v1_machines_machine_id_(machine_id='<value>', ext_urls='false')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `machine_id`       | *str*              | :heavy_check_mark: | N/A                |
| `ext_urls`         | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetV1MachinesMachineIDResponse](../../models/operations/getv1machinesmachineidresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.GetV1MachinesMachineIDResponseBody | 400                                       | application/json                          |
| errors.SDKError                           | 4xx-5xx                                   | */*                                       |
