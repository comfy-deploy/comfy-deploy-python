# Models
(*models*)

## Overview

### Available Operations

* [public_models_models_get](#public_models_models_get) - Public Models

## public_models_models_get

Return a list of available public models with their input/output specifications

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.models.public_models_models_get()

    assert res.response_public_models_models_get is not None

    # Handle response
    print(res.response_public_models_models_get)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.PublicModelsModelsGetResponse](../../models/operations/publicmodelsmodelsgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |