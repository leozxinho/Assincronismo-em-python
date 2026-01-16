import asyncio


# Exemplo prático de sincronismo e assincronismo

async def say_hello(name):
    print(f"{name} is starting...")
    await asyncio.sleep(2)
    print(f"{name} says hello")
    
    
async def main():
    # await say_hello("Olá") # Sincrono
    await asyncio.gather( # Assincrono
        say_hello("Leonardo"),
        say_hello("Oliveira")
    )
    
    

asyncio.run(main())
