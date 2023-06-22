from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .outlook_category import OutlookCategory

from .entity import Entity

@dataclass
class OutlookUser(Entity):
    # A list of categories defined for the user.
    master_categories: Optional[List[OutlookCategory]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutlookUser
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OutlookUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .outlook_category import OutlookCategory

        from .entity import Entity
        from .outlook_category import OutlookCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "masterCategories": lambda n : setattr(self, 'master_categories', n.get_collection_of_object_values(OutlookCategory)),
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
        writer.write_collection_of_object_values("masterCategories", self.master_categories)
    

