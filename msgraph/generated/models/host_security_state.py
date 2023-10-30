from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class HostSecurityState(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Host FQDN (Fully Qualified Domain Name) (for example, machine.company.com).
    fqdn: Optional[str] = None
    # The isAzureAdJoined property
    is_azure_ad_joined: Optional[bool] = None
    # The isAzureAdRegistered property
    is_azure_ad_registered: Optional[bool] = None
    # True if the host is domain joined to an on-premises Active Directory domain.
    is_hybrid_azure_domain_joined: Optional[bool] = None
    # The local host name, without the DNS domain name.
    net_bios_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Host Operating System. (For example, Windows 10, macOS, RHEL, etc.).
    os: Optional[str] = None
    # Private (not routable) IPv4 or IPv6 address (see RFC 1918) at the time of the alert.
    private_ip_address: Optional[str] = None
    # Publicly routable IPv4 or IPv6 address (see RFC 1918) at time of the alert.
    public_ip_address: Optional[str] = None
    # Provider-generated/calculated risk score of the host.  Recommended value range of 0-1, which equates to a percentage.
    risk_score: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostSecurityState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HostSecurityState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "fqdn": lambda n : setattr(self, 'fqdn', n.get_str_value()),
            "is_azure_ad_joined": lambda n : setattr(self, 'is_azure_ad_joined', n.get_bool_value()),
            "is_azure_ad_registered": lambda n : setattr(self, 'is_azure_ad_registered', n.get_bool_value()),
            "is_hybrid_azure_domain_joined": lambda n : setattr(self, 'is_hybrid_azure_domain_joined', n.get_bool_value()),
            "net_bios_name": lambda n : setattr(self, 'net_bios_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "private_ip_address": lambda n : setattr(self, 'private_ip_address', n.get_str_value()),
            "public_ip_address": lambda n : setattr(self, 'public_ip_address', n.get_str_value()),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("fqdn", self.fqdn)
        writer.write_bool_value("is_azure_ad_joined", self.is_azure_ad_joined)
        writer.write_bool_value("is_azure_ad_registered", self.is_azure_ad_registered)
        writer.write_bool_value("is_hybrid_azure_domain_joined", self.is_hybrid_azure_domain_joined)
        writer.write_str_value("net_bios_name", self.net_bios_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("os", self.os)
        writer.write_str_value("private_ip_address", self.private_ip_address)
        writer.write_str_value("public_ip_address", self.public_ip_address)
        writer.write_str_value("risk_score", self.risk_score)
        writer.write_additional_data_value(self.additional_data)
    

