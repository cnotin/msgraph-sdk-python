from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.device_configuration import DeviceConfiguration
    from ....models.o_data_errors.o_data_error import ODataError
    from .assign.assign_request_builder import AssignRequestBuilder
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .device_setting_state_summaries.device_setting_state_summaries_request_builder import DeviceSettingStateSummariesRequestBuilder
    from .device_statuses.device_statuses_request_builder import DeviceStatusesRequestBuilder
    from .device_status_overview.device_status_overview_request_builder import DeviceStatusOverviewRequestBuilder
    from .get_oma_setting_plain_text_value_with_secret_reference_value_id.get_oma_setting_plain_text_value_with_secret_reference_value_id_request_builder import GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequestBuilder
    from .user_statuses.user_statuses_request_builder import UserStatusesRequestBuilder
    from .user_status_overview.user_status_overview_request_builder import UserStatusOverviewRequestBuilder

class DeviceConfigurationItemRequestBuilder():
    """
    Provides operations to manage the deviceConfigurations property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceConfigurationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/deviceConfigurations/{deviceConfiguration%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[DeviceConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes a androidWorkProfileGeneralDeviceConfiguration.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DeviceConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[DeviceConfiguration]:
        """
        Read properties and relationships of the sharedPCConfiguration object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceConfiguration]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.device_configuration import DeviceConfiguration

        return await self.request_adapter.send_async(request_info, DeviceConfiguration, error_mapping)
    
    def get_oma_setting_plain_text_value_with_secret_reference_value_id(self,secret_reference_value_id: Optional[str] = None) -> GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequestBuilder:
        """
        Provides operations to call the getOmaSettingPlainTextValue method.
        Args:
            secretReferenceValueId: Usage: secretReferenceValueId='{secretReferenceValueId}'
        Returns: GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequestBuilder
        """
        if not secret_reference_value_id:
            raise TypeError("secret_reference_value_id cannot be null.")
        from .get_oma_setting_plain_text_value_with_secret_reference_value_id.get_oma_setting_plain_text_value_with_secret_reference_value_id_request_builder import GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequestBuilder

        return GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequestBuilder(self.request_adapter, self.path_parameters, secret_reference_value_id)
    
    async def patch(self,body: Optional[DeviceConfiguration] = None, request_configuration: Optional[DeviceConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[DeviceConfiguration]:
        """
        Update the properties of a androidCustomConfiguration object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceConfiguration]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.device_configuration import DeviceConfiguration

        return await self.request_adapter.send_async(request_info, DeviceConfiguration, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes a androidWorkProfileGeneralDeviceConfiguration.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[DeviceConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read properties and relationships of the sharedPCConfiguration object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[DeviceConfiguration] = None, request_configuration: Optional[DeviceConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a androidCustomConfiguration object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def assign(self) -> AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        from .assign.assign_request_builder import AssignRequestBuilder

        return AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceConfiguration entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_setting_state_summaries(self) -> DeviceSettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceSettingStateSummaries property of the microsoft.graph.deviceConfiguration entity.
        """
        from .device_setting_state_summaries.device_setting_state_summaries_request_builder import DeviceSettingStateSummariesRequestBuilder

        return DeviceSettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_statuses(self) -> DeviceStatusesRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.deviceConfiguration entity.
        """
        from .device_statuses.device_statuses_request_builder import DeviceStatusesRequestBuilder

        return DeviceStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_status_overview(self) -> DeviceStatusOverviewRequestBuilder:
        """
        Provides operations to manage the deviceStatusOverview property of the microsoft.graph.deviceConfiguration entity.
        """
        from .device_status_overview.device_status_overview_request_builder import DeviceStatusOverviewRequestBuilder

        return DeviceStatusOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_statuses(self) -> UserStatusesRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.deviceConfiguration entity.
        """
        from .user_statuses.user_statuses_request_builder import UserStatusesRequestBuilder

        return UserStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_status_overview(self) -> UserStatusOverviewRequestBuilder:
        """
        Provides operations to manage the userStatusOverview property of the microsoft.graph.deviceConfiguration entity.
        """
        from .user_status_overview.user_status_overview_request_builder import UserStatusOverviewRequestBuilder

        return UserStatusOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceConfigurationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceConfigurationItemRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the sharedPCConfiguration object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class DeviceConfigurationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceConfigurationItemRequestBuilder.DeviceConfigurationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceConfigurationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

