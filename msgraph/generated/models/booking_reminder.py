from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_reminder_recipients import BookingReminderRecipients

@dataclass
class BookingReminder(AdditionalDataHolder, Parsable):
    """
    This type represents when and to whom to send an e-mail reminder.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The message in the reminder.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The amount of time before the start of an appointment that the reminder should be sent. It's denoted in ISO 8601 format.
    offset: Optional[datetime.timedelta] = None
    # The recipients property
    recipients: Optional[BookingReminderRecipients] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingReminder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingReminder
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BookingReminder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .booking_reminder_recipients import BookingReminderRecipients

        from .booking_reminder_recipients import BookingReminderRecipients

        fields: Dict[str, Callable[[Any], None]] = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_timedelta_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_enum_value(BookingReminderRecipients)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_timedelta_value()("offset", self.offset)
        writer.write_enum_value("recipients", self.recipients)
        writer.write_additional_data_value(self.additional_data)
    

