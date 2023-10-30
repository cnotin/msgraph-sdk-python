from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_customer_information_base import BookingCustomerInformationBase
    from .booking_price_type import BookingPriceType
    from .booking_reminder import BookingReminder
    from .date_time_time_zone import DateTimeTimeZone
    from .entity import Entity
    from .location import Location

from .entity import Entity

@dataclass
class BookingAppointment(Entity):
    """
    Represents a booked appointment of a service by a customer in a business.
    """
    # Additional information that is sent to the customer when an appointment is confirmed.
    additional_information: Optional[str] = None
    # The URL of the meeting to join anonymously.
    anonymous_join_web_url: Optional[str] = None
    # The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
    customer_time_zone: Optional[str] = None
    # A collection of customer properties for an appointment. An appointment contains a list of customer information and each unit will indicate the properties of a customer who is part of that appointment. Optional.
    customers: Optional[List[BookingCustomerInformationBase]] = None
    # The length of the appointment, denoted in ISO8601 format.
    duration: Optional[datetime.timedelta] = None
    # The endDateTime property
    end_date_time: Optional[DateTimeTimeZone] = None
    # The current number of customers in the appointment
    filled_attendees_count: Optional[int] = None
    # If true, indicates that the appointment will be held online. Default value is false.
    is_location_online: Optional[bool] = None
    # The URL of the online meeting for the appointment.
    join_web_url: Optional[str] = None
    # The maximum number of customers allowed in an appointment. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
    maximum_attendees_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If true indicates that the bookingCustomer for this appointment doesn't wish to receive a confirmation for this appointment.
    opt_out_of_customer_email: Optional[bool] = None
    # The amount of time to reserve after the appointment ends, for cleaning up, as an example. The value is expressed in ISO8601 format.
    post_buffer: Optional[datetime.timedelta] = None
    # The amount of time to reserve before the appointment begins, for preparation, as an example. The value is expressed in ISO8601 format.
    pre_buffer: Optional[datetime.timedelta] = None
    # The regular price for an appointment for the specified bookingService.
    price: Optional[float] = None
    # Represents the type of pricing of a booking service.
    price_type: Optional[BookingPriceType] = None
    # The collection of customer reminders sent for this appointment. The value of this property is available only when reading this bookingAppointment by its ID.
    reminders: Optional[List[BookingReminder]] = None
    # An additional tracking ID for the appointment, if the appointment has been created directly by the customer on the scheduling page, as opposed to by a staff member on the behalf of the customer. Only supported for appointment if maxAttendeeCount is 1.
    self_service_appointment_id: Optional[str] = None
    # The ID of the bookingService associated with this appointment.
    service_id: Optional[str] = None
    # The location where the service is delivered.
    service_location: Optional[Location] = None
    # The name of the bookingService associated with this appointment.This property is optional when creating a new appointment. If not specified, it's computed from the service associated with the appointment by the serviceId property.
    service_name: Optional[str] = None
    # Notes from a bookingStaffMember. The value of this property is available only when reading this bookingAppointment by its ID.
    service_notes: Optional[str] = None
    # If true, indicates SMS notifications will be sent to the customers for the appointment. Default value is false.
    sms_notifications_enabled: Optional[bool] = None
    # The ID of each bookingStaffMember who is scheduled in this appointment.
    staff_member_ids: Optional[List[str]] = None
    # The startDateTime property
    start_date_time: Optional[DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingAppointment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingAppointment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BookingAppointment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .booking_customer_information_base import BookingCustomerInformationBase
        from .booking_price_type import BookingPriceType
        from .booking_reminder import BookingReminder
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .location import Location

        from .booking_customer_information_base import BookingCustomerInformationBase
        from .booking_price_type import BookingPriceType
        from .booking_reminder import BookingReminder
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .location import Location

        fields: Dict[str, Callable[[Any], None]] = {
            "additional_information": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "anonymous_join_web_url": lambda n : setattr(self, 'anonymous_join_web_url', n.get_str_value()),
            "customer_time_zone": lambda n : setattr(self, 'customer_time_zone', n.get_str_value()),
            "customers": lambda n : setattr(self, 'customers', n.get_collection_of_object_values(BookingCustomerInformationBase)),
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_object_value(DateTimeTimeZone)),
            "filled_attendees_count": lambda n : setattr(self, 'filled_attendees_count', n.get_int_value()),
            "is_location_online": lambda n : setattr(self, 'is_location_online', n.get_bool_value()),
            "join_web_url": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "maximum_attendees_count": lambda n : setattr(self, 'maximum_attendees_count', n.get_int_value()),
            "opt_out_of_customer_email": lambda n : setattr(self, 'opt_out_of_customer_email', n.get_bool_value()),
            "post_buffer": lambda n : setattr(self, 'post_buffer', n.get_timedelta_value()),
            "pre_buffer": lambda n : setattr(self, 'pre_buffer', n.get_timedelta_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "price_type": lambda n : setattr(self, 'price_type', n.get_enum_value(BookingPriceType)),
            "reminders": lambda n : setattr(self, 'reminders', n.get_collection_of_object_values(BookingReminder)),
            "self_service_appointment_id": lambda n : setattr(self, 'self_service_appointment_id', n.get_str_value()),
            "service_id": lambda n : setattr(self, 'service_id', n.get_str_value()),
            "service_location": lambda n : setattr(self, 'service_location', n.get_object_value(Location)),
            "service_name": lambda n : setattr(self, 'service_name', n.get_str_value()),
            "service_notes": lambda n : setattr(self, 'service_notes', n.get_str_value()),
            "sms_notifications_enabled": lambda n : setattr(self, 'sms_notifications_enabled', n.get_bool_value()),
            "staff_member_ids": lambda n : setattr(self, 'staff_member_ids', n.get_collection_of_primitive_values(str)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
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
        writer.write_str_value("additional_information", self.additional_information)
        writer.write_str_value("anonymous_join_web_url", self.anonymous_join_web_url)
        writer.write_str_value("customer_time_zone", self.customer_time_zone)
        writer.write_collection_of_object_values("customers", self.customers)
        writer.write_object_value("end_date_time", self.end_date_time)
        writer.write_bool_value("is_location_online", self.is_location_online)
        writer.write_str_value("join_web_url", self.join_web_url)
        writer.write_int_value("maximum_attendees_count", self.maximum_attendees_count)
        writer.write_bool_value("opt_out_of_customer_email", self.opt_out_of_customer_email)
        writer.write_timedelta_value("post_buffer", self.post_buffer)
        writer.write_timedelta_value("pre_buffer", self.pre_buffer)
        writer.write_float_value("price", self.price)
        writer.write_enum_value("price_type", self.price_type)
        writer.write_collection_of_object_values("reminders", self.reminders)
        writer.write_str_value("self_service_appointment_id", self.self_service_appointment_id)
        writer.write_str_value("service_id", self.service_id)
        writer.write_object_value("service_location", self.service_location)
        writer.write_str_value("service_name", self.service_name)
        writer.write_str_value("service_notes", self.service_notes)
        writer.write_bool_value("sms_notifications_enabled", self.sms_notifications_enabled)
        writer.write_collection_of_primitive_values("staff_member_ids", self.staff_member_ids)
        writer.write_object_value("start_date_time", self.start_date_time)
    

