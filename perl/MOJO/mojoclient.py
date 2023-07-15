import asyncio
import websockets

async def send_message():
    async with websockets.connect('ws://localhost:3000/echo') as websocket:
        await websocket.send('Hello, server!')
        response = await websocket.recv()
        print(f'Received: {response}')

asyncio.get_event_loop().run_until_complete(send_message())

