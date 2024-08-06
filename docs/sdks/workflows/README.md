# Workflows
(*workflows*)

### Available Operations

* [get_websocket_deployment_id_](#get_websocket_deployment_id_) - Get a websocket url for a specific deployment
* [post_machine_endpoint](#post_machine_endpoint) - Create an endpoint for a machine
* [get_v1_workflows](#get_v1_workflows) - Retrieve workflows
* [post_v1_workflows](#post_v1_workflows) - Create a new workflow
* [get_v1_workflows_workflow_id_](#get_v1_workflows_workflow_id_) - Retrieve a specific workflow by ID
* [get_v1_workflows_workflow_id_outputs](#get_v1_workflows_workflow_id_outputs) - Retrieve the most recent outputs for a workflow

## get_websocket_deployment_id_

Get a websocket url for a specific deployment

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_websocket_deployment_id_(deployment_id="<value>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `deployment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetWebsocketDeploymentIDResponse](../../models/operations/getwebsocketdeploymentidresponse.md)**
### Errors

| Error Object                                | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.GetWebsocketDeploymentIDResponseBody | 500                                         | application/json                            |
| errors.SDKError                             | 4xx-5xx                                     | */*                                         |

## post_machine_endpoint

Create an endpoint for a machine

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.post_machine_endpoint()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostMachineEndpointRequestBody](../../models/operations/postmachineendpointrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |


### Response

**[operations.PostMachineEndpointResponse](../../models/operations/postmachineendpointresponse.md)**
### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.PostMachineEndpointResponseBody | 500                                    | application/json                       |
| errors.SDKError                        | 4xx-5xx                                | */*                                    |

## get_v1_workflows

Retrieve workflows based on optional query parameters

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_v1_workflows()

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetV1WorkflowsResponse](../../models/operations/getv1workflowsresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.GetV1WorkflowsResponseBody | 400                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |

## post_v1_workflows

Create a new workflow by analyzing the provided workflow JSON

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.post_v1_workflows()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostV1WorkflowsRequestBody](../../models/operations/postv1workflowsrequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.PostV1WorkflowsResponse](../../models/operations/postv1workflowsresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.PostV1WorkflowsResponseBody | 400                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |

## get_v1_workflows_workflow_id_

Retrieve the latest version of a specific workflow by its ID

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_v1_workflows_workflow_id_(workflow_id="<value>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetV1WorkflowsWorkflowIDResponse](../../models/operations/getv1workflowsworkflowidresponse.md)**
### Errors

| Error Object                                | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.GetV1WorkflowsWorkflowIDResponseBody | 400                                         | application/json                            |
| errors.SDKError                             | 4xx-5xx                                     | */*                                         |

## get_v1_workflows_workflow_id_outputs

Retrieve the latest version of a specific workflow by its ID

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.workflows.get_v1_workflows_workflow_id_outputs(request={
    "workflow_id": "<value>",
})

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetV1WorkflowsWorkflowIDOutputsRequest](../../models/operations/getv1workflowsworkflowidoutputsrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |


### Response

**[operations.GetV1WorkflowsWorkflowIDOutputsResponse](../../models/operations/getv1workflowsworkflowidoutputsresponse.md)**
### Errors

| Error Object                                       | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.GetV1WorkflowsWorkflowIDOutputsResponseBody | 400                                                | application/json                                   |
| errors.SDKError                                    | 4xx-5xx                                            | */*                                                |
