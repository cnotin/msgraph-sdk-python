from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class NumberValuePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The decimalSeparator property
    decimal_separator: Optional[Json] = None
    # The groupSeparator property
    group_separator: Optional[Json] = None
    # The text property
    text: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NumberValuePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NumberValuePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return NumberValuePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "decimal_separator": lambda n : setattr(self, 'decimal_separator', n.get_object_value(Json)),
            "group_separator": lambda n : setattr(self, 'group_separator', n.get_object_value(Json)),
            "text": lambda n : setattr(self, 'text', n.get_object_value(Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("decimal_separator", self.decimal_separator)
        writer.write_object_value("group_separator", self.group_separator)
        writer.write_object_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

