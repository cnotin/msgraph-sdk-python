from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_target import AuthenticationMethodTarget

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class VoiceAuthenticationMethodConfiguration(AuthenticationMethodConfiguration):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.voiceAuthenticationMethodConfiguration"
    # A collection of groups that are enabled to use the authentication method. Expanded by default.
    include_targets: Optional[List[AuthenticationMethodTarget]] = None
    # true if users can register office phones, otherwise, false.
    is_office_phone_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VoiceAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VoiceAuthenticationMethodConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VoiceAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "include_targets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(AuthenticationMethodTarget)),
            "is_office_phone_allowed": lambda n : setattr(self, 'is_office_phone_allowed', n.get_bool_value()),
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
        writer.write_collection_of_object_values("include_targets", self.include_targets)
        writer.write_bool_value("is_office_phone_allowed", self.is_office_phone_allowed)
    

