def classFactory(iface):
    from .plugin import DigitalTwinPlugin
    return DigitalTwinPlugin(iface)
