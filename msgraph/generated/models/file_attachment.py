from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment import Attachment

from .attachment import Attachment

@dataclass
class FileAttachment(Attachment):
    odata_type = "#microsoft.graph.fileAttachment"
    # The base64-encoded contents of the file.
    content_bytes: Optional[bytes] = None
    # The ID of the attachment in the Exchange store.
    content_id: Optional[str] = None
    # Do not use this property as it is not supported.
    content_location: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileAttachment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FileAttachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attachment import Attachment

        from .attachment import Attachment

        fields: Dict[str, Callable[[Any], None]] = {
            "contentBytes": lambda n : setattr(self, 'content_bytes', n.get_bytes_value()),
            "contentId": lambda n : setattr(self, 'content_id', n.get_str_value()),
            "contentLocation": lambda n : setattr(self, 'content_location', n.get_str_value()),
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
        writer.write_bytes_value("contentBytes", self.content_bytes)
        writer.write_str_value("contentId", self.content_id)
        writer.write_str_value("contentLocation", self.content_location)
    

