from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.screen_sharing_role import ScreenSharingRole

@dataclass
class ChangeScreenSharingRolePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The role property
    role: Optional[ScreenSharingRole] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChangeScreenSharingRolePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChangeScreenSharingRolePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ChangeScreenSharingRolePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.screen_sharing_role import ScreenSharingRole

        from .....models.screen_sharing_role import ScreenSharingRole

        fields: Dict[str, Callable[[Any], None]] = {
            "role": lambda n : setattr(self, 'role', n.get_enum_value(ScreenSharingRole)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

