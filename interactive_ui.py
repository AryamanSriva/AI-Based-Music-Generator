"""
Interactive UI for Music Generation
This module provides a Jupyter notebook widget interface for music generation.
"""

from ipywidgets import Textarea, Button, VBox, HBox, Output
from IPython.display import display, Audio, clear_output
from music_generator import MusicGenerator
import datetime


class MusicGeneratorUI:
    """Interactive UI for music generation using ipywidgets."""
    
    def __init__(self, model_name='facebook/musicgen-small', duration=8):
        """
        Initialize the UI.
        
        Args:
            model_name (str): The pretrained model to use
            duration (int): Duration of generated music in seconds
        """
        self.generator = MusicGenerator(model_name, duration)
        self.setup_widgets()
        self.generated_count = 0
        
    def setup_widgets(self):
        """Setup all UI widgets."""
        # Text input for music description
        self.description = Textarea(
            value='',
            placeholder='Enter a music prompt (e.g., "upbeat rock song with guitar solo")',
            description='Music Prompt:',
            disabled=False,
            rows=4,
            layout={'width': '500px'}
        )
        
        # Generate button
        self.generate_button = Button(
            description="Generate Music",
            button_style='primary',
            layout={'width': '150px'}
        )
        
        # Status output
        self.status_output = Output()
        
        # Audio output
        self.audio_output = Output()
        
        # Connect button to function
        self.generate_button.on_click(self.generate_music)
        
    def initialize_model(self):
        """Initialize the music generation model."""
        with self.status_output:
            clear_output(wait=True)
            print("Initializing model...")
            
        try:
            self.generator.load_model()
            self.generator.configure_model()
            
            with self.status_output:
                clear_output(wait=True)
                print("✅ Model loaded successfully! Ready to generate music.")
                
        except Exception as e:
            with self.status_output:
                clear_output(wait=True)
                print(f"❌ Error loading model: {str(e)}")
                
    def generate_music(self, button):
        """
        Generate music based on user input.
        
        Args:
            button: The button widget that triggered this function
        """
        prompt = self.description.value.strip()
        
        if not prompt:
            with self.status_output:
                clear_output(wait=True)
                print("⚠️ Please enter a music prompt!")
            return
            
        # Disable button during generation
        self.generate_button.disabled = True
        self.generate_button.description = "Generating..."
        
        with self.status_output:
            clear_output(wait=True)
            print(f"🎵 Generating music for: '{prompt}'")
            print("This may take a few moments...")
            
        try:
            # Generate music
            audio_data, sampling_rate = self.generator.generate_music(prompt)
            
            # Display audio player
            with self.audio_output:
                clear_output(wait=True)
                audio_widget = Audio(audio_data, rate=sampling_rate)
                display(audio_widget)
                
            # Save audio file
            self.generated_count += 1
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_music_{self.generated_count}_{timestamp}.wav"
            self.generator.save_audio(audio_data, filename)
            
            with self.status_output:
                clear_output(wait=True)
                print(f"✅ Music generated successfully!")
                print(f"💾 Saved as: {filename}")
                print(f"⏱️ Duration: {len(audio_data[0]) / sampling_rate:.1f} seconds")
                
        except Exception as e:
            with self.status_output:
                clear_output(wait=True)
                print(f"❌ Error generating music: {str(e)}")
                
        finally:
            # Re-enable button
            self.generate_button.disabled = False
            self.generate_button.description = "Generate Music"
            
    def display(self):
        """Display the complete UI."""
        # Initialize model first
        self.initialize_model()
        
        # Create layout
        ui = VBox([
            self.description,
            HBox([self.generate_button]),
            self.status_output,
            self.audio_output
        ])
        
        display(ui)


def create_simple_ui():
    """Create a simple version of the UI (original notebook style)."""
    generator = MusicGenerator()
    
    # Load and configure model
    generator.load_model()
    generator.configure_model()
    
    # Create widgets
    description = Textarea(
        value='', 
        placeholder='Give a music prompt', 
        disabled=False, 
        rows=4
    )
    generate_button = Button(description="Generate Tune")
    
    def generate_tune(event):
        """Generate music when button is clicked."""
        if description.value.strip():
            results, sampling_rate = generator.generate_music(description.value)
            display(Audio(results, rate=sampling_rate))
    
    # Connect button click
    generate_button.on_click(generate_tune)
    
    # Display UI
    display(description)
    display(generate_button)


if __name__ == "__main__":
    # This will work in Jupyter notebook environment
    print("Creating Music Generator UI...")
    ui = MusicGeneratorUI()
    ui.display()
