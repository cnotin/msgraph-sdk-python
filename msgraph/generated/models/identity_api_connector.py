from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase
    from .entity import Entity

from .entity import Entity

@dataclass
class IdentityApiConnector(Entity):
    # The object which describes the authentication configuration details for calling the API. Basic and PKCS 12 client certificate are supported.
    authentication_configuration: Optional[ApiAuthenticationConfigurationBase] = None
    # The name of the API connector.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL of the API endpoint to call.
    target_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityApiConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityApiConnector
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IdentityApiConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase
        from .entity import Entity

        from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "authentication_configuration": lambda n : setattr(self, 'authentication_configuration', n.get_object_value(ApiAuthenticationConfigurationBase)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "target_url": lambda n : setattr(self, 'target_url', n.get_str_value()),
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
        writer.write_object_value("authentication_configuration", self.authentication_configuration)
        writer.write_str_value("display_name", self.display_name)
        writer.write_str_value("target_url", self.target_url)
    

