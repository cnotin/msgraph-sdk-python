from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_mobile_app import ManagedMobileApp
    from .targeted_managed_app_protection import TargetedManagedAppProtection

from .targeted_managed_app_protection import TargetedManagedAppProtection

@dataclass
class AndroidManagedAppProtection(TargetedManagedAppProtection):
    """
    Policy used to configure detailed management settings targeted to specific security groups and for a specified set of apps on an Android device
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidManagedAppProtection"
    # List of apps to which the policy is deployed.
    apps: Optional[List[ManagedMobileApp]] = None
    # Friendly name of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
    custom_browser_display_name: Optional[str] = None
    # Unique identifier of the preferred custom browser to open weblink on Android. When this property is configured, ManagedBrowserToOpenLinksRequired should be true.
    custom_browser_package_id: Optional[str] = None
    # Count of apps to which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[ManagedAppPolicyDeploymentSummary] = None
    # When this setting is enabled, app level encryption is disabled if device level encryption is enabled
    disable_app_encryption_if_device_encryption_is_enabled: Optional[bool] = None
    # Indicates whether application data for managed apps should be encrypted
    encrypt_app_data: Optional[bool] = None
    # Define the oldest required Android security patch level a user can have to gain secure access to the app.
    minimum_required_patch_version: Optional[str] = None
    # Define the oldest recommended Android security patch level a user can have for secure access to the app.
    minimum_warning_patch_version: Optional[str] = None
    # Indicates whether a managed user can take screen captures of managed apps
    screen_capture_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedAppProtection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidManagedAppProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_protection import TargetedManagedAppProtection

        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_protection import TargetedManagedAppProtection

        fields: Dict[str, Callable[[Any], None]] = {
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ManagedMobileApp)),
            "custom_browser_display_name": lambda n : setattr(self, 'custom_browser_display_name', n.get_str_value()),
            "custom_browser_package_id": lambda n : setattr(self, 'custom_browser_package_id', n.get_str_value()),
            "deployed_app_count": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deployment_summary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(ManagedAppPolicyDeploymentSummary)),
            "disable_app_encryption_if_device_encryption_is_enabled": lambda n : setattr(self, 'disable_app_encryption_if_device_encryption_is_enabled', n.get_bool_value()),
            "encrypt_app_data": lambda n : setattr(self, 'encrypt_app_data', n.get_bool_value()),
            "minimum_required_patch_version": lambda n : setattr(self, 'minimum_required_patch_version', n.get_str_value()),
            "minimum_warning_patch_version": lambda n : setattr(self, 'minimum_warning_patch_version', n.get_str_value()),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
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
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_str_value("custom_browser_display_name", self.custom_browser_display_name)
        writer.write_str_value("custom_browser_package_id", self.custom_browser_package_id)
        writer.write_int_value("deployed_app_count", self.deployed_app_count)
        writer.write_object_value("deployment_summary", self.deployment_summary)
        writer.write_bool_value("disable_app_encryption_if_device_encryption_is_enabled", self.disable_app_encryption_if_device_encryption_is_enabled)
        writer.write_bool_value("encrypt_app_data", self.encrypt_app_data)
        writer.write_str_value("minimum_required_patch_version", self.minimum_required_patch_version)
        writer.write_str_value("minimum_warning_patch_version", self.minimum_warning_patch_version)
        writer.write_bool_value("screen_capture_blocked", self.screen_capture_blocked)
    

