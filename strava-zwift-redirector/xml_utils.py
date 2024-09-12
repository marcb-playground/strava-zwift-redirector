import re

def move_watts_to_power(file_source_path, file_target_path):
    # Read the content from the source file
    with open(file_source_path, 'r') as file:
        content = file.read()
    
    # Define a regex pattern to find the <extensions> tag and the watts value
    pattern = re.compile(
        r'(<extensions>)(.*?)(<gpxtpx:TrackPointExtension>.*?<gpxtpx:watts>)(\d+)(</gpxtpx:watts>)(.*?)(</gpxtpx:TrackPointExtension>.*?</extensions>)',
        re.DOTALL
    )
    
    # Function to replace the watts with the power element
    def replace_watts_with_power(match):
        before_track_point_extension = match.group(1) + match.group(2)
        watts_value = match.group(4)
        track_point_extension_content = match.group(3) + match.group(5) + match.group(6) + match.group(7)
        power_element = f'<power>{watts_value}</power>'
        return before_track_point_extension + power_element + track_point_extension_content
    
    # Substitute the matched pattern with the new content
    updated_content = pattern.sub(replace_watts_with_power, content)
    
    # Write the updated content to the target file
    with open(file_target_path, 'w') as file:
        file.write(updated_content)
