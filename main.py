import fastapi as _fastapi
import blockchain as _blockchain

blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()

# endpoint to mine a block
@app.post("/mine_block/")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid.")
    block = blockchain.mine_block(data=data)

    return block

# endpoint to return the entire blockchain
@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid.")
    chain = blockchain.chain
    return chain

# endpoint to see if the blockchain is valid 
@app.get("/validate/")
def is_blockchain_valid():
    return blockchain.is_chain_valid()

# endpoint returns the previous block
@app.get("/previous_block")
def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid.")
    return blockchain.get_previous_block()