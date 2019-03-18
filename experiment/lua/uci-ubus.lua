--[[
  Collect Interface object on a device
{
    "type": "DeviceMonitoring",
    "general": ,
    "interfaces": [{
    "name": "lo",
    "uptime": 4295,
    "statistics": {
      "collisions": 0,
      "rx_frame_errors": 0,
      "tx_compressed": 0,
      "multicast": 0,
      "rx_length_errors": 0,
      "tx_dropped": 0,
      "rx_bytes": 5732,
      "rx_missed_errors": 0,
      "tx_errors": 0,
      "rx_compressed": 0,
      "rx_over_errors": 0,
      "tx_fifo_errors": 0,
      "rx_crc_errors": 0,
      "rx_packets": 56,
      "tx_heartbeat_errors": 0,
      "rx_dropped": 0,
      "tx_aborted_errors": 0,
      "tx_packets": 56,
      "rx_errors": 0,
      "tx_bytes": 5732,
      "tx_window_errors": 0,
      "rx_fifo_errors": 0,
      "tx_carrier_errors": 0
    }
}],
    "resources": 
}
]]
uci = require("uci")
json = require("json")

x = uci.cursor()

DeviceConfig = {
    general = {},
    interfaces = {},
    resources = {}
}

DeviceString = [[{
    "type": "DeviceMonitoring",
    "general": %s,
    "interfaces": %s,
    "resources": %s
}]]

Interface = {
    name = "DEFAULT",
    uptime = -1,
    statistics = {
        collisions = -1,
        rx_frame_errors = -1,
        tx_compressed = -1,
        multicast = -1,
        rx_length_errors = -1,
        tx_dropped = -1,
        rx_bytes = -1,
        rx_missed_errors = -1,
        tx_errors = -1,
        rx_compressed = -1,
        rx_over_errors = -1,
        tx_fifo_errors = -1,
        rx_crc_errors = -1,
        rx_packets = -1,
        tx_heartbeat_errors = -1,
        rx_dropped = -1,
        tx_aborted_errors = -1,
        tx_packets = -1,
        rx_errors = -1,
        tx_bytes = -1,
        tx_window_errors = -1,
        rx_fifo_errors = -1,
        tx_carrier_errors = -1
    }
}

interfaceString =
    [[{
    "name": "%s",
    "uptime": %d,
    "statistics": {
      "collisions": %d,
      "rx_frame_errors": %d,
      "tx_compressed": %d,
      "multicast": %d,
      "rx_length_errors": %d,
      "tx_dropped": %d,
      "rx_bytes": %d,
      "rx_missed_errors": %d,
      "tx_errors": %d,
      "rx_compressed": %d,
      "rx_over_errors": %d,
      "tx_fifo_errors": %d,
      "rx_crc_errors": %d,
      "rx_packets": %d,
      "tx_heartbeat_errors": %d,
      "rx_dropped": %d,
      "tx_aborted_errors": %d,
      "tx_packets": %d,
      "rx_errors": %d,
      "tx_bytes": %d,
      "tx_window_errors": %d,
      "rx_fifo_errors": %d,
      "tx_carrier_errors": %d
    }
}]]

function Interface:new(
    name,
    uptime,
    collisions,
    rx_frame_errors,
    tx_compressed,
    multicast,
    rx_length_errors,
    tx_dropped,
    rx_bytes,
    rx_missed_errors,
    tx_errors,
    rx_compressed,
    rx_over_errors,
    tx_fifo_errors,
    rx_crc_errors,
    rx_packets,
    tx_heartbeat_errors,
    rx_dropped,
    tx_aborted_errors,
    tx_packets,
    rx_errors,
    tx_bytes,
    tx_window_errors,
    rx_fifo_errors,
    tx_carrier_errors)
    setmetatable({}, Interface)

    self.name = name
    self.uptime = uptime or -1
    self.statistics.collisions = collisions or -1
    self.statistics.rx_frame_errors = rx_frame_errors or -1
    self.statistics.tx_compressed = tx_compressed or -1
    self.statistics.multicast = multicast or -1
    self.statistics.rx_length_errors = rx_length_errors or -1
    self.statistics.tx_dropped = tx_dropped or -1
    self.statistics.rx_bytes = rx_bytes or -1
    self.statistics.rx_missed_errors = rx_missed_errors or -1
    self.statistics.tx_errors = tx_errors or -1
    self.statistics.rx_compressed = rx_compressed or -1
    self.statistics.rx_over_errors = rx_over_errors or -1
    self.statistics.tx_fifo_errors = tx_fifo_errors or -1
    self.statistics.rx_crc_errors = rx_crc_errors or -1
    self.statistics.rx_packets = rx_packets or -1
    self.statistics.tx_heartbeat_errors = tx_heartbeat_errors or -1
    self.statistics.rx_dropped = rx_dropped or -1
    self.statistics.tx_aborted_errors = tx_aborted_errors or -1
    self.statistics.tx_packets = tx_packets or -1
    self.statistics.rx_errors = rx_errors or -1
    self.statistics.tx_bytes = tx_bytes or -1
    self.statistics.tx_window_errors = tx_window_errors or -1
    self.statistics.rx_fifo_errors = rx_fifo_errors or -1
    self.statistics.tx_carrier_errors = tx_carrier_errors or -1
    return self
