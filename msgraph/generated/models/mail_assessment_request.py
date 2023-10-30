from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mail_destination_routing_reason import MailDestinationRoutingReason
    from .threat_assessment_request import ThreatAssessmentRequest

from .threat_assessment_request import ThreatAssessmentRequest

@dataclass
class MailAssessmentRequest(ThreatAssessmentRequest):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mailAssessmentRequest"
    # The reason for mail routed to its destination. Possible values are: none, mailFlowRule, safeSender, blockedSender, advancedSpamFiltering, domainAllowList, domainBlockList, notInAddressBook, firstTimeSender, autoPurgeToInbox, autoPurgeToJunk, autoPurgeToDeleted, outbound, notJunk, junk.
    destination_routing_reason: Optional[MailDestinationRoutingReason] = None
    # The resource URI of the mail message for assessment.
    message_uri: Optional[str] = None
    # The mail recipient whose policies are used to assess the mail.
    recipient_email: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MailAssessmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailAssessmentRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MailAssessmentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mail_destination_routing_reason import MailDestinationRoutingReason
        from .threat_assessment_request import ThreatAssessmentRequest

        from .mail_destination_routing_reason import MailDestinationRoutingReason
        from .threat_assessment_request import ThreatAssessmentRequest

        fields: Dict[str, Callable[[Any], None]] = {
            "destination_routing_reason": lambda n : setattr(self, 'destination_routing_reason', n.get_enum_value(MailDestinationRoutingReason)),
            "message_uri": lambda n : setattr(self, 'message_uri', n.get_str_value()),
            "recipient_email": lambda n : setattr(self, 'recipient_email', n.get_str_value()),
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
        writer.write_enum_value("destination_routing_reason", self.destination_routing_reason)
        writer.write_str_value("message_uri", self.message_uri)
        writer.write_str_value("recipient_email", self.recipient_email)
    

