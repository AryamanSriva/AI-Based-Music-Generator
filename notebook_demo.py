"""
Jupyter Notebook Demo Script
This script replicates the original notebook functionality for Jupyter environments.
"""

# Import all necessary packages (Task 1)
import torchaudio
import audiocraft
from audiocraft.models import MusicGen
from IPython.display import Audio, display
from ipywidgets import Textarea, Button

print("✅ All packages imported successfully!")

# Load pretrained model (Task 2)
print("Loading MusicGen model...")
model = MusicGen.get_pretrained('facebook/musicgen-small')
print("✅ Model loaded successfully!")

# Configure model parameters (Task 3)
model.set_generation_params(duration=8)
print("✅ Model configured with 8-second duration!")

# Generate music (Task 4)
print("Generating sample music...")
results = model.generate(['classic rock song'])
sampling_rate = model.sample_rate
print("✅ Sample music generated!")

# Display audio player
print("🎵 Playing generated music:")
display(Audio(results[0].numpy(), rate=sampling_rate))

# Build text input (Task 5)
print("\nCreating text input widget...")
description = Textarea(rows=4)
display(description)

# Generate button (Task 6)
print("Creating generate button...")
generate_button = Button(description="Generate Tune")
display(generate_button)

# Connect UI to model (Task 7)
print("Setting up interactive interface...")

# Recreate widgets with better configuration
description = Textarea(
    value='', 
    placeholder='Give a music prompt', 
    disabled=False, 
    rows=4
)

generate_button = Button(description="Generate Tune")

# Function to generate music as prompted
def generate_tune(event):
    """Generate music based on user input."""
    if description.value.strip():
        print(f"🎵 Generating: '{description.value}'")
        results = model.generate([description.value])
        sampling_rate = model.sample_rate
        display(Audio(results[0].numpy(), rate=sampling_rate))
    else:
        print("⚠️ Please enter a music prompt!")

# Create click event on the button
generate_button.on_click(generate_tune)

# Display the UI items
print("🎛️ Interactive Music Generator Ready!")
display(description)
display(generate_button)

# Refine prompts examples (Task 8)
print("\n" + "="*50)
print("PROMPT REFINEMENT EXAMPLES")
print("="*50)

# Example 1: Simple prompt
print("\n🎵 Example 1: Simple 'rock song'")
results = model.generate(['rock song'])
sampling_rate = model.sample_rate
display(Audio(results[0].numpy(), rate=sampling_rate))

# Example 2: Detailed prompt
print("\n🎵 Example 2: Detailed 'upbeat rock song with guitar solo'")
results = model.generate(['upbeat rock song with guitar solo'])
sampling_rate = model.sample_rate
display(Audio(results[0].numpy(), rate=sampling_rate))

print("\n✨ Notebook demo completed!")
print("Try entering different prompts in the text area above and click 'Generate Tune'")

# Additional helper functions for notebook users
def quick_generate(prompt, duration=8):
    """
    Quick function to generate music with a prompt.
    
    Args:
        prompt (str): Music description
        duration (int): Duration in seconds
    
    Returns:
        IPython.display.Audio: Audio player widget
    """
    model.set_generation_params(duration=duration)
    results = model.generate([prompt])
    sampling_rate = model.sample_rate
    return Audio(results[0].numpy(), rate=sampling_rate)

def save_generated_music(prompt, filename, duration=8):
    """
    Generate and save music to file.
    
    Args:
        prompt (str): Music description
        filename (str): Output filename
        duration (int): Duration in seconds
    """
    model.set_generation_params(duration=duration)
    results = model.generate([prompt])
    sampling_rate = model.sample_rate
    
    # Save audio
    torchaudio.save(filename, results[0], sampling_rate)
    print(f"💾 Music saved as: {filename}")
    
    return Audio(results[0].numpy(), rate=sampling_rate)

# Example usage instructions
print("\n" + "="*50)
print("HELPER FUNCTIONS AVAILABLE:")
print("="*50)
print("1. quick_generate(prompt, duration=8)")
print("   - Quick music generation")
print("   - Example: quick_generate('jazz piano', 10)")
print()
print("2. save_generated_music(prompt, filename, duration=8)")
print("   - Generate and save music")
print("   - Example: save_generated_music('blues', 'my_blues.wav', 12)")
print()
print("Try these functions in new cells!")
