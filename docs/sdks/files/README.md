# Files
(*files*)

### Available Operations

* [get_upload_url](#get_upload_url) - Upload any files to the storage

## get_upload_url

Usually when you run something, you want to upload a file, image etc.

### Example Usage

```python
from comfydeploy import ComfyDeploy
from comfydeploy.models import operations

s = ComfyDeploy(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.files.get_upload_url(type_=operations.Type.APPLICATION_OCTET_STREAM, file_size="<value>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `type`                                                              | [operations.Type](../../models/operations/type.md)                  | :heavy_check_mark:                                                  | N/A                                                                 |
| `file_size`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetUploadURLResponse](../../models/operations/getuploadurlresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.GetUploadURLResponseBody | 500                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |
