function General:toString()
    local generalObjectFormat = [[
    {
        "local_time": %d,
        "uptime": %d
    }]]
    local general = string.format(generalObjectFormat, self.local_time, self.uptime)
    return general
end

function Interface:toString()
    local interfaceObjectString =
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
    local interface =
        string.format(
        interfaceObjectString,
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
    local deviceObjectString =
        [[
    {
        "type": "DeviceMonitoring",
        "general": %s,
        "interfaces": %s,
        "resources": "%s"
    }]]
    local deviceInterfaces = "[" .. table.concat(DeviceConfig.interfaces, ", ") .. "]"
    local deviceGeneral = table.concat(DeviceConfig.general, ", ")
    local deviceResources = table.concat(DeviceConfig.resources, ", ")
    deviceConfig = string.format(deviceObjectString, deviceGeneral, deviceInterfaces, deviceResources)
    if PRODUCTION then
        deviceConfig, _ = string.gsub(deviceConfig, " ", "")
        deviceConfig, _ = string.gsub(deviceConfig, "\n", "")
    end
    return deviceConfig
end
