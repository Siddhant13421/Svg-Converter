import os
import cairosvg # type: ignore

def convert_svg_to_png(input_folder, output_folder, width=84, height=84):
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all SVG files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".svg"):
            # Create full file paths
            svg_file = os.path.join(input_folder, filename)
            png_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")
            
            # Convert SVG to PNG with specified size
            with open(svg_file, 'rb') as svg:
                cairosvg.svg2png(file_obj=svg, write_to=png_file, output_width=width, output_height=height)
                
            print(f"Converted: {svg_file} -> {png_file}")

# Example usage
input_folder = "PATH/Input_Folder"
output_folder = "PATH/Output_Folder"

convert_svg_to_png(input_folder, output_folder, width=84, height=84)
