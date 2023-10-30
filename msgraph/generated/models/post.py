from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment import Attachment
    from .extension import Extension
    from .item_body import ItemBody
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .outlook_item import OutlookItem
    from .recipient import Recipient
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

from .outlook_item import OutlookItem

@dataclass
class Post(OutlookItem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.post"
    # Read-only. Nullable. Supports $expand.
    attachments: Optional[List[Attachment]] = None
    # The contents of the post. This is a default property. This property can be null.
    body: Optional[ItemBody] = None
    # Unique ID of the conversation. Read-only.
    conversation_id: Optional[str] = None
    # Unique ID of the conversation thread. Read-only.
    conversation_thread_id: Optional[str] = None
    # The collection of open extensions defined for the post. Read-only. Nullable. Supports $expand.
    extensions: Optional[List[Extension]] = None
    # The from property
    from_: Optional[Recipient] = None
    # Indicates whether the post has at least one attachment. This is a default property.
    has_attachments: Optional[bool] = None
    # Read-only. Supports $expand.
    in_reply_to: Optional[Post] = None
    # The collection of multi-value extended properties defined for the post. Read-only. Nullable.
    multi_value_extended_properties: Optional[List[MultiValueLegacyExtendedProperty]] = None
    # Conversation participants that were added to the thread as part of this post.
    new_participants: Optional[List[Recipient]] = None
    # Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    received_date_time: Optional[datetime.datetime] = None
    # Contains the address of the sender. The value of Sender is assumed to be the address of the authenticated user in the case when Sender is not specified. This is a default property.
    sender: Optional[Recipient] = None
    # The collection of single-value extended properties defined for the post. Read-only. Nullable.
    single_value_extended_properties: Optional[List[SingleValueLegacyExtendedProperty]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Post:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Post
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Post()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attachment import Attachment
        from .extension import Extension
        from .item_body import ItemBody
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .recipient import Recipient
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        from .attachment import Attachment
        from .extension import Extension
        from .item_body import ItemBody
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .recipient import Recipient
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        fields: Dict[str, Callable[[Any], None]] = {
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(Attachment)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "conversation_id": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "conversation_thread_id": lambda n : setattr(self, 'conversation_thread_id', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "from": lambda n : setattr(self, 'from_', n.get_object_value(Recipient)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "in_reply_to": lambda n : setattr(self, 'in_reply_to', n.get_object_value(Post)),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "new_participants": lambda n : setattr(self, 'new_participants', n.get_collection_of_object_values(Recipient)),
            "received_date_time": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "sender": lambda n : setattr(self, 'sender', n.get_object_value(Recipient)),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
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
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_object_value("body", self.body)
        writer.write_str_value("conversation_id", self.conversation_id)
        writer.write_str_value("conversation_thread_id", self.conversation_thread_id)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_object_value("from", self.from_)
        writer.write_bool_value("has_attachments", self.has_attachments)
        writer.write_object_value("in_reply_to", self.in_reply_to)
        writer.write_collection_of_object_values("multi_value_extended_properties", self.multi_value_extended_properties)
        writer.write_collection_of_object_values("new_participants", self.new_participants)
        writer.write_datetime_value("received_date_time", self.received_date_time)
        writer.write_object_value("sender", self.sender)
        writer.write_collection_of_object_values("single_value_extended_properties", self.single_value_extended_properties)
    