end

function Interface:toString()
    local interface =
        string.format(
        interfaceString,
        self.name,
        self.uptime,
        self.statistics.collisions,
        self.statistics.rx_frame_errors,
        self.statistics.tx_compressed,
        self.statistics.multicast,
        self.statistics.rx_length_errors,
        self.statistics.tx_dropped,
        self.statistics.rx_bytes,
        self.statistics.rx_missed_errors,
        self.statistics.tx_errors,
        self.statistics.rx_compressed,
        self.statistics.rx_over_errors,
        self.statistics.tx_fifo_errors,
        self.statistics.rx_crc_errors,
        self.statistics.rx_packets,
        self.statistics.tx_heartbeat_errors,
        self.statistics.rx_dropped,
        self.statistics.tx_aborted_errors,
        self.statistics.tx_packets,
        self.statistics.rx_errors,
        self.statistics.tx_bytes,
        self.statistics.tx_window_errors,
        self.statistics.rx_fifo_errors,
        self.statistics.tx_carrier_errors
    )
    return interface
end

function DeviceConfig:toString()
    local deviceInterfaces = "[" .. table.concat(DeviceConfig.interfaces, ", ") .. "]"
    local deviceGeneral = table.concat(DeviceConfig.general, ", ")
    local deviceResources = table.concat(DeviceConfig.resources, ", ")
    deviceConfig = string.format(DeviceString, deviceGeneral, deviceInterfaces, deviceResources)
    if PRODUCTION then
        deviceConfig, _ = string.gsub(deviceConfig, " ", "")
        deviceConfig, _ = string.gsub(deviceConfig, "\n", "")
    end
    return deviceConfig
end

-- cat /sys/class/net/lo/statistics/collisions
function get_sys_statistics(ifname, fname)
    local path = string.format("/sys/class/net/%s/statistics/%s", ifname, fname)
    local file = io.open(path, "r")
    if file ~= nil then
        content = file:read("*l")
        io.close(file)
        return content
    else
        return -1
    end
end
function get_ifstatus(name)
    command = string.format("/sbin/ifstatus %s", name)
    handler = io.popen(command)
    result = handler:read("*a")
    handler:close()
    return json.parse(result)
end

x:foreach(
    "network",
    "interface",
    function(intr)
        ifname = intr["ifname"]
        ifstatus = get_ifstatus(intr[".name"])
        collisions = get_sys_statistics(ifname, "collisions")
        rx_frame_errors = get_sys_statistics(ifname, "rx_frame_errors")
        tx_compressed = get_sys_statistics(ifname, "tx_compressed")
        multicast = get_sys_statistics(ifname, "multicast")
        rx_length_errors = get_sys_statistics(ifname, "rx_length_errors")
        tx_dropped = get_sys_statistics(ifname, "tx_dropped")
        rx_bytes = get_sys_statistics(ifname, "rx_bytes")
        rx_missed_errors = get_sys_statistics(ifname, "rx_missed_errors")
        tx_errors = get_sys_statistics(ifname, "tx_errors")
        rx_compressed = get_sys_statistics(ifname, "rx_compressed")
        rx_over_errors = get_sys_statistics(ifname, "rx_over_errors")
        tx_fifo_errors = get_sys_statistics(ifname, "tx_fifo_errors")
        rx_crc_errors = get_sys_statistics(ifname, "rx_crc_errors")
        rx_packets = get_sys_statistics(ifname, "rx_packets")
        tx_heartbeat_errors = get_sys_statistics(ifname, "tx_heartbeat_errors")
        rx_dropped = get_sys_statistics(ifname, "rx_dropped")
        tx_aborted_errors = get_sys_statistics(ifname, "tx_aborted_errors")
        tx_packets = get_sys_statistics(ifname, "tx_packets")
        rx_errors = get_sys_statistics(ifname, "rx_errors")
        tx_bytes = get_sys_statistics(ifname, "tx_bytes")
        tx_window_errors = get_sys_statistics(ifname, "tx_window_errors")
        rx_fifo_errors = get_sys_statistics(ifname, "rx_fifo_errors")
        tx_carrier_errors = get_sys_statistics(ifname, "tx_carrier_errors")

        nxtInterface =
            Interface:new(
            ifname,
            ifstatus["uptime"],
            collisions,
            rx_frame_errors,
            tx_compressed,
            multicast,
            rx_length_errors,
            tx_dropped,
            rx_bytes,
            rx_missed_errors,
            tx_errors,
            rx_compressed,
            rx_over_errors,
            tx_fifo_errors,
            rx_crc_errors,
            rx_packets,
            tx_heartbeat_errors,
            rx_dropped,
            tx_aborted_errors,
            tx_packets,
            rx_errors,
            tx_bytes,
            tx_window_errors,
            rx_fifo_errors,
            tx_carrier_errors
        ):toString()
        table.insert(DeviceConfig["interfaces"], nxtInterface)
    end
)
print(DeviceConfig:toString())
