from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
    from .microsoft_authenticator_feature_settings import MicrosoftAuthenticatorFeatureSettings

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class MicrosoftAuthenticatorAuthenticationMethodConfiguration(AuthenticationMethodConfiguration):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration"
    # A collection of Microsoft Authenticator settings such as application context and location context, and whether they are enabled for all users or specific users only.
    feature_settings: Optional[MicrosoftAuthenticatorFeatureSettings] = None
    # A collection of groups that are enabled to use the authentication method. Expanded by default.
    include_targets: Optional[List[MicrosoftAuthenticatorAuthenticationMethodTarget]] = None
    # The isSoftwareOathEnabled property
    is_software_oath_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftAuthenticatorAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAuthenticatorAuthenticationMethodConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftAuthenticatorAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .microsoft_authenticator_feature_settings import MicrosoftAuthenticatorFeatureSettings

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .microsoft_authenticator_feature_settings import MicrosoftAuthenticatorFeatureSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "feature_settings": lambda n : setattr(self, 'feature_settings', n.get_object_value(MicrosoftAuthenticatorFeatureSettings)),
            "include_targets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(MicrosoftAuthenticatorAuthenticationMethodTarget)),
            "is_software_oath_enabled": lambda n : setattr(self, 'is_software_oath_enabled', n.get_bool_value()),
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
        writer.write_object_value("feature_settings", self.feature_settings)
        writer.write_collection_of_object_values("include_targets", self.include_targets)
        writer.write_bool_value("is_software_oath_enabled", self.is_software_oath_enabled)
    

