from PIL import Image

def main(): 
    img = Image.open("binaryImageInput.png")  
    print (img.mode) 
  
if __name__ == "__main__": 
    main()
