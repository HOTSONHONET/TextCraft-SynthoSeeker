from fastapi import FastAPI, WebSocket


chats_router = FastAPI()


@chats_router.websocket("/ws/{kg_id}")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")