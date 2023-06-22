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
    from .....models.access_package import AccessPackage
    from .....models.o_data_errors.o_data_error import ODataError
    from .access_packages_incompatible_with.access_packages_incompatible_with_request_builder import AccessPackagesIncompatibleWithRequestBuilder
    from .assignment_policies.assignment_policies_request_builder import AssignmentPoliciesRequestBuilder
    from .catalog.catalog_request_builder import CatalogRequestBuilder
    from .get_applicable_policy_requirements.get_applicable_policy_requirements_request_builder import GetApplicablePolicyRequirementsRequestBuilder
    from .incompatible_access_packages.incompatible_access_packages_request_builder import IncompatibleAccessPackagesRequestBuilder
    from .incompatible_groups.incompatible_groups_request_builder import IncompatibleGroupsRequestBuilder

class AccessPackageItemRequestBuilder():
    """
    Provides operations to manage the accessPackages property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AccessPackageItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete an accessPackage object. You cannot delete an access package if it has any **accessPackageAssignment**.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessPackageItemRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessPackage]:
        """
        Retrieve the properties and relationships of an accessPackage object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackage]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package import AccessPackage

        return await self.request_adapter.send_async(request_info, AccessPackage, error_mapping)
    
    async def patch(self,body: Optional[AccessPackage] = None, request_configuration: Optional[AccessPackageItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[AccessPackage]:
        """
        Update an existing accessPackage object to change one or more of its properties, such as the display name or description.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackage]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package import AccessPackage

        return await self.request_adapter.send_async(request_info, AccessPackage, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessPackageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an accessPackage object. You cannot delete an access package if it has any **accessPackageAssignment**.
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessPackageItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of an accessPackage object.
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
    
    def to_patch_request_information(self,body: Optional[AccessPackage] = None, request_configuration: Optional[AccessPackageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update an existing accessPackage object to change one or more of its properties, such as the display name or description.
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
    def access_packages_incompatible_with(self) -> AccessPackagesIncompatibleWithRequestBuilder:
        """
        Provides operations to manage the accessPackagesIncompatibleWith property of the microsoft.graph.accessPackage entity.
        """
        from .access_packages_incompatible_with.access_packages_incompatible_with_request_builder import AccessPackagesIncompatibleWithRequestBuilder

        return AccessPackagesIncompatibleWithRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_policies(self) -> AssignmentPoliciesRequestBuilder:
        """
        Provides operations to manage the assignmentPolicies property of the microsoft.graph.accessPackage entity.
        """
        from .assignment_policies.assignment_policies_request_builder import AssignmentPoliciesRequestBuilder

        return AssignmentPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def catalog(self) -> CatalogRequestBuilder:
        """
        Provides operations to manage the catalog property of the microsoft.graph.accessPackage entity.
        """
        from .catalog.catalog_request_builder import CatalogRequestBuilder

        return CatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_applicable_policy_requirements(self) -> GetApplicablePolicyRequirementsRequestBuilder:
        """
        Provides operations to call the getApplicablePolicyRequirements method.
        """
        from .get_applicable_policy_requirements.get_applicable_policy_requirements_request_builder import GetApplicablePolicyRequirementsRequestBuilder

        return GetApplicablePolicyRequirementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incompatible_access_packages(self) -> IncompatibleAccessPackagesRequestBuilder:
        """
        Provides operations to manage the incompatibleAccessPackages property of the microsoft.graph.accessPackage entity.
        """
        from .incompatible_access_packages.incompatible_access_packages_request_builder import IncompatibleAccessPackagesRequestBuilder

        return IncompatibleAccessPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incompatible_groups(self) -> IncompatibleGroupsRequestBuilder:
        """
        Provides operations to manage the incompatibleGroups property of the microsoft.graph.accessPackage entity.
        """
        from .incompatible_groups.incompatible_groups_request_builder import IncompatibleGroupsRequestBuilder

        return IncompatibleGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccessPackageItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessPackageItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of an accessPackage object.
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
    class AccessPackageItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessPackageItemRequestBuilder.AccessPackageItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessPackageItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

