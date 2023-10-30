from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

@dataclass
class UnifiedRoleManagementPolicyAuthenticationContextRule(UnifiedRoleManagementPolicyRule):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule"
    # The value of the authentication context claim.
    claim_value: Optional[str] = None
    # Determines whether this rule is enabled.
    is_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyAuthenticationContextRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyAuthenticationContextRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementPolicyAuthenticationContextRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        fields: Dict[str, Callable[[Any], None]] = {
            "claim_value": lambda n : setattr(self, 'claim_value', n.get_str_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
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
        writer.write_str_value("claim_value", self.claim_value)
        writer.write_bool_value("is_enabled", self.is_enabled)
    

