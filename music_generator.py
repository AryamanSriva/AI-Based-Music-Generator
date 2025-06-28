"""
Music Generator using MusicGen AI Model
This module provides functionality to generate music using Facebook's MusicGen model.
"""

import torchaudio
import audiocraft
from audiocraft.models import MusicGen
from IPython.display import Audio
import torch
import numpy as np


class MusicGenerator:
    """A class to handle music generation using MusicGen AI model."""
    
    def __init__(self, model_name='facebook/musicgen-small', duration=8):
        """
        Initialize the MusicGenerator.
        
        Args:
            model_name (str): The pretrained model to use
            duration (int): Duration of generated music in seconds
        """
        self.model_name = model_name
        self.duration = duration
        self.model = None
        self.sampling_rate = None
        
    def load_model(self):
        """Load the pretrained MusicGen model."""
        print(f"Loading model: {self.model_name}")
        self.model = MusicGen.get_pretrained(self.model_name)
        self.sampling_rate = self.model.sample_rate
        print(f"Model loaded successfully. Sample rate: {self.sampling_rate}")
        
    def configure_model(self, duration=None):
        """
        Configure model parameters.
        
        Args:
            duration (int, optional): Duration in seconds. If None, uses instance duration.
        """
        if self.model is None:
            raise ValueError("Model not loaded. Call load_model() first.")
            
        duration = duration or self.duration
        self.model.set_generation_params(duration=duration)
        print(f"Model configured with duration: {duration} seconds")
        
    def generate_music(self, prompt):
        """
        Generate music based on text prompt.
        
        Args:
            prompt (str): Text description of the music to generate
            
        Returns:
            tuple: (audio_data, sampling_rate)
        """
        if self.model is None:
            raise ValueError("Model not loaded. Call load_model() first.")
            
        print(f"Generating music for prompt: '{prompt}'")
        results = self.model.generate([prompt])
        audio_data = results[0].numpy()
        
        return audio_data, self.sampling_rate
        
    def save_audio(self, audio_data, filename, sampling_rate=None):
        """
        Save generated audio to file.
        
        Args:
            audio_data: Audio data as numpy array
            filename (str): Output filename
            sampling_rate (int, optional): Sampling rate. Uses model's rate if None.
        """
        sampling_rate = sampling_rate or self.sampling_rate
        
        # Convert to tensor if numpy array
        if isinstance(audio_data, np.ndarray):
            audio_tensor = torch.from_numpy(audio_data)
        else:
            audio_tensor = audio_data
            
        torchaudio.save(filename, audio_tensor, sampling_rate)
        print(f"Audio saved to: {filename}")
        
    def play_audio(self, audio_data, sampling_rate=None):
        """
        Play audio in Jupyter notebook environment.
        
        Args:
            audio_data: Audio data as numpy array
            sampling_rate (int, optional): Sampling rate. Uses model's rate if None.
            
        Returns:
            IPython.display.Audio object
        """
        sampling_rate = sampling_rate or self.sampling_rate
        return Audio(audio_data, rate=sampling_rate)


def main():
    """Example usage of MusicGenerator."""
    # Initialize generator
    generator = MusicGenerator(duration=8)
    
    # Load model
    generator.load_model()
    
    # Configure model
    generator.configure_model()
    
    # Generate music examples
    prompts = [
        'classic rock song',
        'rock song',
        'upbeat rock song with guitar solo'
    ]
    
    for i, prompt in enumerate(prompts):
        print(f"\n--- Generating example {i+1} ---")
        audio_data, sample_rate = generator.generate_music(prompt)
        
        # Save to file
        filename = f"generated_music_{i+1}.wav"
        generator.save_audio(audio_data, filename)
        
        print(f"Generated audio shape: {audio_data.shape}")
        print(f"Sample rate: {sample_rate}")


if __name__ == "__main__":
    main()
