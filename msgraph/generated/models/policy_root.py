from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
    from .admin_consent_request_policy import AdminConsentRequestPolicy
    from .app_management_policy import AppManagementPolicy
    from .authentication_flows_policy import AuthenticationFlowsPolicy
    from .authentication_methods_policy import AuthenticationMethodsPolicy
    from .authentication_strength_policy import AuthenticationStrengthPolicy
    from .authorization_policy import AuthorizationPolicy
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .conditional_access_policy import ConditionalAccessPolicy
    from .cross_tenant_access_policy import CrossTenantAccessPolicy
    from .entity import Entity
    from .feature_rollout_policy import FeatureRolloutPolicy
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
    from .permission_grant_policy import PermissionGrantPolicy
    from .tenant_app_management_policy import TenantAppManagementPolicy
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy
    from .unified_role_management_policy import UnifiedRoleManagementPolicy
    from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

from .entity import Entity

@dataclass
class PolicyRoot(Entity):
    # The policy that controls the idle time out for web sessions for applications.
    activity_based_timeout_policies: Optional[List[ActivityBasedTimeoutPolicy]] = None
    # The policy by which consent requests are created and managed for the entire tenant.
    admin_consent_request_policy: Optional[AdminConsentRequestPolicy] = None
    # The policies that enforce app management restrictions for specific applications and service principals, overriding the defaultAppManagementPolicy.
    app_management_policies: Optional[List[AppManagementPolicy]] = None
    # The policy configuration of the self-service sign-up experience of external users.
    authentication_flows_policy: Optional[AuthenticationFlowsPolicy] = None
    # The authentication methods and the users that are allowed to use them to sign in and perform multifactor authentication (MFA) in Microsoft Entra ID.
    authentication_methods_policy: Optional[AuthenticationMethodsPolicy] = None
    # The authentication method combinations that are to be used in scenarios defined by Microsoft Entra Conditional Access.
    authentication_strength_policies: Optional[List[AuthenticationStrengthPolicy]] = None
    # The policy that controls Microsoft Entra authorization settings.
    authorization_policy: Optional[AuthorizationPolicy] = None
    # The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
    claims_mapping_policies: Optional[List[ClaimsMappingPolicy]] = None
    # The custom rules that define an access scenario.
    conditional_access_policies: Optional[List[ConditionalAccessPolicy]] = None
    # The custom rules that define an access scenario when interacting with external Microsoft Entra tenants.
    cross_tenant_access_policy: Optional[CrossTenantAccessPolicy] = None
    # The tenant-wide policy that enforces app management restrictions for all applications and service principals.
    default_app_management_policy: Optional[TenantAppManagementPolicy] = None
    # The feature rollout policy associated with a directory object.
    feature_rollout_policies: Optional[List[FeatureRolloutPolicy]] = None
    # The policy to control Microsoft Entra authentication behavior for federated users.
    home_realm_discovery_policies: Optional[List[HomeRealmDiscoveryPolicy]] = None
    # The policy that represents the security defaults that protect against common attacks.
    identity_security_defaults_enforcement_policy: Optional[IdentitySecurityDefaultsEnforcementPolicy] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy that specifies the conditions under which consent can be granted.
    permission_grant_policies: Optional[List[PermissionGrantPolicy]] = None
    # Specifies the various policies associated with scopes and roles.
    role_management_policies: Optional[List[UnifiedRoleManagementPolicy]] = None
    # The assignment of a role management policy to a role definition object.
    role_management_policy_assignments: Optional[List[UnifiedRoleManagementPolicyAssignment]] = None
    # The policy that specifies the characteristics of SAML tokens issued by Microsoft Entra ID.
    token_issuance_policies: Optional[List[TokenIssuancePolicy]] = None
    # The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Microsoft Entra ID.
    token_lifetime_policies: Optional[List[TokenLifetimePolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicyRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PolicyRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .app_management_policy import AppManagementPolicy
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authorization_policy import AuthorizationPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .conditional_access_policy import ConditionalAccessPolicy
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .entity import Entity
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .permission_grant_policy import PermissionGrantPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .app_management_policy import AppManagementPolicy
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authorization_policy import AuthorizationPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .conditional_access_policy import ConditionalAccessPolicy
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .entity import Entity
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .permission_grant_policy import PermissionGrantPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

        fields: Dict[str, Callable[[Any], None]] = {
            "activity_based_timeout_policies": lambda n : setattr(self, 'activity_based_timeout_policies', n.get_collection_of_object_values(ActivityBasedTimeoutPolicy)),
            "admin_consent_request_policy": lambda n : setattr(self, 'admin_consent_request_policy', n.get_object_value(AdminConsentRequestPolicy)),
            "app_management_policies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(AppManagementPolicy)),
            "authentication_flows_policy": lambda n : setattr(self, 'authentication_flows_policy', n.get_object_value(AuthenticationFlowsPolicy)),
            "authentication_methods_policy": lambda n : setattr(self, 'authentication_methods_policy', n.get_object_value(AuthenticationMethodsPolicy)),
            "authentication_strength_policies": lambda n : setattr(self, 'authentication_strength_policies', n.get_collection_of_object_values(AuthenticationStrengthPolicy)),
            "authorization_policy": lambda n : setattr(self, 'authorization_policy', n.get_object_value(AuthorizationPolicy)),
            "claims_mapping_policies": lambda n : setattr(self, 'claims_mapping_policies', n.get_collection_of_object_values(ClaimsMappingPolicy)),
            "conditional_access_policies": lambda n : setattr(self, 'conditional_access_policies', n.get_collection_of_object_values(ConditionalAccessPolicy)),
            "cross_tenant_access_policy": lambda n : setattr(self, 'cross_tenant_access_policy', n.get_object_value(CrossTenantAccessPolicy)),
            "default_app_management_policy": lambda n : setattr(self, 'default_app_management_policy', n.get_object_value(TenantAppManagementPolicy)),
            "feature_rollout_policies": lambda n : setattr(self, 'feature_rollout_policies', n.get_collection_of_object_values(FeatureRolloutPolicy)),
            "home_realm_discovery_policies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(HomeRealmDiscoveryPolicy)),
            "identity_security_defaults_enforcement_policy": lambda n : setattr(self, 'identity_security_defaults_enforcement_policy', n.get_object_value(IdentitySecurityDefaultsEnforcementPolicy)),
            "permission_grant_policies": lambda n : setattr(self, 'permission_grant_policies', n.get_collection_of_object_values(PermissionGrantPolicy)),
            "role_management_policies": lambda n : setattr(self, 'role_management_policies', n.get_collection_of_object_values(UnifiedRoleManagementPolicy)),
            "role_management_policy_assignments": lambda n : setattr(self, 'role_management_policy_assignments', n.get_collection_of_object_values(UnifiedRoleManagementPolicyAssignment)),
            "token_issuance_policies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(TokenIssuancePolicy)),
            "token_lifetime_policies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(TokenLifetimePolicy)),
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
        writer.write_collection_of_object_values("activity_based_timeout_policies", self.activity_based_timeout_policies)
        writer.write_object_value("admin_consent_request_policy", self.admin_consent_request_policy)
        writer.write_collection_of_object_values("app_management_policies", self.app_management_policies)
        writer.write_object_value("authentication_flows_policy", self.authentication_flows_policy)
        writer.write_object_value("authentication_methods_policy", self.authentication_methods_policy)
        writer.write_collection_of_object_values("authentication_strength_policies", self.authentication_strength_policies)
        writer.write_object_value("authorization_policy", self.authorization_policy)
        writer.write_collection_of_object_values("claims_mapping_policies", self.claims_mapping_policies)
        writer.write_collection_of_object_values("conditional_access_policies", self.conditional_access_policies)
        writer.write_object_value("cross_tenant_access_policy", self.cross_tenant_access_policy)
        writer.write_object_value("default_app_management_policy", self.default_app_management_policy)
        writer.write_collection_of_object_values("feature_rollout_policies", self.feature_rollout_policies)
        writer.write_collection_of_object_values("home_realm_discovery_policies", self.home_realm_discovery_policies)
        writer.write_object_value("identity_security_defaults_enforcement_policy", self.identity_security_defaults_enforcement_policy)
        writer.write_collection_of_object_values("permission_grant_policies", self.permission_grant_policies)
        writer.write_collection_of_object_values("role_management_policies", self.role_management_policies)
        writer.write_collection_of_object_values("role_management_policy_assignments", self.role_management_policy_assignments)
        writer.write_collection_of_object_values("token_issuance_policies", self.token_issuance_policies)
        writer.write_collection_of_object_values("token_lifetime_policies", self.token_lifetime_policies)
    

