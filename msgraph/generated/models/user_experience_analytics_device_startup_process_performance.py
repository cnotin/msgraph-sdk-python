from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsDeviceStartupProcessPerformance(Entity):
    """
    The user experience analytics device startup process performance.
    """
    # The count of devices which initiated this process on startup. Supports: $filter, $select, $OrderBy. Read-only.
    device_count: Optional[int] = None
    # The median impact of startup process on device boot time in milliseconds. Supports: $filter, $select, $OrderBy. Read-only.
    median_impact_in_ms: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the startup process. Examples: outlook, excel. Supports: $select, $OrderBy. Read-only.
    process_name: Optional[str] = None
    # The product name of the startup process. Examples: Microsoft Outlook, Microsoft Excel. Supports: $select, $OrderBy. Read-only.
    product_name: Optional[str] = None
    # The publisher of the startup process. Examples: Microsoft Corporation, Contoso Corp. Supports: $select, $OrderBy. Read-only.
    publisher: Optional[str] = None
    # The total impact of startup process on device boot time in milliseconds. Supports: $filter, $select, $OrderBy. Read-only.
    total_impact_in_ms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceStartupProcessPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceStartupProcessPerformance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDeviceStartupProcessPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "device_count": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "median_impact_in_ms": lambda n : setattr(self, 'median_impact_in_ms', n.get_int_value()),
            "process_name": lambda n : setattr(self, 'process_name', n.get_str_value()),
            "product_name": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "total_impact_in_ms": lambda n : setattr(self, 'total_impact_in_ms', n.get_int_value()),
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
        writer.write_int_value("device_count", self.device_count)
        writer.write_int_value("median_impact_in_ms", self.median_impact_in_ms)
        writer.write_str_value("process_name", self.process_name)
        writer.write_str_value("product_name", self.product_name)
        writer.write_str_value("publisher", self.publisher)
        writer.write_int_value("total_impact_in_ms", self.total_impact_in_ms)
    

