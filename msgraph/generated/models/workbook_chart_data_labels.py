from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

from .entity import Entity

@dataclass
class WorkbookChartDataLabels(Entity):
    # Represents the format of chart data labels, which includes fill and font formatting. Read-only.
    format: Optional[WorkbookChartDataLabelFormat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # DataLabelPosition value that represents the position of the data label. The possible values are: None, Center, InsideEnd, InsideBase, OutsideEnd, Left, Right, Top, Bottom, BestFit, Callout.
    position: Optional[str] = None
    # String representing the separator used for the data labels on a chart.
    separator: Optional[str] = None
    # Boolean value representing if the data label bubble size is visible or not.
    show_bubble_size: Optional[bool] = None
    # Boolean value representing if the data label category name is visible or not.
    show_category_name: Optional[bool] = None
    # Boolean value representing if the data label legend key is visible or not.
    show_legend_key: Optional[bool] = None
    # Boolean value representing if the data label percentage is visible or not.
    show_percentage: Optional[bool] = None
    # Boolean value representing if the data label series name is visible or not.
    show_series_name: Optional[bool] = None
    # Boolean value representing if the data label value is visible or not.
    show_value: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartDataLabels:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartDataLabels
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookChartDataLabels()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

        from .entity import Entity
        from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(WorkbookChartDataLabelFormat)),
            "position": lambda n : setattr(self, 'position', n.get_str_value()),
            "separator": lambda n : setattr(self, 'separator', n.get_str_value()),
            "show_bubble_size": lambda n : setattr(self, 'show_bubble_size', n.get_bool_value()),
            "show_category_name": lambda n : setattr(self, 'show_category_name', n.get_bool_value()),
            "show_legend_key": lambda n : setattr(self, 'show_legend_key', n.get_bool_value()),
            "show_percentage": lambda n : setattr(self, 'show_percentage', n.get_bool_value()),
            "show_series_name": lambda n : setattr(self, 'show_series_name', n.get_bool_value()),
            "show_value": lambda n : setattr(self, 'show_value', n.get_bool_value()),
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
        writer.write_object_value("format", self.format)
        writer.write_str_value("position", self.position)
        writer.write_str_value("separator", self.separator)
        writer.write_bool_value("show_bubble_size", self.show_bubble_size)
        writer.write_bool_value("show_category_name", self.show_category_name)
        writer.write_bool_value("show_legend_key", self.show_legend_key)
        writer.write_bool_value("show_percentage", self.show_percentage)
        writer.write_bool_value("show_series_name", self.show_series_name)
        writer.write_bool_value("show_value", self.show_value)
    

