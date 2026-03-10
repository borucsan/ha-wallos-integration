from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import WallosCoordinator
from .wallos_api import WallosAPI

PLATFORMS = ["sensor", "calendar"]

_LOGGER = logging.getLogger(__name__)

_LOGGER.debug("[wallos] Module loaded")


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):

    api = WallosAPI(
        entry.data["url"],
        entry.data["api_key"],
    )

    coordinator = WallosCoordinator(hass, api)

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True