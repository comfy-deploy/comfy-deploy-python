# File
(*file*)

## Overview

### Available Operations

* [upload](#upload) - Upload File
* [create_folder_assets_folder_post](#create_folder_assets_folder_post) - Create Folder
* [list_assets_assets_get](#list_assets_assets_get) - List Assets
* [delete_asset_assets_asset_id_delete](#delete_asset_assets_asset_id_delete) - Delete Asset
* [get_asset_assets_asset_id_get](#get_asset_assets_asset_id_get) - Get Asset
* [upload_asset_file_assets_upload_post](#upload_asset_file_assets_upload_post) - Upload Asset File

## upload

Upload File

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.file.upload(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    assert res.file_upload_response is not None

    # Handle response
    print(res.file_upload_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.BodyUploadFileFileUploadPost](../../models/components/bodyuploadfilefileuploadpost.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UploadFileFileUploadPostResponse](../../models/operations/uploadfilefileuploadpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_folder_assets_folder_post

Create Folder

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.file.create_folder_assets_folder_post(request={
        "name": "<value>",
    })

    assert res.asset_response is not None

    # Handle response
    print(res.asset_response)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.CreateFolderRequest](../../models/components/createfolderrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.CreateFolderAssetsFolderPostResponse](../../models/operations/createfolderassetsfolderpostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_assets_assets_get

List Assets

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.file.list_assets_assets_get()

    assert res.response_list_assets_assets_get is not None

    # Handle response
    print(res.response_list_assets_assets_get)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Folder path to list items from                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.ListAssetsAssetsGetResponse](../../models/operations/listassetsassetsgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_asset_assets_asset_id_delete

Delete Asset

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.file.delete_asset_assets_asset_id_delete(asset_id="<id>")

    assert res.any is not None

    # Handle response
    print(res.any)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteAssetAssetsAssetIDDeleteResponse](../../models/operations/deleteassetassetsassetiddeleteresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_asset_assets_asset_id_get

Get Asset

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.file.get_asset_assets_asset_id_get(asset_id="<id>")

    assert res.asset_response is not None

    # Handle response
    print(res.asset_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `asset_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetAssetAssetsAssetIDGetResponse](../../models/operations/getassetassetsassetidgetresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## upload_asset_file_assets_upload_post

Upload Asset File

### Example Usage

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.file.upload_asset_file_assets_upload_post(body_upload_asset_file_assets_upload_post={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    assert res.asset_response is not None

    # Handle response
    print(res.asset_response)

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

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |