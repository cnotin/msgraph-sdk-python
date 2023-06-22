from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .managed_android_lob_app import ManagedAndroidLobApp
    from .managed_app import ManagedApp
    from .managed_i_o_s_lob_app import ManagedIOSLobApp
    from .mobile_app_content import MobileAppContent

from .managed_app import ManagedApp

@dataclass
class ManagedMobileLobApp(ManagedApp):
    odata_type = "#microsoft.graph.managedMobileLobApp"
    # The internal committed content version.
    committed_content_version: Optional[str] = None
    # The list of content versions for this app.
    content_versions: Optional[List[MobileAppContent]] = None
    # The name of the main Lob application file.
    file_name: Optional[str] = None
    # The total size, including all uploaded files.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedMobileLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedMobileLobApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidLobApp".casefold():
            from .managed_android_lob_app import ManagedAndroidLobApp

            return ManagedAndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSLobApp".casefold():
            from .managed_i_o_s_lob_app import ManagedIOSLobApp

            return ManagedIOSLobApp()
        return ManagedMobileLobApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_app import ManagedApp
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .mobile_app_content import MobileAppContent

        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_app import ManagedApp
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .mobile_app_content import MobileAppContent

        fields: Dict[str, Callable[[Any], None]] = {
            "committedContentVersion": lambda n : setattr(self, 'committed_content_version', n.get_str_value()),
            "contentVersions": lambda n : setattr(self, 'content_versions', n.get_collection_of_object_values(MobileAppContent)),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("committedContentVersion", self.committed_content_version)
        writer.write_collection_of_object_values("contentVersions", self.content_versions)
        writer.write_str_value("fileName", self.file_name)
        writer.write_int_value("size", self.size)
    

