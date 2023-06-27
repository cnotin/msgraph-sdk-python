from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_external_user_lifecycle_action import AccessPackageExternalUserLifecycleAction
    from .entity import Entity

from .entity import Entity

@dataclass
class EntitlementManagementSettings(Entity):
    # If externalUserLifecycleAction is blockSignInAndDelete, the duration, typically a number of days, after an external user is blocked from sign in before their account is deleted.
    duration_until_external_user_deleted_after_blocked: Optional[datetime.timedelta] = None
    # Automatic action that the service should take when an external user's last access package assignment is removed. The possible values are: none, blockSignIn, blockSignInAndDelete, unknownFutureValue.
    external_user_lifecycle_action: Optional[AccessPackageExternalUserLifecycleAction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EntitlementManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagementSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EntitlementManagementSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_external_user_lifecycle_action import AccessPackageExternalUserLifecycleAction
        from .entity import Entity

        from .access_package_external_user_lifecycle_action import AccessPackageExternalUserLifecycleAction
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "durationUntilExternalUserDeletedAfterBlocked": lambda n : setattr(self, 'duration_until_external_user_deleted_after_blocked', n.get_timedelta_value()),
            "externalUserLifecycleAction": lambda n : setattr(self, 'external_user_lifecycle_action', n.get_enum_value(AccessPackageExternalUserLifecycleAction)),
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
        writer.write_timedelta_value()("durationUntilExternalUserDeletedAfterBlocked", self.duration_until_external_user_deleted_after_blocked)
        writer.write_enum_value("externalUserLifecycleAction", self.external_user_lifecycle_action)
    

