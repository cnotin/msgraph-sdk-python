from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_type import BookingType
    from .place import Place

from .place import Place

@dataclass
class Room(Place):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.room"
    # Specifies the name of the audio device in the room.
    audio_device_name: Optional[str] = None
    # Type of room. Possible values are standard, and reserved.
    booking_type: Optional[BookingType] = None
    # Specifies the building name or building number that the room is in.
    building: Optional[str] = None
    # Specifies the capacity of the room.
    capacity: Optional[int] = None
    # Specifies the name of the display device in the room.
    display_device_name: Optional[str] = None
    # Email address of the room.
    email_address: Optional[str] = None
    # Specifies a descriptive label for the floor, for example, P.
    floor_label: Optional[str] = None
    # Specifies the floor number that the room is on.
    floor_number: Optional[int] = None
    # Specifies whether the room is wheelchair accessible.
    is_wheel_chair_accessible: Optional[bool] = None
    # Specifies a descriptive label for the room, for example, a number or name.
    label: Optional[str] = None
    # Specifies a nickname for the room, for example, 'conf room'.
    nickname: Optional[str] = None
    # Specifies additional features of the room, for example, details like the type of view or furniture type.
    tags: Optional[List[str]] = None
    # Specifies the name of the video device in the room.
    video_device_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Room:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Room
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Room()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .booking_type import BookingType
        from .place import Place

        from .booking_type import BookingType
        from .place import Place

        fields: Dict[str, Callable[[Any], None]] = {
            "audio_device_name": lambda n : setattr(self, 'audio_device_name', n.get_str_value()),
            "booking_type": lambda n : setattr(self, 'booking_type', n.get_enum_value(BookingType)),
            "building": lambda n : setattr(self, 'building', n.get_str_value()),
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "display_device_name": lambda n : setattr(self, 'display_device_name', n.get_str_value()),
            "email_address": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "floor_label": lambda n : setattr(self, 'floor_label', n.get_str_value()),
            "floor_number": lambda n : setattr(self, 'floor_number', n.get_int_value()),
            "is_wheel_chair_accessible": lambda n : setattr(self, 'is_wheel_chair_accessible', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "nickname": lambda n : setattr(self, 'nickname', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "video_device_name": lambda n : setattr(self, 'video_device_name', n.get_str_value()),
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
        writer.write_str_value("audio_device_name", self.audio_device_name)
        writer.write_enum_value("booking_type", self.booking_type)
        writer.write_str_value("building", self.building)
        writer.write_int_value("capacity", self.capacity)
        writer.write_str_value("display_device_name", self.display_device_name)
        writer.write_str_value("email_address", self.email_address)
        writer.write_str_value("floor_label", self.floor_label)
        writer.write_int_value("floor_number", self.floor_number)
        writer.write_bool_value("is_wheel_chair_accessible", self.is_wheel_chair_accessible)
        writer.write_str_value("label", self.label)
        writer.write_str_value("nickname", self.nickname)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("video_device_name", self.video_device_name)
    

