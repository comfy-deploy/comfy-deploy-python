# Comfyui
(*comfyui*)

### Available Operations

* [get_auth_response_request_id_](#get_auth_response_request_id_) - Get an API Key with code
* [post_workflow](#post_workflow) - Upload workflow from ComfyUI
* [get_workflow_version_version_id_](#get_workflow_version_version_id_) - Get comfyui workflow
* [get_workflow_id_](#get_workflow_id_) - Get comfyui workflow
* [get_deployment_id_inputs](#get_deployment_id_inputs) - Get comfyui workflow inputs definition
* [get_deployment](#get_deployment) - Get all deployed workflows

## get_auth_response_request_id_

This endpoints is specifically built for ComfyUI workflow upload.

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.comfyui.get_auth_response_request_id_(request_id="<value>")

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetAuthResponseRequestIDResponse](../../models/operations/getauthresponserequestidresponse.md)**
### Errors

| Error Object                                | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.GetAuthResponseRequestIDResponseBody | 500                                         | application/json                            |
| errors.SDKError                             | 4xx-5xx                                     | */*                                         |

## post_workflow

This endpoints is specifically built for ComfyUI workflow upload.

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.comfyui.post_workflow()

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PostWorkflowRequestBody](../../models/operations/postworkflowrequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |


### Response

**[operations.PostWorkflowResponse](../../models/operations/postworkflowresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.PostWorkflowResponseBody | 500                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |

## get_workflow_version_version_id_

Use this to retrieve comfyui workflow by id

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.comfyui.get_workflow_version_version_id_(version_id="<value>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `version_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetWorkflowVersionVersionIDResponse](../../models/operations/getworkflowversionversionidresponse.md)**
### Errors

| Error Object                                   | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| errors.GetWorkflowVersionVersionIDResponseBody | 500                                            | application/json                               |
| errors.SDKError                                | 4xx-5xx                                        | */*                                            |

## get_workflow_id_

Use this to retrieve comfyui workflow by id

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.comfyui.get_workflow_id_(id="<value>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetWorkflowIDResponse](../../models/operations/getworkflowidresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GetWorkflowIDResponseBody | 500                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |

## get_deployment_id_inputs

Use this to retrieve comfyui workflow inputs definition by id

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.comfyui.get_deployment_id_inputs(id="<value>")

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetDeploymentIDInputsResponse](../../models/operations/getdeploymentidinputsresponse.md)**
### Errors

| Error Object                             | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.GetDeploymentIDInputsResponseBody | 500                                      | application/json                         |
| errors.SDKError                          | 4xx-5xx                                  | */*                                      |

## get_deployment

Get all deployed workflows

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.comfyui.get_deployment()

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `environment`                                                              | [Optional[operations.Environment]](../../models/operations/environment.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |


### Response

**[operations.GetDeploymentResponse](../../models/operations/getdeploymentresponse.md)**
### Errors

| Error Object                     | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.GetDeploymentResponseBody | 500                              | application/json                 |
| errors.SDKError                  | 4xx-5xx                          | */*                              |
