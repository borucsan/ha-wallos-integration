# Wallos Home Assistant Integration

A custom Home Assistant integration for [Wallos](https://wallosapp.com/).

## Disclaimer

This project is currently being developed primarily as a learning project.

It is experimental, still evolving, and may be incomplete or unstable. For now, it should be treated as a personal test project rather than a production-ready integration.

## Current Goals

- Connect Home Assistant to a Wallos instance
- Configure the integration through the Home Assistant UI
- Expose selected Wallos data as Home Assistant sensors

## Installation

1. Copy the `custom_components/wallos` folder into your Home Assistant configuration directory:
   `/config/custom_components/wallos`
2. Restart Home Assistant.
3. Open `Settings` -> `Devices & Services`.
4. Click `Add Integration`.
5. Search for `Wallos`.

## Configuration

During setup, you will be asked for:

- `URL`
- `API key`

If you are running Wallos as a Home Assistant add-on, the URL may look like:

`http://d4932a7c-wallos:8282`

## Development Status

At this stage, the integration is intended for experimentation and learning. Features, entity model, and configuration flow may still change as the project develops.

## License

This repository is licensed under the terms of the `LICENSE` file included in this project.
