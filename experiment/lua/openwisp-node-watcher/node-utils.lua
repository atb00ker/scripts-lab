DeviceConfig = {
    general = {},
    interfaces = {},
    resources = {}
}

General = {
    local_time = -1,
    uptime = -1
}

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

Resources = {
  loadavg = {-1 , -1, -1}
}

function split(str, delim)
    local t = {}

    for substr in string.gmatch(str, "[^" .. delim .. "]*") do
        if substr ~= nil and string.len(substr) > 0 then
            table.insert(t, substr)
        end
    end

    return t
end
