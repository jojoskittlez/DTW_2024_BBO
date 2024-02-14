import asyncio

from asyncua import Client

url = "opc.tcp://192.168.0.100:4334/UA/Simulator"
# namespace = "http://examples.freeopcua.github.io"


async def main():

    print(f"Connecting to {url} ...")
    async with Client(url=url) as client:
        # Find the namespace index
        #nsidx = await client.get_namespace_index(namespace)
        #print(f"Namespace Index for '{namespace}': {nsidx}")

        # Get the variable node for read / write
        #var = await client.nodes.root.get_children()
        #print(var)
        child_var = await client.nodes.objects.get_children(32)
        print(child_var)
        ref_var = await client.nodes.objects.get_references()
        print(ref_var)

        #for i in child_var:
        #    try:
        #        client.nodes.getvalue()
        #    except:
        #        print("idk man")

        #value = await var.read_value()
        #print(f"Value of MyVariable ({var}): {value}")

        #new_value = value - 50
        #print(f"Setting value of MyVariable to {new_value} ...")
        #await var.write_value(new_value)

        # Calling a method
        #res = await client.nodes.objects.call_method(f"{nsidx}:ServerMethod", 5)
        #print(f"Calling ServerMethod returned {res}")


if __name__ == "__main__":
    asyncio.run(main())

# get child - nodeid 