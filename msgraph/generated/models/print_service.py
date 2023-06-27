from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .print_service_endpoint import PrintServiceEndpoint

from .entity import Entity

@dataclass
class PrintService(Entity):
    # Endpoints that can be used to access the service. Read-only. Nullable.
    endpoints: Optional[List[PrintServiceEndpoint]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintService
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrintService()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .print_service_endpoint import PrintServiceEndpoint

        from .entity import Entity
        from .print_service_endpoint import PrintServiceEndpoint

        fields: Dict[str, Callable[[Any], None]] = {
            "endpoints": lambda n : setattr(self, 'endpoints', n.get_collection_of_object_values(PrintServiceEndpoint)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("endpoints", self.endpoints)
    

