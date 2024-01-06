
import sys
from typing import Tuple, Generator
from PIL import Image, ImageDraw, ImageFont

# Defaults
BACKGROUND_COLOR = (144, 200, 255)
LETTER_BACKGROUND_COLOR = (255, 255, 255)
LETTER_COLOR = (0, 0, 0)

def get_max_height(num_of_chars: int):
    """Calculate the height based on the num of chars given"""
    return ((num_of_chars + 15) // 16) * 16

def get_xy_squares(height: int) -> Generator[Tuple[int, int], None, None]:
    """Yield all the possible positions of a given 16 * 16 x height image"""
    for y in range(0, height // 16):
        for x in range(0, 16):
            yield (x * 16, y * 16)


def draw_char(draw: ImageDraw, character: str, x: int, y: int):
    """Here, we are expecting the argument of x and y to be corrected already, and is the top left corner of a square
    """
    if len(character) != 1:
        sys.exit()
    drawX = x - 1
    drawY = y + 1

    rectangle = (x, drawY, x + 4, drawY + 11)
    
    draw.rectangle(rectangle, fill=LETTER_BACKGROUND_COLOR)
    draw.text((drawX, drawY), character, font=font, fill=LETTER_COLOR)



if __name__ == "__main__":
    # Load TTF file
    if len(sys.argv) < 4:
        print("Not enough arguments!")
        print("Usage: main <path/to/.ttf> <font_size:10> characters....")
        sys.exit()
    font_path = sys.argv[1]
    font_size = int(sys.argv[2])
    font = ImageFont.truetype(font_path, font_size)

    characters = "".join(sys.argv[3:]).replace(" ", "")
    print(f"Parsing: {characters}")

    max_width = 16 # in 16x16 tiles
    height = get_max_height(len(characters))

    # Create an image and draw object
    image = Image.new('RGB', (max_width * 16, height), color=BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)

    # Render character on the image
    for i, position in enumerate(get_xy_squares(height)):
        if i >= len(characters):
            break
        x = position[0]
        y = position[1]
        char = characters[i]
        draw_char(draw, char, x, y)

    # Save the image
    image.save('output.png')
