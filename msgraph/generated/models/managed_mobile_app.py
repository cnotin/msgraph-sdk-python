from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app_identifier import MobileAppIdentifier

from .entity import Entity

@dataclass
class ManagedMobileApp(Entity):
    """
    The identifier for the deployment an app.
    """
    # The identifier for an app with it's operating system type.
    mobile_app_identifier: Optional[MobileAppIdentifier] = None
    # The OdataType property
    OdataType: Optional[str] = None
    # Version of the entity.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedMobileApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedMobileApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagedMobileApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app_identifier import MobileAppIdentifier

        from .entity import Entity
        from .mobile_app_identifier import MobileAppIdentifier

        fields: Dict[str, Callable[[Any], None]] = {
            "mobileAppIdentifier": lambda n : setattr(self, 'mobile_app_identifier', n.get_object_value(MobileAppIdentifier)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("mobileAppIdentifier", self.mobile_app_identifier)
        writer.write_str_value("version", self.version)
    

