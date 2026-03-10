from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN


class WallosEntity(CoordinatorEntity):

    _attr_has_entity_name = True

    def __init__(self, coordinator):
        super().__init__(coordinator)

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, "wallos")},
            name="Wallos",
            manufacturer="Wallos",
        )