from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .host import Host

from ..entity import Entity

@dataclass
class HostPair(Entity):
    # The childHost property
    child_host: Optional[Host] = None
    # The date and time when Microsoft Defender Threat Intelligence first observed the hostPair. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    first_seen_date_time: Optional[datetime.datetime] = None
    # The date and time when Microsoft Defender Threat Intelligence last observed the hostPair. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime.datetime] = None
    # The reason that two hosts are identified as hostPair.
    link_kind: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parentHost property
    parent_host: Optional[Host] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostPair:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostPair
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HostPair()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .host import Host

        from ..entity import Entity
        from .host import Host

        fields: Dict[str, Callable[[Any], None]] = {
            "child_host": lambda n : setattr(self, 'child_host', n.get_object_value(Host)),
            "first_seen_date_time": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "last_seen_date_time": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "link_kind": lambda n : setattr(self, 'link_kind', n.get_str_value()),
            "parent_host": lambda n : setattr(self, 'parent_host', n.get_object_value(Host)),
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
        writer.write_object_value("child_host", self.child_host)
        writer.write_datetime_value("first_seen_date_time", self.first_seen_date_time)
        writer.write_datetime_value("last_seen_date_time", self.last_seen_date_time)
        writer.write_str_value("link_kind", self.link_kind)
        writer.write_object_value("parent_host", self.parent_host)
    

