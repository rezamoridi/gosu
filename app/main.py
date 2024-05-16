import uvicorn


if __name__ == "__main__":
    print("Running ...")
    uvicorn.run("config:app", reload=True, host="0.0.0.0", port=8000)



