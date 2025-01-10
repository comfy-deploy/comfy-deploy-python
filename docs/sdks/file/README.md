# File
(*file*)

### Available Operations

* [upload](#upload) - Upload File
* [create_folder_assets_folder_post](#create_folder_assets_folder_post) - Create Folder
* [list_assets_assets_get](#list_assets_assets_get) - List Assets
* [get_asset_assets_asset_id_get](#get_asset_assets_asset_id_get) - Get Asset
* [delete_asset_assets_asset_id_delete](#delete_asset_assets_asset_id_delete) - Delete Asset
* [upload_asset_file_assets_upload_post](#upload_asset_file_assets_upload_post) - Upload Asset File

## upload

Upload File

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.file.upload(request={
    "file": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
})

if res.file_upload_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.BodyUploadFileFileUploadPost](../../models/components/bodyuploadfilefileuploadpost.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |


### Response

**[operations.UploadFileFileUploadPostResponse](../../models/operations/uploadfilefileuploadpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## create_folder_assets_folder_post

Create Folder

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.file.create_folder_assets_folder_post(request={
    "name": "<value>",
})

if res.asset_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.CreateFolderRequest](../../models/components/createfolderrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |


### Response

**[operations.CreateFolderAssetsFolderPostResponse](../../models/operations/createfolderassetsfolderpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## list_assets_assets_get

List Assets

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.file.list_assets_assets_get()

if res.response_list_assets_assets_get is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Folder path to list items from                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.ListAssetsAssetsGetResponse](../../models/operations/listassetsassetsgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## get_asset_assets_asset_id_get

Get Asset

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.file.get_asset_assets_asset_id_get(asset_id="<value>")

if res.asset_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.GetAssetAssetsAssetIDGetResponse](../../models/operations/getassetassetsassetidgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## delete_asset_assets_asset_id_delete

Delete Asset

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.file.delete_asset_assets_asset_id_delete(asset_id="<value>")

if res.any is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[operations.DeleteAssetAssetsAssetIDDeleteResponse](../../models/operations/deleteassetassetsassetiddeleteresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## upload_asset_file_assets_upload_post

Upload Asset File

### Example Usage

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.file.upload_asset_file_assets_upload_post(body_upload_asset_file_assets_upload_post={
    "file": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
})

if res.asset_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `body_upload_asset_file_assets_upload_post`                                                                      | [components.BodyUploadAssetFileAssetsUploadPost](../../models/components/bodyuploadassetfileassetsuploadpost.md) | :heavy_check_mark:                                                                                               | N/A                                                                                                              |
| `parent_path`                                                                                                    | *Optional[str]*                                                                                                  | :heavy_minus_sign:                                                                                               | Parent folder path                                                                                               |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |


### Response

**[operations.UploadAssetFileAssetsUploadPostResponse](../../models/operations/uploadassetfileassetsuploadpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |
