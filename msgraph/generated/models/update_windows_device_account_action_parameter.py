from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_device_account import WindowsDeviceAccount

@dataclass
class UpdateWindowsDeviceAccountActionParameter(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Not yet documented
    calendar_sync_enabled: Optional[bool] = None
    # Not yet documented
    device_account: Optional[WindowsDeviceAccount] = None
    # Not yet documented
    device_account_email: Optional[str] = None
    # Not yet documented
    exchange_server: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Not yet documented
    password_rotation_enabled: Optional[bool] = None
    # Not yet documented
    session_initiation_protocal_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateWindowsDeviceAccountActionParameter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateWindowsDeviceAccountActionParameter
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdateWindowsDeviceAccountActionParameter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_device_account import WindowsDeviceAccount

        from .windows_device_account import WindowsDeviceAccount

        fields: Dict[str, Callable[[Any], None]] = {
            "calendar_sync_enabled": lambda n : setattr(self, 'calendar_sync_enabled', n.get_bool_value()),
            "device_account": lambda n : setattr(self, 'device_account', n.get_object_value(WindowsDeviceAccount)),
            "device_account_email": lambda n : setattr(self, 'device_account_email', n.get_str_value()),
            "exchange_server": lambda n : setattr(self, 'exchange_server', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "password_rotation_enabled": lambda n : setattr(self, 'password_rotation_enabled', n.get_bool_value()),
            "session_initiation_protocal_address": lambda n : setattr(self, 'session_initiation_protocal_address', n.get_str_value()),
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
        writer.write_bool_value("calendar_sync_enabled", self.calendar_sync_enabled)
        writer.write_object_value("device_account", self.device_account)
        writer.write_str_value("device_account_email", self.device_account_email)
        writer.write_str_value("exchange_server", self.exchange_server)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("password_rotation_enabled", self.password_rotation_enabled)
        writer.write_str_value("session_initiation_protocal_address", self.session_initiation_protocal_address)
        writer.write_additional_data_value(self.additional_data)
    

