from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_comment_reply import WorkbookCommentReply

from .entity import Entity

@dataclass
class WorkbookComment(Entity):
    # The content of comment.
    content: Optional[str] = None
    # Indicates the type for the comment.
    content_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The replies property
    replies: Optional[List[WorkbookCommentReply]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookComment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookComment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookComment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_comment_reply import WorkbookCommentReply

        from .entity import Entity
        from .workbook_comment_reply import WorkbookCommentReply

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "content_type": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "replies": lambda n : setattr(self, 'replies', n.get_collection_of_object_values(WorkbookCommentReply)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("content", self.content)
        writer.write_str_value("content_type", self.content_type)
        writer.write_collection_of_object_values("replies", self.replies)
    

