# Generated by Django 3.2.9 on 2022-02-18 13:31

from django.db import migrations, models
import simo.core.utils.helpers
import simo.core.utils.mixins
import simo_esphome.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_create_generic'),
    ]

    operations = [
        migrations.CreateModel(
            name='ESPDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=40, unique=True)),
                ('api_secret', models.CharField(default=simo.core.utils.helpers.get_random_string, editable=False, help_text='Used for communications encryption and as hotspot password in fallback mode when device is unable to connect to your WiFi.', max_length=100)),
                ('platform', models.CharField(choices=[('esp32', 'ESP32'), ('esp8266', 'ESP8266')], default='esp32', max_length=50)),
                ('board', models.CharField(choices=[('alksesp32', 'alksesp32'), ('az-delivery-devkit-v4', 'az-delivery-devkit-v4'), ('bpi-bit', 'bpi-bit'), ('briki_abc_esp32', 'briki_abc_esp32'), ('briki_mbc-wb_esp32', 'briki_mbc-wb_esp32'), ('d-duino-32', 'd-duino-32'), ('esp-wrover-kit', 'esp-wrover-kit'), ('esp32-devkitlipo', 'esp32-devkitlipo'), ('esp32-evb', 'esp32-evb'), ('esp32-gateway', 'esp32-gateway'), ('esp32-poe-iso', 'esp32-poe-iso'), ('esp32-poe', 'esp32-poe'), ('esp32-pro', 'esp32-pro'), ('esp320', 'esp320'), ('esp32cam', 'esp32cam'), ('esp32dev', 'esp32dev'), ('esp32doit-devkit-v1', 'esp32doit-devkit-v1'), ('esp32doit-espduino', 'esp32doit-espduino'), ('esp32thing', 'esp32thing'), ('esp32thing_plus', 'esp32thing_plus'), ('esp32vn-iot-uno', 'esp32vn-iot-uno'), ('espea32', 'espea32'), ('espectro32', 'espectro32'), ('espino32', 'espino32'), ('etboard', 'etboard'), ('featheresp32', 'featheresp32'), ('firebeetle32', 'firebeetle32'), ('fm-devkit', 'fm-devkit'), ('frogboard', 'frogboard'), ('healtypi4', 'healtypi4'), ('heltec_wifi_kit_32', 'heltec_wifi_kit_32'), ('heltec_wifi_kit_32_v2', 'heltec_wifi_kit_32_v2'), ('heltec_wifi_lora_32', 'heltec_wifi_lora_32'), ('heltec_wifi_lora_32_V2', 'heltec_wifi_lora_32_V2'), ('heltec_wireless_stick', 'heltec_wireless_stick'), ('heltec_wireless_stick_lite', 'heltec_wireless_stick_lite'), ('honeylemon', 'honeylemon'), ('hornbill32dev', 'hornbill32dev'), ('hornbill32minima', 'hornbill32minima'), ('imbrios-logsens-v1p1', 'imbrios-logsens-v1p1'), ('inex_openkb', 'inex_openkb'), ('intorobot', 'intorobot'), ('iotaap_magnolia', 'iotaap_magnolia'), ('iotbusio', 'iotbusio'), ('iotbusproteus', 'iotbusproteus'), ('kits-edu', 'kits-edu'), ('labplus_mpython', 'labplus_mpython'), ('lolin32', 'lolin32'), ('lolin32_lite', 'lolin32_lite'), ('lolin_d32', 'lolin_d32'), ('lolin_d32_pro', 'lolin_d32_pro'), ('lopy', 'lopy'), ('lopy4', 'lopy4'), ('m5stack-atom', 'm5stack-atom'), ('m5stack-core-esp32', 'm5stack-core-esp32'), ('m5stack-core2', 'm5stack-core2'), ('m5stack-coreink', 'm5stack-coreink'), ('m5stack-fire', 'm5stack-fire'), ('m5stack-grey', 'm5stack-grey'), ('m5stack-timer-cam', 'm5stack-timer-cam'), ('m5stick-c', 'm5stick-c'), ('magicbit', 'magicbit'), ('mgbot-iotik32a', 'mgbot-iotik32a'), ('mgbot-iotik32b', 'mgbot-iotik32b'), ('mhetesp32devkit', 'mhetesp32devkit'), ('mhetesp32minikit', 'mhetesp32minikit'), ('microduino-core-esp32', 'microduino-core-esp32'), ('nano32', 'nano32'), ('nina_w10', 'nina_w10'), ('node32s', 'node32s'), ('nodemcu-32s', 'nodemcu-32s'), ('nscreen-32', 'nscreen-32'), ('odroid_esp32', 'odroid_esp32'), ('onehorse32dev', 'onehorse32dev'), ('oroca_edubot', 'oroca_edubot'), ('pico32', 'pico32'), ('piranha_esp32', 'piranha_esp32'), ('pocket_32', 'pocket_32'), ('pycom_gpy', 'pycom_gpy'), ('qchip', 'qchip'), ('quantum', 'quantum'), ('s_odi_ultra', 's_odi_ultra'), ('sensesiot_weizen', 'sensesiot_weizen'), ('sg-o_airMon', 'sg-o_airMon'), ('sparkfun_lora_gateway_1-channel', 'sparkfun_lora_gateway_1-channel'), ('tinypico', 'tinypico'), ('ttgo-lora32-v1', 'ttgo-lora32-v1'), ('ttgo-lora32-v2', 'ttgo-lora32-v2'), ('ttgo-lora32-v21', 'ttgo-lora32-v21'), ('ttgo-t-beam', 'ttgo-t-beam'), ('ttgo-t-watch', 'ttgo-t-watch'), ('ttgo-t1', 'ttgo-t1'), ('ttgo-t7-v13-mini32', 'ttgo-t7-v13-mini32'), ('ttgo-t7-v14-mini32', 'ttgo-t7-v14-mini32'), ('turta_iot_node', 'turta_iot_node'), ('vintlabs-devkit-v1', 'vintlabs-devkit-v1'), ('wemos_d1_mini32', 'wemos_d1_mini32'), ('wemosbat', 'wemosbat'), ('wesp32', 'wesp32'), ('widora-air', 'widora-air'), ('wifiduino32', 'wifiduino32'), ('xinabox_cw02', 'xinabox_cw02'), ('d1', 'd1'), ('d1_mini', 'd1_mini'), ('d1_mini_lite', 'd1_mini_lite'), ('d1_mini_pro', 'd1_mini_pro'), ('esp01', 'esp01'), ('esp01_1m', 'esp01_1m'), ('esp07', 'esp07'), ('esp12e', 'esp12e'), ('esp210', 'esp210'), ('esp8285', 'esp8285'), ('esp_wroom_02', 'esp_wroom_02'), ('espduino', 'espduino'), ('espectro', 'espectro'), ('espino', 'espino'), ('espinotee', 'espinotee'), ('espmxdevkit', 'espmxdevkit'), ('espresso_lite_v1', 'espresso_lite_v1'), ('espresso_lite_v2', 'espresso_lite_v2'), ('gen4iod', 'gen4iod'), ('heltec_wifi_kit_8', 'heltec_wifi_kit_8'), ('huzzah', 'huzzah'), ('inventone', 'inventone'), ('modwifi', 'modwifi'), ('nodemcu', 'nodemcu'), ('nodemcuv2', 'nodemcuv2'), ('oak', 'oak'), ('phoenix_v1', 'phoenix_v1'), ('phoenix_v2', 'phoenix_v2'), ('sonoff_basic', 'sonoff_basic'), ('sonoff_s20', 'sonoff_s20'), ('sonoff_sv', 'sonoff_sv'), ('sonoff_th', 'sonoff_th'), ('sparkfunBlynk', 'sparkfunBlynk'), ('thing', 'thing'), ('thingdev', 'thingdev'), ('wifi_slot', 'wifi_slot'), ('wifiduino', 'wifiduino'), ('wifinfo', 'wifinfo'), ('wio_link', 'wio_link'), ('wio_node', 'wio_node'), ('xinabox_cw01', 'xinabox_cw01')], default='esp32dev', help_text='* Use platform:ESP8266 board:esp01_1m for Sonoff devices.', max_length=100)),
                ('wifi_ssid', models.CharField(default=simo_esphome.utils.get_last_wifi_ssid, max_length=100)),
                ('wifi_password', models.CharField(default=simo_esphome.utils.get_last_wifi_password, max_length=100)),
                ('dallas_hub', models.PositiveIntegerField(blank=True, null=True, verbose_name='Enable dallas hub')),
                ('additional_yaml', models.TextField(blank=True, null=True)),
                ('connected', models.BooleanField(db_index=True, default=False, verbose_name='WiFi connection')),
                ('signal_strength', models.PositiveIntegerField(editable=False, help_text='Signal strength in %', null=True)),
                ('installed_version', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('compiled_version', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('compiling', models.BooleanField(default=False, editable=False)),
                ('firmware_status', models.CharField(choices=[('up_to_date', 'Up to date'), ('out_of_date', 'Out of date!'), ('compiling', 'Compiling...'), ('needs_update', 'Needs update!'), ('updating', 'Updating...')], db_index=True, default='compiling', max_length=50, verbose_name='firmware')),
                ('occupied_pins', models.JSONField(blank=True, default=dict)),
                ('last_compile', models.DateTimeField(blank=True, editable=False, null=True)),
                ('components', models.ManyToManyField(editable=False, to='core.Component')),
            ],
            options={
                'verbose_name': 'ESP Device',
                'verbose_name_plural': 'ESP Devices',
            },
            bases=(models.Model, simo.core.utils.mixins.SimoAdminMixin),
        ),
    ]
