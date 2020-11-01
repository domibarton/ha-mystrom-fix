from homeassistant.components.mystrom.binary_sensor import MyStromView


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    hass.http.register_view(MyStromFixView(async_add_entities))
    return True


class MyStromFixView(MyStromView):
    url           = "/api/mystrom-fix"
    name          = "api:mystrom-fix"
    requires_auth = False
