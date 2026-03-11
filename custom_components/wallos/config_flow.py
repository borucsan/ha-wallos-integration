import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN


class WallosConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):

        if user_input is not None:

            return self.async_create_entry(
                title="Wallos",
                data=user_input,
            )

        schema = vol.Schema({
            vol.Required("url"): str,
            vol.Required("api_key"): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            description_placeholders={
                "url_hint": "For Wallos add-on from https://github.com/borucsan/ha-addons use: http://63015830_wallos:80"
            },
        )