from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """A black hole is one of the most fascinating and extreme objects in the universe. It is a 
region in space where gravity is so strong that nothing—not even light—can escape its pull. This 
happens because a very large amount of mass is concentrated in an extremely small region, creating 
a gravitational field of immense strength. The boundary around a black hole, beyond which nothing 
can return, is called the event horizon. Anything that crosses this boundary is inevitably pulled 
inward and cannot escape.

Black holes are usually formed when massive stars reach the end of their life cycle and undergo 
a supernova explosion. After the explosion, the remaining core can collapse under its own gravity 
to a point of nearly infinite density known as a singularity. The singularity is surrounded by the
event horizon, which acts as the "surface" of the black hole, though in reality it is not a 
physical surface but rather a point of no return. Depending on their size, black holes are 
categorized into different types: stellar black holes (formed from collapsing stars, a few times 
more massive than the Sun), supermassive black holes (millions to billions of times more massive 
than the Sun and found at the centers of galaxies), and intermediate black holes (sizes between 
stellar and supermassive). There is also a hypothetical type called primordial black holes, 
which may have formed in the very early universe."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
)

result = splitter.split_text(text)

print(len(result))
print(result)