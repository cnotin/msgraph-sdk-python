from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError

class GetOneDriveUsageStorageWithPeriodRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getOneDriveUsageStorage method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, period: Optional[str] = None) -> None:
        """
        Instantiates a new GetOneDriveUsageStorageWithPeriodRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param period: Usage: period='{period}'
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['period'] = str(period)
        super().__init__(request_adapter, "{+baseurl}/reports/getOneDriveUsageStorage(period='{period}')", path_parameters)
    
    async def get(self,request_configuration: Optional[GetOneDriveUsageStorageWithPeriodRequestBuilderGetRequestConfiguration] = None) -> bytes:
        """
        Invoke function getOneDriveUsageStorage
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[GetOneDriveUsageStorageWithPeriodRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function getOneDriveUsageStorage
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.try_add_request_header("Accept", "application/octet-stream, application/json, application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> GetOneDriveUsageStorageWithPeriodRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetOneDriveUsageStorageWithPeriodRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GetOneDriveUsageStorageWithPeriodRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class GetOneDriveUsageStorageWithPeriodRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

