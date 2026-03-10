from datetime import timedelta

from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import DEFAULT_SCAN_INTERVAL
_LOGGER = logging.getLogger(__name__)


_LOGGER.debug("[wallos] Module loaded")


class WallosCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, api):

        super().__init__(
            hass,
            logger=hass.logger,
            name="wallos",
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )

        self.api = api
        _LOGGER.debug(
            "[wallos] Coordinator initialized update_interval=%s",
            self.update_interval,
        )

    async def _async_update_data(self):

        try:
            return await self.api.get_subscriptions()

        except Exception as err:
            raise UpdateFailed(err) from err