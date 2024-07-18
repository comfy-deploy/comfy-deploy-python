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
import os

s = ComfyDeploy(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.run.get(run_id="<value>")

if res.object is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from comfydeploy import ComfyDeploy
import os

async def main():
    s = ComfyDeploy(
        bearer_auth=os.getenv("BEARER_AUTH", ""),
    )
    res = await s.run.get_async(run_id="<value>")
    if res.object is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [run](docs/sdks/run/README.md)

* [get](docs/sdks/run/README.md#get) - Get workflow run output
* [create](docs/sdks/run/README.md#create) - Run a workflow via deployment_id

### [files](docs/sdks/files/README.md)

* [get_upload_url](docs/sdks/files/README.md#get_upload_url) - Upload any files to the storage

### [workflows](docs/sdks/workflows/README.md)

* [get_websocket_deployment_id_](docs/sdks/workflows/README.md#get_websocket_deployment_id_) - Get a websocket url for a specific deployment
* [post_machine_endpoint](docs/sdks/workflows/README.md#post_machine_endpoint) - Create an endpoint for a machine
* [get_v1_workflows](docs/sdks/workflows/README.md#get_v1_workflows) - Retrieve workflows
* [post_v1_workflows](docs/sdks/workflows/README.md#post_v1_workflows) - Create a new workflow
* [get_v1_workflows_workflow_id_](docs/sdks/workflows/README.md#get_v1_workflows_workflow_id_) - Retrieve a specific workflow by ID
* [get_v1_workflows_workflow_id_outputs](docs/sdks/workflows/README.md#get_v1_workflows_workflow_id_outputs) - Retrieve the most recent outputs for a workflow

### [comfyui](docs/sdks/comfyui/README.md)

* [get_auth_response_request_id_](docs/sdks/comfyui/README.md#get_auth_response_request_id_) - Get an API Key with code
* [post_workflow](docs/sdks/comfyui/README.md#post_workflow) - Upload workflow from ComfyUI
* [get_workflow_version_version_id_](docs/sdks/comfyui/README.md#get_workflow_version_version_id_) - Get comfyui workflow
* [get_workflow_id_](docs/sdks/comfyui/README.md#get_workflow_id_) - Get comfyui workflow
* [get_deployment_id_inputs](docs/sdks/comfyui/README.md#get_deployment_id_inputs) - Get comfyui workflow inputs definition
* [get_deployment](docs/sdks/comfyui/README.md#get_deployment) - Get all deployed workflows

### [machines](docs/sdks/machines/README.md)

* [post_gpu_event](docs/sdks/machines/README.md#post_gpu_event) - Register a machine event
* [get_v1_machines](docs/sdks/machines/README.md#get_v1_machines) - Retrieve all machines for a user
* [post_v1_machines](docs/sdks/machines/README.md#post_v1_machines) - Create a new machine
* [get_v1_machines_machine_id_](docs/sdks/machines/README.md#get_v1_machines_machine_id_) - Retrieve a specific machine by ID
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.GetRunResponseBody    | 400                          | application/json             |
| errors.GetRunRunResponseBody | 500                          | application/json             |
| errors.SDKError              | 4xx-5xx                      | */*                          |

### Example

```python
from comfydeploy import ComfyDeploy
from comfydeploy.models import errors
import os

s = ComfyDeploy(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)

res = None
try:
    res = s.run.get(run_id="<value>")

except errors.GetRunResponseBody as e:
    # handle exception
    raise(e)
except errors.GetRunRunResponseBody as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.object is not None:
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
| 0 | `https:///api` | None |

#### Example

```python
from comfydeploy import ComfyDeploy
import os

s = ComfyDeploy(
    server_idx=0,
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.run.get(run_id="<value>")

if res.object is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from comfydeploy import ComfyDeploy
import os

s = ComfyDeploy(
    server_url="https:///api",
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.run.get(run_id="<value>")

if res.object is not None:
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

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from comfydeploy import ComfyDeploy
import os

s = ComfyDeploy(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.run.get(run_id="<value>")

if res.object is not None:
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
import os

s = ComfyDeploy(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.run.get(run_id="<value>",
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res.object is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from comfydeploy import ComfyDeploy
from comfydeploy.utils import BackoffStrategy, RetryConfig
import os

s = ComfyDeploy(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.run.get(run_id="<value>")

if res.object is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

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
