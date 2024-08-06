"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, NoOpLogger
from .utils.retries import RetryConfig
from comfydeploy._hooks import SDKHooks
from comfydeploy.comfyui import Comfyui
from comfydeploy.files import Files
from comfydeploy.machines import Machines
from comfydeploy.models import components
from comfydeploy.run import Run
from comfydeploy.types import OptionalNullable, UNSET
import comfydeploy.utils as utils
from comfydeploy.workflows import Workflows
import httpx
from typing import Any, Callable, Dict, Optional, Union

class ComfyDeploy(BaseSDK):
    r"""Comfy Deploy API: Interact with Comfy Deploy programmatically to trigger run and retrieve output"""
    run: Run
    files: Files
    workflows: Workflows
    comfyui: Comfyui
    machines: Machines
    def __init__(
        self,
        bearer_auth: Union[str, Callable[[], str]],
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param bearer_auth: The bearer_auth required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = NoOpLogger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."
        
        security: Any = None
        if callable(bearer_auth):
            security = lambda: components.Security(bearer_auth = bearer_auth()) # pylint: disable=unnecessary-lambda-assignment
        else:
            security = components.Security(bearer_auth = bearer_auth)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    

        BaseSDK.__init__(self, SDKConfiguration(
            client=client,
            async_client=async_client,
            security=security,
            server_url=server_url,
            server_idx=server_idx,
            retry_config=retry_config,
            timeout_ms=timeout_ms,
            debug_logger=debug_logger
        ))

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.run = Run(self.sdk_configuration)
        self.files = Files(self.sdk_configuration)
        self.workflows = Workflows(self.sdk_configuration)
        self.comfyui = Comfyui(self.sdk_configuration)
        self.machines = Machines(self.sdk_configuration)
    
