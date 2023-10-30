from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class GroupLifecyclePolicy(Entity):
    # List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.
    alternate_notification_emails: Optional[str] = None
    # Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.
    group_lifetime_in_days: Optional[int] = None
    # The group type for which the expiration policy applies. Possible values are All, Selected or None.
    managed_group_types: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupLifecyclePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupLifecyclePolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GroupLifecyclePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "alternate_notification_emails": lambda n : setattr(self, 'alternate_notification_emails', n.get_str_value()),
            "group_lifetime_in_days": lambda n : setattr(self, 'group_lifetime_in_days', n.get_int_value()),
            "managed_group_types": lambda n : setattr(self, 'managed_group_types', n.get_str_value()),
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
        writer.write_str_value("alternate_notification_emails", self.alternate_notification_emails)
        writer.write_int_value("group_lifetime_in_days", self.group_lifetime_in_days)
        writer.write_str_value("managed_group_types", self.managed_group_types)
    

