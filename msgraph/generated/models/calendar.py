from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .calendar_color import CalendarColor
    from .calendar_permission import CalendarPermission
    from .email_address import EmailAddress
    from .entity import Entity
    from .event import Event
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .online_meeting_provider_type import OnlineMeetingProviderType
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

from .entity import Entity

@dataclass
class Calendar(Entity):
    # Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
    allowed_online_meeting_providers: Optional[List[OnlineMeetingProviderType]] = None
    # The permissions of the users with whom the calendar is shared.
    calendar_permissions: Optional[List[CalendarPermission]] = None
    # The calendar view for the calendar. Navigation property. Read-only.
    calendar_view: Optional[List[Event]] = None
    # true if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.
    can_edit: Optional[bool] = None
    # true if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.
    can_share: Optional[bool] = None
    # true if the user can read calendar items that have been marked private, false otherwise.
    can_view_private_items: Optional[bool] = None
    # Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
    change_key: Optional[str] = None
    # Specifies the color theme to distinguish the calendar from other calendars in a UI. The property values are: auto, lightBlue, lightGreen, lightOrange, lightGray, lightYellow, lightTeal, lightPink, lightBrown, lightRed, maxColor.
    color: Optional[CalendarColor] = None
    # The default online meeting provider for meetings sent from this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
    default_online_meeting_provider: Optional[OnlineMeetingProviderType] = None
    # The events in the calendar. Navigation property. Read-only.
    events: Optional[List[Event]] = None
    # The calendar color, expressed in a hex color code of three hexadecimal values, each ranging from 00 to FF and representing the red, green, or blue components of the color in the RGB color space. If the user has never explicitly set a color for the calendar, this property is empty. Read-only.
    hex_color: Optional[str] = None
    # true if this is the default calendar where new events are created by default, false otherwise.
    is_default_calendar: Optional[bool] = None
    # Indicates whether this user calendar can be deleted from the user mailbox.
    is_removable: Optional[bool] = None
    # Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.
    is_tallying_responses: Optional[bool] = None
    # The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.
    multi_value_extended_properties: Optional[List[MultiValueLegacyExtendedProperty]] = None
    # The calendar name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If set, this represents the user who created or added the calendar. For a calendar that the user created or added, the owner property is set to the user. For a calendar shared with the user, the owner property is set to the person who shared that calendar with the user.
    owner: Optional[EmailAddress] = None
    # The collection of single-value extended properties defined for the calendar. Read-only. Nullable.
    single_value_extended_properties: Optional[List[SingleValueLegacyExtendedProperty]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Calendar:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Calendar
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Calendar()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .calendar_color import CalendarColor
        from .calendar_permission import CalendarPermission
        from .email_address import EmailAddress
        from .entity import Entity
        from .event import Event
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .online_meeting_provider_type import OnlineMeetingProviderType
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        from .calendar_color import CalendarColor
        from .calendar_permission import CalendarPermission
        from .email_address import EmailAddress
        from .entity import Entity
        from .event import Event
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .online_meeting_provider_type import OnlineMeetingProviderType
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        fields: Dict[str, Callable[[Any], None]] = {
            "allowed_online_meeting_providers": lambda n : setattr(self, 'allowed_online_meeting_providers', n.get_collection_of_enum_values(OnlineMeetingProviderType)),
            "calendar_permissions": lambda n : setattr(self, 'calendar_permissions', n.get_collection_of_object_values(CalendarPermission)),
            "calendar_view": lambda n : setattr(self, 'calendar_view', n.get_collection_of_object_values(Event)),
            "can_edit": lambda n : setattr(self, 'can_edit', n.get_bool_value()),
            "can_share": lambda n : setattr(self, 'can_share', n.get_bool_value()),
            "can_view_private_items": lambda n : setattr(self, 'can_view_private_items', n.get_bool_value()),
            "change_key": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "color": lambda n : setattr(self, 'color', n.get_enum_value(CalendarColor)),
            "default_online_meeting_provider": lambda n : setattr(self, 'default_online_meeting_provider', n.get_enum_value(OnlineMeetingProviderType)),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(Event)),
            "hex_color": lambda n : setattr(self, 'hex_color', n.get_str_value()),
            "is_default_calendar": lambda n : setattr(self, 'is_default_calendar', n.get_bool_value()),
            "is_removable": lambda n : setattr(self, 'is_removable', n.get_bool_value()),
            "is_tallying_responses": lambda n : setattr(self, 'is_tallying_responses', n.get_bool_value()),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(EmailAddress)),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
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
        writer.write_collection_of_enum_values("allowed_online_meeting_providers", self.allowed_online_meeting_providers)
        writer.write_collection_of_object_values("calendar_permissions", self.calendar_permissions)
        writer.write_collection_of_object_values("calendar_view", self.calendar_view)
        writer.write_bool_value("can_edit", self.can_edit)
        writer.write_bool_value("can_share", self.can_share)
        writer.write_bool_value("can_view_private_items", self.can_view_private_items)
        writer.write_str_value("change_key", self.change_key)
        writer.write_enum_value("color", self.color)
        writer.write_enum_value("default_online_meeting_provider", self.default_online_meeting_provider)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_str_value("hex_color", self.hex_color)
        writer.write_bool_value("is_default_calendar", self.is_default_calendar)
        writer.write_bool_value("is_removable", self.is_removable)
        writer.write_bool_value("is_tallying_responses", self.is_tallying_responses)
        writer.write_collection_of_object_values("multi_value_extended_properties", self.multi_value_extended_properties)
        writer.write_str_value("name", self.name)
        writer.write_object_value("owner", self.owner)
        writer.write_collection_of_object_values("single_value_extended_properties", self.single_value_extended_properties)
    

