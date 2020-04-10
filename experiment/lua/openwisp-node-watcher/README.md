# Simple RPCD Test for OpenWISP Project


Prerequiste:
- Access to OpenWRT device with Lua installed

Step 1. Setup Lua files: copy all the lua files in this folder to `/usr/share/lua/<file-name>`

Step 2. Setup rpcd to get response for ubus:

- Copy `node` file in the router's `/usr/libexec/rpcd` directory (create directory if it's not present.)
- Make `node` file executable: `chmod +x /usr/libexec/rpcd/node`
- Restart rpcd: `/etc/init.d/rpcd restart`

Note: (luci_app_statistics)[https://openwrt.org/docs/guide-user/luci/luci_app_statistics] **might** be required for resources block.

That's it!

Now you should be able use the following cammands:

1. ubus -v list node
```bash
'node' @d1a46d00
	"rlua":{}
	"hello":{}
```

2. ubus call node rlua
```bash
{
	"type": "DeviceMonitoring",
	"general": {
		"local_time": 1552996253,
		"uptime": 1836
	},
	"interfaces": [
		{
			"name": "lo",
			"uptime": 1829,
			"statistics": {
				"collisions": 0,
				"rx_frame_errors": 0,
				"tx_compressed": 0,
				"multicast": 0,
				"rx_length_errors": 0,
				"tx_dropped": 0,
				"rx_bytes": 1696,
				"rx_missed_errors": 0,
				"tx_errors": 0,
				"rx_compressed": 0,
				"rx_over_errors": 0,
				"tx_fifo_errors": 0,
				"rx_crc_errors": 0,
				"rx_packets": 20,
				"tx_heartbeat_errors": 0,
				"rx_dropped": 0,
				"tx_aborted_errors": 0,
				"tx_packets": 20,
				"rx_errors": 0,
				"tx_bytes": 1696,
				"tx_window_errors": 0,
				"rx_fifo_errors": 0,
				"tx_carrier_errors": 0
			}
		},
		{
			"name": "eth0",
			"uptime": 1829,
			"statistics": {
				"collisions": 0,
				"rx_frame_errors": 0,
				"tx_compressed": 0,
				"multicast": 66,
				"rx_length_errors": 0,
				"tx_dropped": 0,
				"rx_bytes": 360204,
				"rx_missed_errors": 0,
				"tx_errors": 0,
				"rx_compressed": 0,
				"rx_over_errors": 0,
				"tx_fifo_errors": 0,
				"rx_crc_errors": 0,
				"rx_packets": 3343,
				"tx_heartbeat_errors": 0,
				"rx_dropped": 0,
				"tx_aborted_errors": 0,
				"tx_packets": 2122,
				"rx_errors": 0,
				"tx_bytes": 363438,
				"tx_window_errors": 0,
				"rx_fifo_errors": 0,
				"tx_carrier_errors": 0
			}
		},
		{
			"name": "eth1",
			"uptime": 1827,
			"statistics": {
				"collisions": 0,
				"rx_frame_errors": 0,
				"tx_compressed": 0,
				"multicast": 0,
				"rx_length_errors": 0,
				"tx_dropped": 0,
				"rx_bytes": 12642,
				"rx_missed_errors": 0,
				"tx_errors": 0,
				"rx_compressed": 0,
				"rx_over_errors": 0,
				"tx_fifo_errors": 0,
				"rx_crc_errors": 0,
				"rx_packets": 135,
				"tx_heartbeat_errors": 0,
				"rx_dropped": 0,
				"tx_aborted_errors": 0,
				"tx_packets": 168,
				"rx_errors": 0,
				"tx_bytes": 16488,
				"tx_window_errors": 0,
				"rx_fifo_errors": 0,
				"tx_carrier_errors": 0
			}
		},
		{
			"name": "eth1",
			"uptime": -1,
			"statistics": {
				"collisions": 0,
				"rx_frame_errors": 0,
				"tx_compressed": 0,
				"multicast": 0,
				"rx_length_errors": 0,
				"tx_dropped": 0,
				"rx_bytes": 12642,
				"rx_missed_errors": 0,
				"tx_errors": 0,
				"rx_compressed": 0,
				"rx_over_errors": 0,
				"tx_fifo_errors": 0,
				"rx_crc_errors": 0,
				"rx_packets": 135,
				"tx_heartbeat_errors": 0,
				"rx_dropped": 0,
				"tx_aborted_errors": 0,
				"tx_packets": 168,
				"rx_errors": 0,
				"tx_bytes": 16488,
				"tx_window_errors": 0,
				"rx_fifo_errors": 0,
				"tx_carrier_errors": 0
			}
		}
	],
	"resources": ""
}
```
