from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .simulation_automation_run_status import SimulationAutomationRunStatus

from .entity import Entity

@dataclass
class SimulationAutomationRun(Entity):
    # Date and time when the run ends in an attack simulation automation.
    end_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier for the attack simulation campaign initiated in the attack simulation automation run.
    simulation_id: Optional[str] = None
    # Date and time when the run starts in an attack simulation automation.
    start_date_time: Optional[datetime.datetime] = None
    # Status of the attack simulation automation run. The possible values are: unknown, running, succeeded, failed, skipped, unknownFutureValue.
    status: Optional[SimulationAutomationRunStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SimulationAutomationRun:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SimulationAutomationRun
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SimulationAutomationRun()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .simulation_automation_run_status import SimulationAutomationRunStatus

        from .entity import Entity
        from .simulation_automation_run_status import SimulationAutomationRunStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "simulation_id": lambda n : setattr(self, 'simulation_id', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SimulationAutomationRunStatus)),
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
        writer.write_datetime_value("end_date_time", self.end_date_time)
        writer.write_str_value("simulation_id", self.simulation_id)
        writer.write_datetime_value("start_date_time", self.start_date_time)
        writer.write_enum_value("status", self.status)
    

