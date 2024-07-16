# Run
(*run*)

### Available Operations

* [get](#get) - Get workflow run output
* [create](#create) - Run a workflow via deployment_id

## get

Call this to get a run's output, usually in conjunction with polling method

### Example Usage

```python
import comfydeploy

s = comfydeploy.ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `run_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetRunResponse](../../models/operations/getrunresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GetRunResponseBody    | 400                          | application/json             |
| errors.GetRunRunResponseBody | 500                          | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

## create

Run a workflow via deployment_id

### Example Usage

```python
import comfydeploy
from comfydeploy.models import operations

s = comfydeploy.ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.create(request=operations.PostRunRequestBody(
    deployment_id='d290f1ee-6c54-4b01-90e6-d701748f0851',
    workflow_id='f47ac10b-58cc-4372-a567-0e02b2c3d479',
    inputs={
        'input_text': 'value1',
        'input_url': 'https://example.png',
    },
    webhook='https://example.com/webhook',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PostRunRequestBody](../../models/operations/postrunrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PostRunResponse](../../models/operations/postrunresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.PostRunResponseBody | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |
