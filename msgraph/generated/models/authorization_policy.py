from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .allow_invites_from import AllowInvitesFrom
    from .default_user_role_permissions import DefaultUserRolePermissions
    from .policy_base import PolicyBase

from .policy_base import PolicyBase

@dataclass
class AuthorizationPolicy(PolicyBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.authorizationPolicy"
    # Indicates whether a user can join the tenant by email validation.
    allow_email_verified_users_to_join_organization: Optional[bool] = None
    # Indicates who can invite external users to the organization. Possible values are: none, adminsAndGuestInviters, adminsGuestInvitersAndAllMembers, everyone.  everyone is the default setting for all cloud environments except US Government. For more information, see allowInvitesFrom values.
    allow_invites_from: Optional[AllowInvitesFrom] = None
    # Indicates whether user consent for risky apps is allowed. We recommend keeping allowUserConsentForRiskyApps as false. Default value is false.
    allow_user_consent_for_risky_apps: Optional[bool] = None
    # Indicates whether users can sign up for email based subscriptions.
    allowed_to_sign_up_email_based_subscriptions: Optional[bool] = None
    # Indicates whether users can use the Self-Service Password Reset feature on the tenant.
    allowed_to_use_s_s_p_r: Optional[bool] = None
    # To disable the use of MSOL PowerShell, set this property to true. This also disables user-based access to the legacy service endpoint used by MSOL PowerShell. This doesn't affect Microsoft Entra Connect or Microsoft Graph.
    block_msol_power_shell: Optional[bool] = None
    # The defaultUserRolePermissions property
    default_user_role_permissions: Optional[DefaultUserRolePermissions] = None
    # Represents role templateId for the role that should be granted to guest user. Currently following roles are supported:  User (a0b1b346-4d3e-4e8b-98f8-753987be4970), Guest User (10dae51f-b6af-4016-8d66-8c2a99b929b3), and Restricted Guest User (2af84b1e-32c8-42b7-82bc-daa82404023b).
    guest_user_role_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthorizationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthorizationPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .allow_invites_from import AllowInvitesFrom
        from .default_user_role_permissions import DefaultUserRolePermissions
        from .policy_base import PolicyBase

        from .allow_invites_from import AllowInvitesFrom
        from .default_user_role_permissions import DefaultUserRolePermissions
        from .policy_base import PolicyBase

        fields: Dict[str, Callable[[Any], None]] = {
            "allow_email_verified_users_to_join_organization": lambda n : setattr(self, 'allow_email_verified_users_to_join_organization', n.get_bool_value()),
            "allow_invites_from": lambda n : setattr(self, 'allow_invites_from', n.get_enum_value(AllowInvitesFrom)),
            "allow_user_consent_for_risky_apps": lambda n : setattr(self, 'allow_user_consent_for_risky_apps', n.get_bool_value()),
            "allowed_to_sign_up_email_based_subscriptions": lambda n : setattr(self, 'allowed_to_sign_up_email_based_subscriptions', n.get_bool_value()),
            "allowed_to_use_s_s_p_r": lambda n : setattr(self, 'allowed_to_use_s_s_p_r', n.get_bool_value()),
            "block_msol_power_shell": lambda n : setattr(self, 'block_msol_power_shell', n.get_bool_value()),
            "default_user_role_permissions": lambda n : setattr(self, 'default_user_role_permissions', n.get_object_value(DefaultUserRolePermissions)),
            "guest_user_role_id": lambda n : setattr(self, 'guest_user_role_id', n.get_uuid_value()),
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
        writer.write_bool_value("allow_email_verified_users_to_join_organization", self.allow_email_verified_users_to_join_organization)
        writer.write_enum_value("allow_invites_from", self.allow_invites_from)
        writer.write_bool_value("allow_user_consent_for_risky_apps", self.allow_user_consent_for_risky_apps)
        writer.write_bool_value("allowed_to_sign_up_email_based_subscriptions", self.allowed_to_sign_up_email_based_subscriptions)
        writer.write_bool_value("allowed_to_use_s_s_p_r", self.allowed_to_use_s_s_p_r)
        writer.write_bool_value("block_msol_power_shell", self.block_msol_power_shell)
        writer.write_object_value("default_user_role_permissions", self.default_user_role_permissions)
        writer.write_uuid_value("guest_user_role_id", self.guest_user_role_id)
    

