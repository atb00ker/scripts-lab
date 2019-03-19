--[[
  Collect Interface object on a device
  Note: Some objects are fetched by UCI.
  uptime is fetched from /proc/uptime
  interface's uptime is fetched from /sbin/ifstatus
  statistics are fetched from /sys/class/net/lo/statistics/

]]
uci = require("uci")
json = require("json")
os = require("os")

require("node-utils")
require("node-string")

ucursor = uci.cursor()

function General:new(local_time, uptime)
    setmetatable({}, General)
    self.local_time = local_time or -1
    self.uptime = uptime or -1
    return self
end

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

-- cat /sys/class/net/lo/statistics/collisions
function get_data_file(path)
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

function get_uptime()
    local file = io.open("/proc/uptime", "r")
    if file ~= nil then
        content = split(file:read(), ".")
        io.close(file)
        return content[1]
    else
        return -1
    end
end

function main()
    -- General
    local_time = os.time()
    uptime = get_uptime()
    objGeneral = General:new(local_time, uptime):toString()
    table.insert(DeviceConfig["general"], objGeneral)
    -- Interface
    ucursor:foreach(
        "network",
        "interface",
        function(intr)
            local ifname = intr["ifname"]
            local ifstatus = get_ifstatus(intr[".name"])
            local path = string.format("/sys/class/net/%s/statistics/", ifname)
            local collisions = get_data_file(path .. "collisions")
            local rx_frame_errors = get_data_file(path .. "rx_frame_errors")
            local tx_compressed = get_data_file(path .. "tx_compressed")
            local multicast = get_data_file(path .. "multicast")
            local rx_length_errors = get_data_file(path .. "rx_length_errors")
            local tx_dropped = get_data_file(path .. "tx_dropped")
            local rx_bytes = get_data_file(path .. "rx_bytes")
            local rx_missed_errors = get_data_file(path .. "rx_missed_errors")
            local tx_errors = get_data_file(path .. "tx_errors")
            local rx_compressed = get_data_file(path .. "rx_compressed")
            local rx_over_errors = get_data_file(path .. "rx_over_errors")
            local tx_fifo_errors = get_data_file(path .. "tx_fifo_errors")
            local rx_crc_errors = get_data_file(path .. "rx_crc_errors")
            local rx_packets = get_data_file(path .. "rx_packets")
            local tx_heartbeat_errors = get_data_file(path .. "tx_heartbeat_errors")
            local rx_dropped = get_data_file(path .. "rx_dropped")
            local tx_aborted_errors = get_data_file(path .. "tx_aborted_errors")
            local tx_packets = get_data_file(path .. "tx_packets")
            local rx_errors = get_data_file(path .. "rx_errors")
            local tx_bytes = get_data_file(path .. "tx_bytes")
            local tx_window_errors = get_data_file(path .. "tx_window_errors")
            local rx_fifo_errors = get_data_file(path .. "rx_fifo_errors")
            local tx_carrier_errors = get_data_file(path .. "tx_carrier_errors")

            objInterface =
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
            table.insert(DeviceConfig["interfaces"], objInterface)
        end
    )
    print(DeviceConfig:toString())
end

main()
