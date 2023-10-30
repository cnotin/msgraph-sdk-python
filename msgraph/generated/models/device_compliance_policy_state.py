from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_status import ComplianceStatus
    from .device_compliance_policy_setting_state import DeviceCompliancePolicySettingState
    from .entity import Entity
    from .policy_platform_type import PolicyPlatformType

from .entity import Entity

@dataclass
class DeviceCompliancePolicyState(Entity):
    """
    Device Compliance Policy State for a given device.
    """
    # The name of the policy for this policyBase
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types for policies.
    platform_type: Optional[PolicyPlatformType] = None
    # Count of how many setting a policy holds
    setting_count: Optional[int] = None
    # The settingStates property
    setting_states: Optional[List[DeviceCompliancePolicySettingState]] = None
    # The state property
    state: Optional[ComplianceStatus] = None
    # The version of the policy
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicyState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceCompliancePolicyState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_status import ComplianceStatus
        from .device_compliance_policy_setting_state import DeviceCompliancePolicySettingState
        from .entity import Entity
        from .policy_platform_type import PolicyPlatformType

        from .compliance_status import ComplianceStatus
        from .device_compliance_policy_setting_state import DeviceCompliancePolicySettingState
        from .entity import Entity
        from .policy_platform_type import PolicyPlatformType

        fields: Dict[str, Callable[[Any], None]] = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "platform_type": lambda n : setattr(self, 'platform_type', n.get_enum_value(PolicyPlatformType)),
            "setting_count": lambda n : setattr(self, 'setting_count', n.get_int_value()),
            "setting_states": lambda n : setattr(self, 'setting_states', n.get_collection_of_object_values(DeviceCompliancePolicySettingState)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ComplianceStatus)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_str_value("display_name", self.display_name)
        writer.write_enum_value("platform_type", self.platform_type)
        writer.write_int_value("setting_count", self.setting_count)
        writer.write_collection_of_object_values("setting_states", self.setting_states)
        writer.write_enum_value("state", self.state)
        writer.write_int_value("version", self.version)
    

