from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType

from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType

@dataclass
class WindowsUpdateActiveHoursInstall(WindowsUpdateInstallScheduleType):
    # The OdataType property
    OdataType: Optional[str] = "#microsoft.graph.windowsUpdateActiveHoursInstall"
    # Active Hours End
    active_hours_end: Optional[datetime.time] = None
    # Active Hours Start
    active_hours_start: Optional[datetime.time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateActiveHoursInstall:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateActiveHoursInstall
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsUpdateActiveHoursInstall()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType

        from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType

        fields: Dict[str, Callable[[Any], None]] = {
            "activeHoursEnd": lambda n : setattr(self, 'active_hours_end', n.get_time_value()),
            "activeHoursStart": lambda n : setattr(self, 'active_hours_start', n.get_time_value()),
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
        writer.write_time_value("activeHoursEnd", self.active_hours_end)
        writer.write_time_value("activeHoursStart", self.active_hours_start)
    

