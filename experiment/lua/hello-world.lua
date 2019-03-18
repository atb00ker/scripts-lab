-- [[ To run it, type: lua hello-world.lua on terminal ]]
print("hello world")

-- Print a table
intr = {
    key1 = 0,
    key2 = 5
}
for key, value in pairs(intr) do
    print(key .. ": " .. tostring(value))
end
