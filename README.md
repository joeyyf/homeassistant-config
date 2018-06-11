# Home Assistant
[Home Assistant](https://home-assistant.io) configuration

I am a total newcomer when it comes to home automation and home assistant, but I am loving the journey so far.
So here is my hardware being used

# Devices

## Outlets / Switches

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [TP-Link Smart Plug HS100](https://amzn.to/2L5Bt9r) | 1 | Wi-Fi | [TP-Link Switch](https://www.home-assistant.io/components/switch.tplink/) | Smart outlet used to control power to cat fountain |

These things are a bit pricey for my taste, but simply brilliant - super easy to set up and use straight out of the box. Loving it

## Lighting

Waiting on a big sale for the [Philips Hue Starter Set](https://amzn.to/2xFtA89) to get things going, as lighting automation is the next big thing, I want to try.

## Climate

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Raspberry Pi Zero W](https://amzn.to/2LYAMiA) | 1 | Wi-Fi | [Raspberry Pi GPIO Binary Sensor](https://www.home-assistant.io/components/binary_sensor.rpi_gpio/) | Temperature, humidity etc. for living room |

Using a [DHT 22/AM2302](https://amzn.to/2sIvrTM) temperature and humidity sensor and planning to get one of these into every room.

## Media

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Samsung UE48J6250](https://amzn.to/2LnRSFK) | 1 | Wi-Fi | [Samsung Smart TV](https://www.home-assistant.io/components/media_player.samsungtv/) | Not so smart smart tv, but it gets the job done |

Having trouble to implement my samsung tv in Hass, but the activity sensor works - so there is that. Still on my todo list though ...

## Voice Assistant

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Amazon Echo Dot](https://amzn.to/2wSreSW) | 6 | Wi-Fi | [Emulated Hue Bridge](https://www.home-assistant.io/components/emulated_hue/) | Planned via Emulated Hue Bridge - native integration for now |

Has nothing to do with Home Assistant for now. I planned to use TTS with my Echo, when there is something available, but for now, I just use the native integration for my smart plug, music streaming and so on.

## Other Hardware

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Synology DS216J](https://amzn.to/2J9SdyY) | 1 | Ethernet | [SynologyDSM Sensor](https://www.home-assistant.io/components/sensor.synologydsm/)| Main storage array |
| [Raspberry Pi 3 b](https://amzn.to/2J9SdyY) | 1 | Ethernet | [Pi-Hole Sensor](https://www.home-assistant.io/components/sensor.pi_hole/), [RESTful Sensor](https://www.home-assistant.io/components/sensor.rest/) | Mainly for pihole, small docker projects etc. |

# Interface

TODO