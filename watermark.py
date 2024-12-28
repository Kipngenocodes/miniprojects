from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    # Open the original image
    original = Image.open(input_image_path).convert("RGBA")

    # Create a transparent overlay for the watermark
    watermark_overlay = Image.new("RGBA", original.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark_overlay)

    # Choose a font and size
    font = ImageFont.truetype("arial.ttf", 36)  # Ensure the font file is available

    # Calculate text dimensions using textbbox
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Position the watermark in the bottom-right corner
    position = (original.width - text_width - 20, original.height - text_height - 20)

    # Add the watermark text
    draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)

    # Combine original image with the watermark
    watermarked = Image.alpha_composite(original, watermark_overlay)

    # Save the result
    watermarked.convert("RGB").save(output_image_path, "JPEG")

# Example usage
add_watermark("input.jpg", "output.jpg", "© Your Watermark")
