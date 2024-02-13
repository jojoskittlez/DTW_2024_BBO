import asyncio

from asyncua import Client

url = "opc.tcp://localhost:4840/freeopcua/server/"
namespace = "OPCUA_S7_DTW"


async def main():

    print(f"Connecting to {url} ...")
    async with Client(url=url) as client:
        # Find the namespace index
        nsidx = await client.get_namespace_index(namespace)
        print(f"Namespace Index for '{namespace}': {nsidx}")

        # Get the variable node for read / write

        # idfk man we probably shoud iterate over all the data thingies we get and have the added here automatically
        # no idea how tho
        # pls help
        # i'm suffering
        var = await client.nodes.root.get_child(
            f"0:st_vision_data/{nsidx}:stVisionData/{nsidx}:sVisionStatus"
        )
        value = await var.read_value()
        print(f"Value of MyVariable ({var}): {value}")

        #new_value = value - 50
        #print(f"Setting value of MyVariable to {new_value} ...")
        #await var.write_value(new_value)

        # Calling a method
        #res = await client.nodes.objects.call_method(f"{nsidx}:ServerMethod", 5)
        #print(f"Calling ServerMethod returned {res}")


if __name__ == "__main__":
    asyncio.run(main())