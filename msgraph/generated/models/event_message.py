from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone
    from .event import Event
    from .event_message_request import EventMessageRequest
    from .event_message_response import EventMessageResponse
    from .event_type import EventType
    from .location import Location
    from .meeting_message_type import MeetingMessageType
    from .message import Message
    from .patterned_recurrence import PatternedRecurrence

from .message import Message

@dataclass
class EventMessage(Message):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.eventMessage"
    # The endDateTime property
    end_date_time: Optional[DateTimeTimeZone] = None
    # The event associated with the event message. The assumption for attendees or room resources is that the Calendar Attendant is set to automatically update the calendar with an event when meeting request event messages arrive. Navigation property.  Read-only.
    event: Optional[Event] = None
    # The isAllDay property
    is_all_day: Optional[bool] = None
    # The isDelegated property
    is_delegated: Optional[bool] = None
    # The isOutOfDate property
    is_out_of_date: Optional[bool] = None
    # The location property
    location: Optional[Location] = None
    # The meetingMessageType property
    meeting_message_type: Optional[MeetingMessageType] = None
    # The recurrence property
    recurrence: Optional[PatternedRecurrence] = None
    # The startDateTime property
    start_date_time: Optional[DateTimeTimeZone] = None
    # The type property
    type: Optional[EventType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EventMessage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageRequest".casefold():
            from .event_message_request import EventMessageRequest

            return EventMessageRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageResponse".casefold():
            from .event_message_response import EventMessageResponse

            return EventMessageResponse()
        return EventMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone
        from .event import Event
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .event_type import EventType
        from .location import Location
        from .meeting_message_type import MeetingMessageType
        from .message import Message
        from .patterned_recurrence import PatternedRecurrence

        from .date_time_time_zone import DateTimeTimeZone
        from .event import Event
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .event_type import EventType
        from .location import Location
        from .meeting_message_type import MeetingMessageType
        from .message import Message
        from .patterned_recurrence import PatternedRecurrence

        fields: Dict[str, Callable[[Any], None]] = {
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_object_value(DateTimeTimeZone)),
            "event": lambda n : setattr(self, 'event', n.get_object_value(Event)),
            "is_all_day": lambda n : setattr(self, 'is_all_day', n.get_bool_value()),
            "is_delegated": lambda n : setattr(self, 'is_delegated', n.get_bool_value()),
            "is_out_of_date": lambda n : setattr(self, 'is_out_of_date', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(Location)),
            "meeting_message_type": lambda n : setattr(self, 'meeting_message_type', n.get_enum_value(MeetingMessageType)),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PatternedRecurrence)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(EventType)),
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
        writer.write_object_value("end_date_time", self.end_date_time)
        writer.write_object_value("event", self.event)
        writer.write_bool_value("is_all_day", self.is_all_day)
        writer.write_bool_value("is_delegated", self.is_delegated)
        writer.write_bool_value("is_out_of_date", self.is_out_of_date)
        writer.write_object_value("location", self.location)
        writer.write_enum_value("meeting_message_type", self.meeting_message_type)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_object_value("start_date_time", self.start_date_time)
        writer.write_enum_value("type", self.type)
    

