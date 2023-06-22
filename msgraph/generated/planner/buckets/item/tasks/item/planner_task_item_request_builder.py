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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.planner_task import PlannerTask
    from .assigned_to_task_board_format.assigned_to_task_board_format_request_builder import AssignedToTaskBoardFormatRequestBuilder
    from .bucket_task_board_format.bucket_task_board_format_request_builder import BucketTaskBoardFormatRequestBuilder
    from .details.details_request_builder import DetailsRequestBuilder
    from .progress_task_board_format.progress_task_board_format_request_builder import ProgressTaskBoardFormatRequestBuilder

class PlannerTaskItemRequestBuilder():
    """
    Provides operations to manage the tasks property of the microsoft.graph.plannerBucket entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PlannerTaskItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/planner/buckets/{plannerBucket%2Did}/tasks/{plannerTask%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[PlannerTaskItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property tasks for planner
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[PlannerTaskItemRequestBuilderGetRequestConfiguration] = None) -> Optional[PlannerTask]:
        """
        Read-only. Nullable. The collection of tasks in the bucket.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlannerTask]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.planner_task import PlannerTask

        return await self.request_adapter.send_async(request_info, PlannerTask, error_mapping)
    
    async def patch(self,body: Optional[PlannerTask] = None, request_configuration: Optional[PlannerTaskItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[PlannerTask]:
        """
        Update the navigation property tasks in planner
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlannerTask]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.planner_task import PlannerTask

        return await self.request_adapter.send_async(request_info, PlannerTask, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PlannerTaskItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property tasks for planner
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
    
    def to_get_request_information(self,request_configuration: Optional[PlannerTaskItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read-only. Nullable. The collection of tasks in the bucket.
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
    
    def to_patch_request_information(self,body: Optional[PlannerTask] = None, request_configuration: Optional[PlannerTaskItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property tasks in planner
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
    def assigned_to_task_board_format(self) -> AssignedToTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the assignedToTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        from .assigned_to_task_board_format.assigned_to_task_board_format_request_builder import AssignedToTaskBoardFormatRequestBuilder

        return AssignedToTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bucket_task_board_format(self) -> BucketTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the bucketTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        from .bucket_task_board_format.bucket_task_board_format_request_builder import BucketTaskBoardFormatRequestBuilder

        return BucketTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def details(self) -> DetailsRequestBuilder:
        """
        Provides operations to manage the details property of the microsoft.graph.plannerTask entity.
        """
        from .details.details_request_builder import DetailsRequestBuilder

        return DetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def progress_task_board_format(self) -> ProgressTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the progressTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        from .progress_task_board_format.progress_task_board_format_request_builder import ProgressTaskBoardFormatRequestBuilder

        return ProgressTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlannerTaskItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PlannerTaskItemRequestBuilderGetQueryParameters():
        """
        Read-only. Nullable. The collection of tasks in the bucket.
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
    class PlannerTaskItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PlannerTaskItemRequestBuilder.PlannerTaskItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PlannerTaskItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

