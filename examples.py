"""
Example scripts for music generation.
This module contains various examples showing different ways to use the MusicGenerator.
"""

from music_generator import MusicGenerator
import os
import time


def basic_example():
    """Basic example of music generation."""
    print("=== BASIC MUSIC GENERATION EXAMPLE ===")
    
    # Initialize generator
    generator = MusicGenerator(duration=8)
    generator.load_model()
    generator.configure_model()
    
    # Generate a simple rock song
    prompt = "classic rock song"
    audio_data, sample_rate = generator.generate_music(prompt)
    
    # Save the result
    generator.save_audio(audio_data, "basic_example.wav")
    print("Basic example completed!")


def multiple_prompts_example():
    """Generate music for multiple prompts."""
    print("\n=== MULTIPLE PROMPTS EXAMPLE ===")
    
    generator = MusicGenerator(duration=10)
    generator.load_model()
    generator.configure_model()
    
    prompts = [
        "upbeat electronic dance music",
        "slow jazz piano ballad",
        "acoustic guitar folk song",
        "heavy metal with drums",
        "ambient atmospheric soundscape"
    ]
    
    for i, prompt in enumerate(prompts):
        print(f"\nGenerating {i+1}/{len(prompts)}: {prompt}")
        
        try:
            audio_data, sample_rate = generator.generate_music(prompt)
            filename = f"example_{i+1}_{prompt.replace(' ', '_')}.wav"
            generator.save_audio(audio_data, filename)
            print(f"✅ Saved: {filename}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            
        # Small delay between generations
        time.sleep(1)


def different_durations_example():
    """Example showing different music durations."""
    print("\n=== DIFFERENT DURATIONS EXAMPLE ===")
    
    generator = MusicGenerator()
    generator.load_model()
    
    durations = [5, 10, 15, 20]
    prompt = "upbeat pop song with vocals"
    
    for duration in durations:
        print(f"\nGenerating {duration}s version...")
        generator.configure_model(duration=duration)
        
        audio_data, sample_rate = generator.generate_music(prompt)
        filename = f"pop_song_{duration}s.wav"
        generator.save_audio(audio_data, filename)
        
        print(f"✅ Generated {duration}s track: {filename}")


def genre_exploration_example():
    """Explore different music genres."""
    print("\n=== GENRE EXPLORATION EXAMPLE ===")
    
    generator = MusicGenerator(duration=12)
    generator.load_model()
    generator.configure_model()
    
    genres = {
        "rock": "energetic rock song with electric guitar",
        "jazz": "smooth jazz with saxophone and piano",
        "classical": "orchestral classical music with strings",
        "hip_hop": "hip hop beat with bass and drums",
        "country": "country music with acoustic guitar and banjo",
        "reggae": "reggae song with guitar and steady rhythm",
        "blues": "slow blues with guitar and harmonica"
    }
    
    # Create genre folder
    genre_folder = "genre_examples"
    os.makedirs(genre_folder, exist_ok=True)
    
    for genre, prompt in genres.items():
        print(f"\n🎵 Generating {genre.upper()} music...")
        print(f"Prompt: {prompt}")
        
        try:
            audio_data, sample_rate = generator.generate_music(prompt)
            filename = os.path.join(genre_folder, f"{genre}_example.wav")
            generator.save_audio(audio_data, filename)
            print(f"✅ Saved: {filename}")
            
        except Exception as e:
            print(f"❌ Error generating {genre}: {e}")


def prompt_refinement_example():
    """Show how prompt refinement affects output."""
    print("\n=== PROMPT REFINEMENT EXAMPLE ===")
    
    generator = MusicGenerator(duration=8)
    generator.load_model()
    generator.configure_model()
    
    # Progressive prompt refinement
    prompts = [
        "rock song",
        "upbeat rock song",
        "upbeat rock song with guitar",
        "upbeat rock song with guitar solo",
        "upbeat rock song with guitar solo and drums"
    ]
    
    refinement_folder = "prompt_refinement"
    os.makedirs(refinement_folder, exist_ok=True)
    
    for i, prompt in enumerate(prompts):
        print(f"\n🎯 Refinement level {i+1}: {prompt}")
        
        try:
            audio_data, sample_rate = generator.generate_music(prompt)
            filename = os.path.join(refinement_folder, f"refinement_{i+1}.wav")
            generator.save_audio(audio_data, filename)
            print(f"✅ Generated: {filename}")
            
        except Exception as e:
            print(f"❌ Error: {e}")


def batch_generation_example():
    """Generate multiple variations of the same prompt."""
    print("\n=== BATCH GENERATION EXAMPLE ===")
    
    generator = MusicGenerator(duration=8)
    generator.load_model()
    generator.configure_model()
    
    prompt = "chill lo-fi hip hop beat"
    num_variations = 3
    
    batch_folder = "batch_generation"
    os.makedirs(batch_folder, exist_ok=True)
    
    print(f"Generating {num_variations} variations of: '{prompt}'")
    
    for i in range(num_variations):
        print(f"\n🔄 Generating variation {i+1}/{num_variations}...")
        
        try:
            audio_data, sample_rate = generator.generate_music(prompt)
            filename = os.path.join(batch_folder, f"variation_{i+1}.wav")
            generator.save_audio(audio_data, filename)
            print(f"✅ Saved variation {i+1}: {filename}")
            
        except Exception as e:
            print(f"❌ Error generating variation {i+1}: {e}")


def run_all_examples():
    """Run all examples."""
    print("🎵 MUSICGEN AI - EXAMPLE SHOWCASE 🎵")
    print("=" * 50)
    
    examples = [
        basic_example,
        multiple_prompts_example,
        different_durations_example,
        genre_exploration_example,
        prompt_refinement_example,
        batch_generation_example
    ]
    
    for example_func in examples:
        try:
            example_func()
            print("\n" + "-" * 50)
            time.sleep(2)  # Brief pause between examples
            
        except KeyboardInterrupt:
            print("\n⏹️ Examples interrupted by user.")
            break
        except Exception as e:
            print(f"\n❌ Error running {example_func.__name__}: {e}")
            continue
    
    print("\n🎉 All examples completed!")
    print("Check the generated audio files in your current directory.")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        example_name = sys.argv[1]
        
        if example_name == "basic":
            basic_example()
        elif example_name == "multiple":
            multiple_prompts_example()
        elif example_name == "durations":
            different_durations_example()
        elif example_name == "genres":
            genre_exploration_example()
        elif example_name == "refinement":
            prompt_refinement_example()
        elif example_name == "batch":
            batch_generation_example()
        elif example_name == "all":
            run_all_examples()
        else:
            print("Available examples: basic, multiple, durations, genres, refinement, batch, all")
    else:
        run_all_examples()
