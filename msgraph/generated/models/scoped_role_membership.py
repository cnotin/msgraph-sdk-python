from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity import Identity

from .entity import Entity

@dataclass
class ScopedRoleMembership(Entity):
    # Unique identifier for the administrative unit that the directory role is scoped to
    administrative_unit_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier for the directory role that the member is in.
    role_id: Optional[str] = None
    # The roleMemberInfo property
    role_member_info: Optional[Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScopedRoleMembership:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScopedRoleMembership
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ScopedRoleMembership()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity import Identity

        from .entity import Entity
        from .identity import Identity

        fields: Dict[str, Callable[[Any], None]] = {
            "administrative_unit_id": lambda n : setattr(self, 'administrative_unit_id', n.get_str_value()),
            "role_id": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "role_member_info": lambda n : setattr(self, 'role_member_info', n.get_object_value(Identity)),
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
        writer.write_str_value("administrative_unit_id", self.administrative_unit_id)
        writer.write_str_value("role_id", self.role_id)
        writer.write_object_value("role_member_info", self.role_member_info)
    

