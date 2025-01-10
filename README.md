# comfydeploy

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install comfydeploy
```

Poetry
```bash
poetry add comfydeploy
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id="b18d8d81-fd7b-4764-a31e-475cb1f36591")

if res.workflow_run_model is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from comfydeploy import ComfyDeploy

async def main():
    s = ComfyDeploy(
        bearer="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.run.get_async(run_id="58ccc65b-c928-4154-952e-30c048b8c2b5")
    if res.workflow_run_model is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [run](docs/sdks/run/README.md)

* [get](docs/sdks/run/README.md#get) - Get Run
* [~~queue~~](docs/sdks/run/README.md#queue) - Queue a workflow :warning: **Deprecated**
* [~~sync~~](docs/sdks/run/README.md#sync) - Run a workflow in sync :warning: **Deprecated**
* [~~stream~~](docs/sdks/run/README.md#stream) - Run a workflow in stream :warning: **Deprecated**
* [cancel_run_run_run_id_cancel_post](docs/sdks/run/README.md#cancel_run_run_run_id_cancel_post) - Cancel Run

### [run.deployment](docs/sdks/deployment/README.md)

* [queue](docs/sdks/deployment/README.md#queue) - Deployment - Queue
* [sync](docs/sdks/deployment/README.md#sync) - Deployment - Sync
* [stream](docs/sdks/deployment/README.md#stream) - Deployment - Stream

### [run.workflow](docs/sdks/workflow/README.md)

* [queue](docs/sdks/workflow/README.md#queue) - Workflow - Queue
* [sync](docs/sdks/workflow/README.md#sync) - Workflow - Sync
* [stream](docs/sdks/workflow/README.md#stream) - Workflow - Stream

### [session](docs/sdks/session/README.md)

* [get](docs/sdks/session/README.md#get) - Get Session
* [cancel](docs/sdks/session/README.md#cancel) - Delete Session
* [list](docs/sdks/session/README.md#list) - Get Machine Sessions
* [increase_timeout_session_increase_timeout_post](docs/sdks/session/README.md#increase_timeout_session_increase_timeout_post) - Increase Timeout
* [create](docs/sdks/session/README.md#create) - Create Session

### [deployments](docs/sdks/deployments/README.md)

* [create](docs/sdks/deployments/README.md#create) - Create Deployment
* [list](docs/sdks/deployments/README.md#list) - Get Deployments

### [file](docs/sdks/file/README.md)

* [upload](docs/sdks/file/README.md#upload) - Upload File
* [create_folder_assets_folder_post](docs/sdks/file/README.md#create_folder_assets_folder_post) - Create Folder
* [list_assets_assets_get](docs/sdks/file/README.md#list_assets_assets_get) - List Assets
* [get_asset_assets_asset_id_get](docs/sdks/file/README.md#get_asset_assets_asset_id_get) - Get Asset
* [delete_asset_assets_asset_id_delete](docs/sdks/file/README.md#delete_asset_assets_asset_id_delete) - Delete Asset
* [upload_asset_file_assets_upload_post](docs/sdks/file/README.md#upload_asset_file_assets_upload_post) - Upload Asset File

### [models](docs/sdks/models/README.md)

* [public_models_models_get](docs/sdks/models/README.md#public_models_models_get) - Public Models

### [search](docs/sdks/search/README.md)

* [search_search_model_get](docs/sdks/search/README.md#search_search_model_get) - Search
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

### Example

```python
from comfydeploy import ComfyDeploy
from comfydeploy.models import errors

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.run.get(run_id="b18d8d81-fd7b-4764-a31e-475cb1f36591")

except errors.HTTPValidationError as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.workflow_run_model is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.comfydeploy.com/api` | None |
| 1 | `https://staging.api.comfydeploy.com/api` | None |
| 2 | `http://localhost:3011/api` | None |

#### Example

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    server_idx=2,
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id="b18d8d81-fd7b-4764-a31e-475cb1f36591")

if res.workflow_run_model is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    server_url="https://api.comfydeploy.com/api",
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id="b18d8d81-fd7b-4764-a31e-475cb1f36591")

if res.workflow_run_model is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from comfydeploy import ComfyDeploy
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = ComfyDeploy(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from comfydeploy import ComfyDeploy
from comfydeploy.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = ComfyDeploy(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name        | Type        | Scheme      |
| ----------- | ----------- | ----------- |
| `bearer`    | http        | HTTP Bearer |

To authenticate with the API the `bearer` parameter must be set when initializing the SDK client instance. For example:
```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id="b18d8d81-fd7b-4764-a31e-475cb1f36591")

if res.workflow_run_model is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from comfydeploy import ComfyDeploy
from comfydeploy.utils import BackoffStrategy, RetryConfig

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id="b18d8d81-fd7b-4764-a31e-475cb1f36591",
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res.workflow_run_model is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from comfydeploy import ComfyDeploy
from comfydeploy.utils import BackoffStrategy, RetryConfig

s = ComfyDeploy(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.get(run_id="b18d8d81-fd7b-4764-a31e-475cb1f36591")

if res.workflow_run_model is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Debugging [debug] -->
## Debugging

To emit debug logs for SDK requests and responses you can pass a logger object directly into your SDK object.

```python
from comfydeploy import ComfyDeploy
import logging

logging.basicConfig(level=logging.DEBUG)
s = ComfyDeploy(debug_logger=logging.getLogger("comfydeploy"))
```
<!-- End Debugging [debug] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.

```python
from comfydeploy import ComfyDeploy

s = ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.run.stream(request={
    "model_id": "<value>",
    "inputs": {
        "prompt": "A beautiful landscape",
        "seed": 42,
    },
    "webhook_intermediate_status": True,
})

if res.run_stream is not None:
    for event in res.run_stream:
        # handle event
        print(event, flush=True)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://wiki.python.org/moin/Generators
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

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
<!-- End File uploads [file-upload] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
