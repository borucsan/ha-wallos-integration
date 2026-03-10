from homeassistant.components.sensor import SensorEntity

from .entity import WallosEntity
from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = [
        WallosMonthlyCost(coordinator),
    ]

    async_add_entities(entities)


class WallosMonthlyCost(WallosEntity, SensorEntity):

    _attr_name = "Monthly subscription cost"
    _attr_unique_id = "wallos_monthly_cost"

    @property
    def native_value(self):

        total = 0

        for sub in self.coordinator.data:

            if sub["cycle"] == "monthly":
                total += sub["price"]

            elif sub["cycle"] == "yearly":
                total += sub["price"] / 12

        return round(total, 2)