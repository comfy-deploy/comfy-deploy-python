# comfydeploy

Developer-friendly & type-safe Python SDK specifically catered to leverage *comfydeploy* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=comfydeploy&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/comfydeploy/comfydeploy). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

ComfyDeploy API: 
### Overview

Welcome to the ComfyDeploy API!

To create a run thru the API, use the [queue run endpoint](#tag/run/POST/run/deployment/queue).

Check out the [get run endpoint](#tag/run/GET/run/{run_id}), for getting the status and output of a run.

### Authentication

To authenticate your requests, include your API key in the `Authorization` header as a bearer token. Make sure to generate an API key in the [API Keys section of your ComfyDeploy account](https://www.comfydeploy.com/api-keys).

###
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [comfydeploy](#comfydeploy)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Server-sent event streaming](#server-sent-event-streaming)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install comfydeploy
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add comfydeploy
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from comfydeploy python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "comfydeploy",
# ]
# ///

from comfydeploy import ComfyDeploy

sdk = ComfyDeploy(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.get(run_id="b888f774-3e7c-4135-a18c-6b985523c4bc")

    assert res.workflow_run_model is not None

    # Handle response
    print(res.workflow_run_model)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from comfydeploy import ComfyDeploy

async def main():

    async with ComfyDeploy(
        bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as comfy_deploy:

        res = await comfy_deploy.run.get_async(run_id="b888f774-3e7c-4135-a18c-6b985523c4bc")

        assert res.workflow_run_model is not None

        # Handle response
        print(res.workflow_run_model)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name     | Type | Scheme      |
| -------- | ---- | ----------- |
| `bearer` | http | HTTP Bearer |

To authenticate with the API the `bearer` parameter must be set when initializing the SDK client instance. For example:
```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.get(run_id="b888f774-3e7c-4135-a18c-6b985523c4bc")

    assert res.workflow_run_model is not None

    # Handle response
    print(res.workflow_run_model)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [deployments](docs/sdks/deployments/README.md)

* [create](docs/sdks/deployments/README.md#create) - Create Deployment
* [update](docs/sdks/deployments/README.md#update) - Update Deployment
* [get](docs/sdks/deployments/README.md#get) - Get Deployment
* [list](docs/sdks/deployments/README.md#list) - Get Deployments
* [get_share_deployment_share_username_slug_get](docs/sdks/deployments/README.md#get_share_deployment_share_username_slug_get) - Get Share Deployment
* [get_featured_deployments_deployments_featured_get](docs/sdks/deployments/README.md#get_featured_deployments_deployments_featured_get) - Get Featured Deployments
* [deactivate](docs/sdks/deployments/README.md#deactivate) - Deactivate Deployment

### [file](docs/sdks/file/README.md)

* [upload](docs/sdks/file/README.md#upload) - Upload File
* [create_folder_assets_folder_post](docs/sdks/file/README.md#create_folder_assets_folder_post) - Create Folder
* [list_assets_assets_get](docs/sdks/file/README.md#list_assets_assets_get) - List Assets
* [delete_asset_assets_asset_id_delete](docs/sdks/file/README.md#delete_asset_assets_asset_id_delete) - Delete Asset
* [get_asset_assets_asset_id_get](docs/sdks/file/README.md#get_asset_assets_asset_id_get) - Get Asset
* [upload_asset_file_assets_upload_post](docs/sdks/file/README.md#upload_asset_file_assets_upload_post) - Upload Asset File

### [models](docs/sdks/models/README.md)

* [public_models_models_get](docs/sdks/models/README.md#public_models_models_get) - Public Models

### [run](docs/sdks/run/README.md)

* [get](docs/sdks/run/README.md#get) - Get Run
* [cancel_run_run_run_id_cancel_post](docs/sdks/run/README.md#cancel_run_run_run_id_cancel_post) - Cancel Run

#### [run.deployment](docs/sdks/deployment/README.md)

* [queue](docs/sdks/deployment/README.md#queue) - Deployment - Queue
* [sync](docs/sdks/deployment/README.md#sync) - Deployment - Sync
* [stream](docs/sdks/deployment/README.md#stream) - Deployment - Stream

#### [run.workflow](docs/sdks/workflow/README.md)

* [queue](docs/sdks/workflow/README.md#queue) - Workflow - Queue
* [sync](docs/sdks/workflow/README.md#sync) - Workflow - Sync
* [stream](docs/sdks/workflow/README.md#stream) - Workflow - Stream

### [search](docs/sdks/search/README.md)

* [search_search_model_get](docs/sdks/search/README.md#search_search_model_get) - Search

### [session](docs/sdks/session/README.md)

* [get](docs/sdks/session/README.md#get) - Get Session
* [cancel](docs/sdks/session/README.md#cancel) - Delete Session
* [list](docs/sdks/session/README.md#list) - Get Machine Sessions
* [increase_timeout_session_increase_timeout_post](docs/sdks/session/README.md#increase_timeout_session_increase_timeout_post) - Increase Timeout
* [increase_timeout_2_session_session_id_increase_timeout_post](docs/sdks/session/README.md#increase_timeout_2_session_session_id_increase_timeout_post) - Increase Timeout 2
* [create](docs/sdks/session/README.md#create) - Create Session
* [snapshot_session_session_session_id_snapshot_post](docs/sdks/session/README.md#snapshot_session_session_session_id_snapshot_post) - Snapshot Session

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.  

The stream is also a [Context Manager][context-manager] and can be used with the `with` statement and will close the
underlying connection when the context is exited.

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.deployment.stream(request={
        "deployment_id": "15e79589-12c9-453c-a41a-348fdd7de957",
        "inputs": {
            "prompt": "A beautiful landscape",
            "seed": 42,
        },
        "webhook": "https://myapp.com/webhook",
    })

    assert res.run_stream is not None

    with res.run_stream as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://book.pythontips.com/en/latest/generators.html
[context-manager]: https://book.pythontips.com/en/latest/context_managers.html
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
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from comfydeploy import ComfyDeploy
from comfydeploy.utils import BackoffStrategy, RetryConfig


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.get(run_id="b888f774-3e7c-4135-a18c-6b985523c4bc",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.workflow_run_model is not None

    # Handle response
    print(res.workflow_run_model)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from comfydeploy import ComfyDeploy
from comfydeploy.utils import BackoffStrategy, RetryConfig


with ComfyDeploy(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.get(run_id="b888f774-3e7c-4135-a18c-6b985523c4bc")

    assert res.workflow_run_model is not None

    # Handle response
    print(res.workflow_run_model)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_async` method may raise the following exceptions:

| Error Type                 | Status Code | Content Type     |
| -------------------------- | ----------- | ---------------- |
| errors.HTTPValidationError | 422         | application/json |
| errors.SDKError            | 4XX, 5XX    | \*/\*            |

### Example

```python
from comfydeploy import ComfyDeploy
from comfydeploy.models import errors


with ComfyDeploy(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:
    res = None
    try:

        res = comfy_deploy.run.get(run_id="b888f774-3e7c-4135-a18c-6b985523c4bc")

        assert res.workflow_run_model is not None

        # Handle response
        print(res.workflow_run_model)

    except errors.HTTPValidationError as e:
        # handle e.data: errors.HTTPValidationErrorData
        raise(e)
    except errors.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                                    | Description              |
| --- | ----------------------------------------- | ------------------------ |
| 0   | `https://api.comfydeploy.com/api`         | Production server        |
| 1   | `https://staging.api.comfydeploy.com/api` | Staging server           |
| 2   | `http://localhost:3011/api`               | Local development server |

#### Example

```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    server_idx=2,
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.get(run_id="b888f774-3e7c-4135-a18c-6b985523c4bc")

    assert res.workflow_run_model is not None

    # Handle response
    print(res.workflow_run_model)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from comfydeploy import ComfyDeploy


with ComfyDeploy(
    server_url="https://api.comfydeploy.com/api",
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as comfy_deploy:

    res = comfy_deploy.run.get(run_id="b888f774-3e7c-4135-a18c-6b985523c4bc")

    assert res.workflow_run_model is not None

    # Handle response
    print(res.workflow_run_model)

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

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `ComfyDeploy` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from comfydeploy import ComfyDeploy
def main():

    with ComfyDeploy(
        bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as comfy_deploy:
        # Rest of application here...


# Or when using async:
async def amain():

    async with ComfyDeploy(
        bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as comfy_deploy:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from comfydeploy import ComfyDeploy
import logging

logging.basicConfig(level=logging.DEBUG)
s = ComfyDeploy(debug_logger=logging.getLogger("comfydeploy"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=comfydeploy&utm_campaign=python)
