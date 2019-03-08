--[[
  Save dummy data in lua tables and 
  Output that data in JSON Format.

  Output of this script:
  {
    "type": "DeviceMonitoring",
    "general": ,
    "interfaces": [{
      "name": "wlo1,
      "uptime": 0,
      "statistics": {
        "collisions": 0,
        "rx_frame_errors": 0
        }
      }, {
        "name": "lo1,
        "uptime": 10,
        "statistics": {
          "collisions": 20,
          "rx_frame_errors": 30
      }
    }],
    "resources": 
  }
]]
-- if PRODUCTION is true, extra spaces in output are removed.
PRODUCTION = false

DeviceConfig = {
  general = {},
  interfaces = {},
  resources = {}
}

Interface = {
  name = "NoName",
  uptime = -1,
  statistics = {
    collisions = -1,
    rx_frame_errors = -1
  }
}

function Interface:new(name, uptime, collisions, rx_frame_errors)
  setmetatable({}, Interface)
  self.name = name
  self.uptime = uptime
  self.statistics.collisions = collisions
  self.statistics.rx_frame_errors = rx_frame_errors
  return self
end

interfaceString =
  [[{
    "name": "%s,
    "uptime": %d,
    "statistics": {
      "collisions": %d,
      "rx_frame_errors": %d
    }
}]]

DeviceString = [[{
    "type": "DeviceMonitoring",
    "general": %s,
    "interfaces": %s,
    "resources": %s
}]]

function Interface:toString()
  local interface =
    string.format(interfaceString, self.name, self.uptime, self.statistics.collisions, self.statistics.rx_frame_errors)
  if PRODUCTION then
    interface, _ = string.gsub(interface, " ", "")
    interface, _ = string.gsub(interface, "\n", "")
  end
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

local int1 = Interface:new("wlo1", 0, 0, 0):toString()
table.insert(DeviceConfig["interfaces"], int1)
local int2 = Interface:new("lo1", 10, 20, 30):toString()
table.insert(DeviceConfig["interfaces"], int2)

print(DeviceConfig:toString())
