from Alchemy import initAPIPrivateKey, getSentiment

if __name__ == "__main__":
    initAPIPrivateKey("93bd111c6394f5a24dad62e1854eeb4dd2cde80d")
    t = raw_input("Enter some text('quit' to quit): ")
    while t != "quit":
        r = getSentiment(t)
        print r
        t = raw_input("Enter some text('quit' to quit): ")

