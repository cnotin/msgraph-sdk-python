from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .federated_idp_mfa_behavior import FederatedIdpMfaBehavior
    from .prompt_login_behavior import PromptLoginBehavior
    from .saml_or_ws_fed_provider import SamlOrWsFedProvider
    from .signing_certificate_update_status import SigningCertificateUpdateStatus

from .saml_or_ws_fed_provider import SamlOrWsFedProvider

@dataclass
class InternalDomainFederation(SamlOrWsFedProvider):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.internalDomainFederation"
    # URL of the endpoint used by active clients when authenticating with federated domains set up for single sign-on in Microsoft Entra ID. Corresponds to the ActiveLogOnUri property of the Set-MsolDomainFederationSettings MSOnline v1 PowerShell cmdlet.
    active_sign_in_uri: Optional[str] = None
    # Determines whether Microsoft Entra ID accepts the MFA performed by the federated IdP when a federated user accesses an application that is governed by a conditional access policy that requires MFA. The possible values are: acceptIfMfaDoneByFederatedIdp, enforceMfaByFederatedIdp, rejectMfaByFederatedIdp, unknownFutureValue. For more information, see federatedIdpMfaBehavior values.
    federated_idp_mfa_behavior: Optional[FederatedIdpMfaBehavior] = None
    # If true, when SAML authentication requests are sent to the federated SAML IdP, Microsoft Entra ID will sign those requests using the OrgID signing key. If false (default), the SAML authentication requests sent to the federated IdP are not signed.
    is_signed_authentication_request_required: Optional[bool] = None
    # Fallback token signing certificate that is used to sign tokens when the primary signing certificate expires. Formatted as Base64 encoded strings of the public portion of the federated IdP's token signing certificate. Needs to be compatible with the X509Certificate2 class. Much like the signingCertificate, the nextSigningCertificate property is used if a rollover is required outside of the auto-rollover update, a new federation service is being set up, or if the new token signing certificate is not present in the federation properties after the federation service certificate has been updated.
    next_signing_certificate: Optional[str] = None
    # Sets the preferred behavior for the sign-in prompt. The possible values are: translateToFreshPasswordAuthentication, nativeSupport, disabled, unknownFutureValue.
    prompt_login_behavior: Optional[PromptLoginBehavior] = None
    # URI that clients are redirected to when they sign out of Microsoft Entra services. Corresponds to the LogOffUri property of the Set-MsolDomainFederationSettings MSOnline v1 PowerShell cmdlet.
    sign_out_uri: Optional[str] = None
    # Provides status and timestamp of the last update of the signing certificate.
    signing_certificate_update_status: Optional[SigningCertificateUpdateStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InternalDomainFederation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InternalDomainFederation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InternalDomainFederation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .federated_idp_mfa_behavior import FederatedIdpMfaBehavior
        from .prompt_login_behavior import PromptLoginBehavior
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .signing_certificate_update_status import SigningCertificateUpdateStatus

        from .federated_idp_mfa_behavior import FederatedIdpMfaBehavior
        from .prompt_login_behavior import PromptLoginBehavior
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .signing_certificate_update_status import SigningCertificateUpdateStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "active_sign_in_uri": lambda n : setattr(self, 'active_sign_in_uri', n.get_str_value()),
            "federated_idp_mfa_behavior": lambda n : setattr(self, 'federated_idp_mfa_behavior', n.get_enum_value(FederatedIdpMfaBehavior)),
            "is_signed_authentication_request_required": lambda n : setattr(self, 'is_signed_authentication_request_required', n.get_bool_value()),
            "next_signing_certificate": lambda n : setattr(self, 'next_signing_certificate', n.get_str_value()),
            "prompt_login_behavior": lambda n : setattr(self, 'prompt_login_behavior', n.get_enum_value(PromptLoginBehavior)),
            "sign_out_uri": lambda n : setattr(self, 'sign_out_uri', n.get_str_value()),
            "signing_certificate_update_status": lambda n : setattr(self, 'signing_certificate_update_status', n.get_object_value(SigningCertificateUpdateStatus)),
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
        writer.write_str_value("active_sign_in_uri", self.active_sign_in_uri)
        writer.write_enum_value("federated_idp_mfa_behavior", self.federated_idp_mfa_behavior)
        writer.write_bool_value("is_signed_authentication_request_required", self.is_signed_authentication_request_required)
        writer.write_str_value("next_signing_certificate", self.next_signing_certificate)
        writer.write_enum_value("prompt_login_behavior", self.prompt_login_behavior)
        writer.write_str_value("sign_out_uri", self.sign_out_uri)
        writer.write_object_value("signing_certificate_update_status", self.signing_certificate_update_status)
    

