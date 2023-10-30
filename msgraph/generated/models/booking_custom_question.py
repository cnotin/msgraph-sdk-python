from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .answer_input_type import AnswerInputType
    from .entity import Entity

from .entity import Entity

@dataclass
class BookingCustomQuestion(Entity):
    """
    Represents a custom question of the business.
    """
    # The expected answer type. The possible values are: text, radioButton, unknownFutureValue.
    answer_input_type: Optional[AnswerInputType] = None
    # List of possible answer values.
    answer_options: Optional[List[str]] = None
    # The question.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingCustomQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingCustomQuestion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BookingCustomQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .answer_input_type import AnswerInputType
        from .entity import Entity

        from .answer_input_type import AnswerInputType
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "answer_input_type": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(AnswerInputType)),
            "answer_options": lambda n : setattr(self, 'answer_options', n.get_collection_of_primitive_values(str)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_enum_value("answer_input_type", self.answer_input_type)
        writer.write_collection_of_primitive_values("answer_options", self.answer_options)
        writer.write_str_value("display_name", self.display_name)
    

