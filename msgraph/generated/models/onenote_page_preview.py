from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import onenote_page_preview_links

class OnenotePagePreview(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value

    def __init__(self,) -> None:
        """
        Instantiates a new onenotePagePreview and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        self.odata_type = "#microsoft.graph.onenotePagePreview"
        # The links property
        self._links: Optional[onenote_page_preview_links.OnenotePagePreviewLinks] = None
        # The previewText property
        self._preview_text: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenotePagePreview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenotePagePreview
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return OnenotePagePreview()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "links": lambda n : setattr(self, 'links', n.get_object_value(onenote_page_preview_links.OnenotePagePreviewLinks)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "preview_text": lambda n : setattr(self, 'preview_text', n.get_str_value()),
        }
        return fields

    @property
    def links(self,) -> Optional[onenote_page_preview_links.OnenotePagePreviewLinks]:
        """
        Gets the links property value. The links property
        Returns: Optional[onenote_page_preview_links.OnenotePagePreviewLinks]
        """
        return self._links

    @links.setter
    def links(self,value: Optional[onenote_page_preview_links.OnenotePagePreviewLinks] = None) -> None:
        """
        Sets the links property value. The links property
        Args:
            value: Value to set for the links property.
        """
        self._links = value

    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type

    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value

    @property
    def preview_text(self,) -> Optional[str]:
        """
        Gets the previewText property value. The previewText property
        Returns: Optional[str]
        """
        return self._preview_text

    @preview_text.setter
    def preview_text(self,value: Optional[str] = None) -> None:
        """
        Sets the previewText property value. The previewText property
        Args:
            value: Value to set for the previewText property.
        """
        self._preview_text = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("links", self.links)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("previewText", self.preview_text)
        writer.write_additional_data_value(self.additional_data)

