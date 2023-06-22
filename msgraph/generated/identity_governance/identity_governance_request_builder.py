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
    from ..models.identity_governance import IdentityGovernance
    from ..models.o_data_errors.o_data_error import ODataError
    from .access_reviews.access_reviews_request_builder import AccessReviewsRequestBuilder
    from .app_consent.app_consent_request_builder import AppConsentRequestBuilder
    from .entitlement_management.entitlement_management_request_builder import EntitlementManagementRequestBuilder
    from .terms_of_use.terms_of_use_request_builder import TermsOfUseRequestBuilder

class IdentityGovernanceRequestBuilder():
    """
    Provides operations to manage the identityGovernance singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new IdentityGovernanceRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[IdentityGovernanceRequestBuilderGetRequestConfiguration] = None) -> Optional[IdentityGovernance]:
        """
        Get identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IdentityGovernance]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.identity_governance import IdentityGovernance

        return await self.request_adapter.send_async(request_info, IdentityGovernance, error_mapping)
    
    async def patch(self,body: Optional[IdentityGovernance] = None, request_configuration: Optional[IdentityGovernanceRequestBuilderPatchRequestConfiguration] = None) -> Optional[IdentityGovernance]:
        """
        Update identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IdentityGovernance]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.identity_governance import IdentityGovernance

        return await self.request_adapter.send_async(request_info, IdentityGovernance, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[IdentityGovernanceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get identityGovernance
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
    
    def to_patch_request_information(self,body: Optional[IdentityGovernance] = None, request_configuration: Optional[IdentityGovernanceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update identityGovernance
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
    def access_reviews(self) -> AccessReviewsRequestBuilder:
        """
        Provides operations to manage the accessReviews property of the microsoft.graph.identityGovernance entity.
        """
        from .access_reviews.access_reviews_request_builder import AccessReviewsRequestBuilder

        return AccessReviewsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_consent(self) -> AppConsentRequestBuilder:
        """
        Provides operations to manage the appConsent property of the microsoft.graph.identityGovernance entity.
        """
        from .app_consent.app_consent_request_builder import AppConsentRequestBuilder

        return AppConsentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def entitlement_management(self) -> EntitlementManagementRequestBuilder:
        """
        Provides operations to manage the entitlementManagement property of the microsoft.graph.identityGovernance entity.
        """
        from .entitlement_management.entitlement_management_request_builder import EntitlementManagementRequestBuilder

        return EntitlementManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terms_of_use(self) -> TermsOfUseRequestBuilder:
        """
        Provides operations to manage the termsOfUse property of the microsoft.graph.identityGovernance entity.
        """
        from .terms_of_use.terms_of_use_request_builder import TermsOfUseRequestBuilder

        return TermsOfUseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IdentityGovernanceRequestBuilderGetQueryParameters():
        """
        Get identityGovernance
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
    class IdentityGovernanceRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[IdentityGovernanceRequestBuilder.IdentityGovernanceRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class IdentityGovernanceRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

