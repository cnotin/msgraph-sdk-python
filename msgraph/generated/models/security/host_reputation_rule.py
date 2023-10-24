from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .host_reputation_rule_severity import HostReputationRuleSeverity

@dataclass
class HostReputationRule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    BackingStore: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The description of the rule that gives more context.
    description: Optional[str] = None
    # The name of the rule.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Link to a web page with details related to this rule.
    related_details_url: Optional[str] = None
    # The severity property
    severity: Optional[HostReputationRuleSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostReputationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostReputationRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HostReputationRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .host_reputation_rule_severity import HostReputationRuleSeverity

        from .host_reputation_rule_severity import HostReputationRuleSeverity

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "relatedDetailsUrl": lambda n : setattr(self, 'related_details_url', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(HostReputationRuleSeverity)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("relatedDetailsUrl", self.related_details_url)
        writer.write_enum_value("severity", self.severity)
        writer.write_additional_data_value(self.additional_data)
    

