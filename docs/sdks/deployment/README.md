# Deployment
(*deployment*)

### Available Operations

* [get_input_definition](#get_input_definition) - Get comfyui workflow inputs definition
* [get](#get) - Get all deployed workflows

## get_input_definition

Use this to retrieve comfyui workflow inputs definition by id

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.deployment.get_input_definition(id="<value>")

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

## get

Get all deployed workflows

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.deployment.get()

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
