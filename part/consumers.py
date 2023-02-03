from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
class MyAsync_Consumer(AsyncConsumer):
    async def webscoket_connect(self,event):        
        print(" webscoket get connected ",event)
        await self.send({
            "type":"websocket.accept"          
        })
    async def webscoket_recive(self,event):
        print("msg is recived",event)
        for i in range(0,5):
            self.send({
                "type": "websocket.send",
                "text":str(i),
            })
    async def webscoket_disconncted(self,event):
        print("get dissconnected")
        raise StopConsumer
        