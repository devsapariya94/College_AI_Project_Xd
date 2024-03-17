import engineFunctions
user_api_input="what is pthotosynthesis give answer in short?"
node_0 = engineFunctions.scrapper_youtube(link='https://www.youtube.com/watch?v=jnoVtCKECmQ&ab_channel=NickWhit')
print(node_0)
node_1 = engineFunctions.chat_with_index(index = node_0, query='what is photosynthesis?')
# print(node_1)